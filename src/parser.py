__all__ = ['ParseException', 'Precedence', 'InfixParselet', 'PrefixParselet', 'Parser',]

from abc import ABC, abstractmethod
from collections.abc import Iterator
from enum import Enum, unique
from tokens import Token, TokenType
from expressions import Expression


class ParseException(RuntimeError):
    def __init__(self, message: str) -> None:
        super().__init__(message)

    @property
    def message(self):
        return self.args[0]


@unique
class Precedence(Enum):
    """Defines the different precedence levels used by the infix parsers.

    These determine how a series of infix expressions will be grouped. For example,
    "a + b * c - d" will be parsed as "(a + (b * c)) - d" because "*" has higher
    precedence than "+" and "-". Here, bigger numbers mean higher precedence.
    """

    # In order of increasing precedence.
    BELOW_ASSIGNMENT = 0
    ASSIGNMENT = 1
    CONDITIONAL = 2
    SUM = 3
    PRODUCT = 4
    EXPONENT = 5
    PREFIX = 6
    POSTFIX = 7
    CALL = 8

    def one_lower(self) -> 'Precedence':
        return Precedence(self.value - 1)

    def __lt__(self, other: 'Precedence'):
        return self.value < other.value


class InfixParselet(ABC):
    """One of the two parselet interfaces used by the Pratt parser.

    An InfixParselet is associated with a token that appears in the middle of the
    expression it parses. Its parse() method will be called after the left-hand
    side has been parsed, and it in turn is responsible for parsing everything
    that comes after the token. This is also used for postfix expressions, in
    which case it simply doesn't consume any more tokens in its parse() call.
    """

    @abstractmethod
    def parse(self, parser: 'Parser', left: Expression,
              token: Token) -> Expression:
        pass

    @property
    @abstractmethod
    def precedence(self) -> Precedence:
        pass


class PrefixParselet(ABC):
    """One of the two interfaces used by the Pratt parser.

    A PrefixParselet is associated with a token that appears at the beginning of an
    expression. Its parse() method will be called with the consumed leading token, and
    the parselet is responsible for parsing anything that comes after that token.
    This interface is also used for single-token expressions like variables, in
    which case parse() simply doesn't consume any more tokens.
    """

    @abstractmethod
    def parse(self, parser: 'Parser', token: Token) -> Expression:
        pass


class Parser:
    def __init__(self, tokens: Iterator[Token]):
        self.tokens = tokens
        self.read: list[Token] = []
        self.prefix_parselets: dict[TokenType, PrefixParselet] = {}
        self.infix_parselets: dict[TokenType, InfixParselet] = {}

    def register(self, token: TokenType, parselet: PrefixParselet | InfixParselet):
        if isinstance(parselet, PrefixParselet):
            self.prefix_parselets[token] = parselet
        elif isinstance(parselet, InfixParselet):
            self.infix_parselets[token] = parselet
        else:
            raise NotImplementedError()

    def parse_expression(self, precedence: Precedence = Precedence(0)) -> Expression:
        token = self.consume()
        prefix = self.prefix_parselets.get(token.type, None)
        if not prefix:
            raise ParseException(f"Could not parse \"{token.text}\".")
        left = prefix.parse(self, token)
        while precedence < self.precedence:
            token = self.consume()
            infix = self.infix_parselets[token.type]
            left = infix.parse(self, left, token)
        return left

    def match(self, expected: TokenType) -> bool:
        token = self.look_ahead(0)
        if token.type != expected:
            return False
        self.consume()
        return True

    def _consume_0(self) -> Token:
        # Make sure we've read the token.
        self.look_ahead(0)
        return self.read.pop(0)

    def consume(self, expected: TokenType | None = None) -> Token:
        if not expected:
            return self._consume_0()
        token = self.look_ahead(0)
        if token.type != expected:
            raise RuntimeError(
                f"Expected token {expected} and found {token.type}")
        return self.consume()

    def look_ahead(self, distance: int):
        # Read in as many as needed.
        while distance >= len(self.read):
            self.read.append(next(self.tokens))
        # Get the queued token.
        return self.read[distance]

    @property
    def precedence(self):
        parser = self.infix_parselets.get(self.look_ahead(0).type, None)
        if parser:
            return parser.precedence
        return Precedence(0)
