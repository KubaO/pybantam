__all__ = ['lex']

from collections.abc import Iterable

from tokens import Token, TokenType, SCANNER, PATTERN_KEYS


def _match_to_token(match) -> Token:
    i = match.lastindex
    value = match[i]
    type_ = PATTERN_KEYS[i]
    return Token(type_, value)


def lex(text: str) -> Iterable[Token]:
    """
    A simple lexer that yields tokens.

    Takes a string and splits it into a series of Tokens.
    Numbers and string literals are not supported. This is really just the bare
    minimum to give the parser something to work with.
    """

    yield from map(_match_to_token, SCANNER.finditer(text))

    # The above loop will yield one EOF token. We'll
    # just keep returning them as many times as we're asked so that the
    # parser's lookahead doesn't have to worry about running out of tokens.
    while True:
        yield Token(TokenType.EOF, "")
