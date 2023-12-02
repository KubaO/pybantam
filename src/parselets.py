__all__ = ['AssignParselet', 'BinaryOperatorParselet', 'CallParselet', 'ConditionalParselet',
           'PostfixOperatorParselet', 'GroupParselet', 'NameParselet', 'PrefixOperatorParselet',
           # from Parser
           'InfixParselet', 'PrefixParselet']

from parser import InfixParselet, PrefixParselet, Parser, Precedence, ParseException
from expressions import *
from tokens import Token, TokenType


class AssignParselet(InfixParselet):
    """Parses assignment expressions like "a = b".

    The left side of an assignment
    expression must be a simple name like "a", and expressions are
    right-associative. (In other words, "a = b = c" is parsed as "a = (b = c)").
    """

    def parse(self, parser: Parser, left: Expression, token: Token):
        right = parser.parse_expression(Precedence.BELOW_ASSIGNMENT)
        if not isinstance(left, (NameExpression, )):
            raise ParseException(
                "The left-hand side of an assignment must be a name.")
        name = left.name
        return AssignExpression(name, right)

    @property
    def precedence(self):
        return Precedence.ASSIGNMENT


class BinaryOperatorParselet(InfixParselet):
    """Generic infix parselet for a binary arithmetic operator.

    The only difference when parsing, "+", "-", "*", "/", and "^" is precedence and
    associativity, so we can use a single parselet class for all of those.
    """

    def __init__(self, precedence: Precedence, is_right: bool):
        super().__init__()
        self._precedence = precedence
        self._is_right = is_right

    def parse(self, parser: Parser, left: Expression, token: Token):
        # To handle right-associative operators like "^", we allow a slightly
        # lower precedence when parsing the right-hand side. This will let a
        # parselet with the same precedence appear on the right, which will then
        # take *this* parselet's result as its left-hand argument.
        precedence = self._precedence.one_lower() if self._is_right else self._precedence
        right = parser.parse_expression(precedence)
        return OperatorExpression(left, token.type, right)

    @property
    def precedence(self):
        return self._precedence


class CallParselet(InfixParselet):
    """Parselet to parse a function call like "a(b, c, d)"."""

    def parse(self, parser: Parser, left: Expression, token: Token):
        # Parse the comma-separated arguments until we hit, ")".
        args: list[Expression] = []
        # There may be no arguments at all.
        if not parser.match(TokenType.RIGHT_PAREN):
            while True:
                args.append(parser.parse_expression())
                if not parser.match(TokenType.COMMA):
                    break
            parser.consume(TokenType.RIGHT_PAREN)
        return CallExpression(left, args)

    @property
    def precedence(self):
        return Precedence.CALL


class ConditionalParselet(InfixParselet):
    """Parselet for the condition or ternary operator, like "a ? b : c"."""

    def parse(self, parser: Parser, left: Expression, token: Token):
        then_arm = parser.parse_expression()
        parser.consume(TokenType.COLON)
        else_arm = parser.parse_expression(Precedence.CONDITIONAL.one_lower())
        return ConditionalExpression(left, then_arm, else_arm)

    @property
    def precedence(self):
        return Precedence.CONDITIONAL


class PostfixOperatorParselet(InfixParselet):
    """Generic infix parselet for an unary arithmetic operator.

    Parses postfix unary "?" expressions.
    """

    def __init__(self, precedence: Precedence):
        super().__init__()
        self._precedence = precedence

    def parse(self, parser: Parser, left: Expression, token: Token):
        return PostfixExpression(left, token.type)

    @property
    def precedence(self):
        return self._precedence


class GroupParselet(PrefixParselet):
    """Parses parentheses used to group an expression, like "a * (b + c)"."""

    def parse(self, parser: Parser, token: Token):
        expression = parser.parse_expression()
        parser.consume(TokenType.RIGHT_PAREN)
        return expression


class NameParselet(PrefixParselet):
    """Simple parselet for a named variable like "abc"."""

    def parse(self, parser: Parser, token: Token):
        return NameExpression(token.text)


class PrefixOperatorParselet(PrefixParselet):
    """Generic prefix parselet for an unary arithmetic operator.

    Parses prefix unary "-", "+", "~", and "!" expressions.
    """

    def __init__(self, precedence: Precedence):
        super().__init__()
        self._precedence = precedence

    def parse(self, parser: Parser, token: Token):
        # To handle right-associative operators like "^", we allow a slightly
        # lower precedence when parsing the right-hand side. This will let a
        # parselet with the same precedence appear on the right, which will then
        # take *this* parselet's result as its left-hand argument.
        right = parser.parse_expression(self._precedence)
        return PrefixExpression(token.type, right)

    @property
    def precedence(self):
        return self._precedence
