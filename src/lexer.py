__all__ = ['Lexer']

from collections.abc import Iterator
from tokens import Token, TokenType


class Lexer(Iterator[Token]):
    """A very primitive lexer.

    Takes a string and splits it into a series of Tokens. Operators and
    punctuation are mapped to unique keywords. Names,
    which can be any series of letters, are turned into NAME tokens. All other
    characters are ignored (except to separate names). Numbers and strings are
    not supported. This is really just the bare minimum to give the parser
    something to work with.
    """

    def __init__(self, text: str):
        """Creates a new Lexer to tokenize the given string.

        text -- the string to tokenize
        """
        super().__init__()
        self.index = 0
        self.text = text
        self.punctuators: dict[str, TokenType] = {}
        # Register all of the TokenTypes that are explicit punctuators.
        for _type in TokenType:
            punctuator = _type.punctuator
            if punctuator is not None:
                self.punctuators[punctuator] = _type

    def __next__(self) -> Token:
        while self.index < len(self.text):
            c = self.text[self.index]
            self.index += 1
            if c in self.punctuators:
                # Handle punctuation.
                return Token(self.punctuators[c], c)
            if c.isalpha():
                # Handle names.
                start = self.index - 1
                while self.index < len(self.text):
                    if not self.text[self.index].isalpha():
                        break
                    self.index += 1
                name = self.text[start: self.index]
                return Token(TokenType.NAME, name)
            # Ignore all other characters (whitespace, etc.)
        # Once we've reached the end of the string, just return EOF tokens. We'll
        # just keeping returning them as many times as we're asked so that the
        # parser's lookahead doesn't have to worry about running out of tokens.
        return Token(TokenType.EOF, "")


