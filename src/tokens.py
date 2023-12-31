__all__ = ['TokenType', 'Token']


from enum import Enum, unique
from typing import NamedTuple


@unique
class TokenType(Enum):
    LEFT_PAREN = 'LEFT_PAREN'
    RIGHT_PAREN = 'RIGHT_PAREN'
    COMMA = 'COMMA'
    ASSIGN = 'ASSIGN'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    ASTERISK = 'ASTERISK'
    SLASH = 'SLASH'
    CARET = 'CARET'
    TILDE = 'TILDE'
    BANG = 'BANG'
    QUESTION = 'QUESTION'
    COLON = 'COLON'
    NAME = 'NAME'
    EOF = 'EOF'

    @property
    def punctuator(self) -> str | None:
        """Gets the text of a punctuator token.

        If the TokenType represents a punctuator (i.e. a token that can split an
        identifier like '+', this will get its text.
        """
        return _punctuators.get(self, None)


_punctuators = {
    TokenType.LEFT_PAREN: '(',
    TokenType.RIGHT_PAREN: ')',
    TokenType.COMMA: ',',
    TokenType.ASSIGN: '=',
    TokenType.PLUS: '+',
    TokenType.MINUS: '-',
    TokenType.ASTERISK: '*',
    TokenType.SLASH: '/',
    TokenType.CARET: '^',
    TokenType.TILDE: '~',
    TokenType.BANG: '!',
    TokenType.QUESTION: '?',
    TokenType.COLON: ':',
}


class Token(NamedTuple):
    """A simple token class. These are generated by Lexer and consumed by Parser."""

    type: TokenType
    text: str

    def __str__(self):
        return self.text
