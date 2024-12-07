__all__ = ['TokenType', 'Token', 'SCANNER', 'PATTERN_KEYS']

import re
from enum import Enum
from typing import NamedTuple, cast


class TokenType(Enum):
    LEFT_PAREN = '('
    RIGHT_PAREN = ')'
    COMMA = ','
    ASSIGN = '='
    PLUS = '+'
    MINUS = '-'
    ASTERISK = '*'
    SLASH = '/'
    CARET = '^'
    TILDE = '~'
    BANG = '!'
    QUESTION = '?'
    COLON = ':'
    NAME = br'\w+'
    EOF = br'$'

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"

    def __new__(cls, value: str | bytes):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.re = re.escape(value) if isinstance(value, str) else value.decode('utf-8')
        return obj


class Token(NamedTuple):
    """A simple token class. These are generated by Lexer and consumed by Parser."""

    type: TokenType
    text: str

    def __str__(self):
        return self.text


# The scanner uses the regular expression engine.
# Each token type is captured into a group with its name.
# The groups are in the order of TokenType enumerations.
# The regular expression reads: r'(?P<LEFT_PAREN>\()|(?P<RIGHT_PAREN>\))|' ... '(?P<EOF>$)'

SCANNER = re.compile(
    "|".join(f"(?P<{tt.name}>{tt.re})" for tt in TokenType)
)

PATTERN_KEYS = {v: TokenType[k] for k, v in SCANNER.groupindex.items()}
