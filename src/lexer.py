__all__ = ['lex']

import re
from collections.abc import Iterable

from tokens import Token, TokenType, TOKEN_PATTERNS

_scanner = re.compile(
    "|".join(f"(?P<{token.name}>{patt})" for token, patt in TOKEN_PATTERNS.items())
)
# The scanner uses the regular expression engine.
# Each token type is captured into a group with its name.
# The groups are in the order of TokenType enumerations.
# The regular expression reads: r'(?P<LEFT_PAREN>\()|(?P<RIGHT_PAREN>\))|' ... '(?P<EOF>$)'


_pattern_keys: list[TokenType] = list(TOKEN_PATTERNS.keys())


def lex(text: str) -> Iterable[Token]:
    """
    A simple lexer that yields tokens.

    Takes a string and splits it into a series of Tokens.
    Numbers and strings are not supported. This is really just the bare
    minimum to give the parser something to work with.
    """

    for match in _scanner.finditer(text):
        i, value = next(filter(lambda ir: ir[1] is not None, enumerate(match.groups())))
        type_ = _pattern_keys[i]
        yield Token(type_, value)

    # The above loop will yield one EOF token. We'll
    # just keep returning them as many times as we're asked so that the
    # parser's lookahead doesn't have to worry about running out of tokens.
    yield Token(TokenType.EOF, "")
