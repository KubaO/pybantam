__all__ = ['BantamParser']

from lexer import Lexer
from parselets import *
from parser import Parser, Precedence
from tokens import TokenType


class BantamParser(Parser):
    """Extends the generic Parser class with support for parsing the actual Bantam grammar."""

    def __init__(self, lexer: Lexer):
        super().__init__(lexer)
        # Register all the parselets for the grammar.
        # Register the ones that need special parselets.
        self.register(TokenType.NAME, NameParselet())
        self.register(TokenType.ASSIGN, AssignParselet())
        self.register(TokenType.QUESTION, ConditionalParselet())
        self.register(TokenType.LEFT_PAREN, GroupParselet())
        self.register(TokenType.LEFT_PAREN, CallParselet())
        # Register the simple operator parselets.
        self.prefix(TokenType.PLUS, Precedence.PREFIX)
        self.prefix(TokenType.MINUS, Precedence.PREFIX)
        self.prefix(TokenType.TILDE, Precedence.PREFIX)
        self.prefix(TokenType.BANG, Precedence.PREFIX)
        # For kicks, we'll make "!" both prefix and postfix, kind of like ++.
        self.postfix(TokenType.BANG, Precedence.POSTFIX)
        self.infix_left(TokenType.PLUS, Precedence.SUM)
        self.infix_left(TokenType.MINUS, Precedence.SUM)
        self.infix_left(TokenType.ASTERISK, Precedence.PRODUCT)
        self.infix_left(TokenType.SLASH, Precedence.PRODUCT)
        self.infix_right(TokenType.CARET, Precedence.EXPONENT)

    def postfix(self, token: TokenType, precedence: Precedence):
        """Registers a postfix unary operator parselet for the given token and precedence."""
        self.register(token, PostfixOperatorParselet(precedence))

    def prefix(self, token: TokenType, precedence: Precedence):
        """Registers a prefix unary operator parselet for the given token and precedence."""
        self.register(token, PrefixOperatorParselet(precedence))

    def infix_left(self, token: TokenType, precedence: Precedence):
        """Registers a left-associative binary operator parselet for the given token and
        precedence."""
        self.register(token, BinaryOperatorParselet(precedence, False))

    def infix_right(self, token: TokenType, precedence: Precedence):
        """Registers a right-associative binary operator parselet for the given token and
        precedence."""
        self.register(token, BinaryOperatorParselet(precedence, True))
