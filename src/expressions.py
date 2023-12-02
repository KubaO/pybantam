__all__ = [
    'Expression',
    'AssignExpression',
    'CallExpression',
    'ConditionalExpression',
    'NameExpression',
    'OperatorExpression',
    'PostfixExpression',
    'PrefixExpression',
]

from abc import ABC, abstractmethod
from dataclasses import dataclass
from tokens import TokenType


class Expression(ABC):
    """Interface for all expression AST node classes."""

    @abstractmethod
    def __str__(self) -> str:
        """Pretty-print the expression to a string."""


@dataclass(frozen=True)
class AssignExpression(Expression):
    """An assignment expression like "a = b"."""

    name: str
    right: Expression

    def __str__(self):
        return f"({self.name} = {self.right})"


@dataclass(frozen=True)
class CallExpression(Expression):
    """A function call like "a(b, c, d)"."""

    function: Expression
    args: list[Expression]

    def __str__(self):
        return f"{self.function}({', '.join(map(str, self.args))})"


@dataclass(frozen=True)
class ConditionalExpression(Expression):
    """A ternary conditional expression like "a ? b : c"."""

    condition: Expression
    then_arm: Expression
    else_arm: Expression

    def __str__(self):
        return f"({self.condition} ? {self.then_arm} : {self.else_arm})"


@dataclass(frozen=True)
class NameExpression(Expression):
    """A simple variable name expression like "abc"."""

    name: str

    def __str__(self):
        return self.name


@dataclass(frozen=True)
class OperatorExpression(Expression):
    """A binary arithmetic expression like "a + b" or "c ^ d"."""

    left: Expression
    operator: TokenType
    right: Expression

    def __str__(self):
        return f"({self.left} {self.operator.punctuator} {self.right})"


@dataclass(frozen=True)
class PostfixExpression(Expression):
    """A postfix unary arithmetic expression like "a!"."""

    left: Expression
    operator: TokenType

    def __str__(self):
        return f"({self.left}{self.operator.punctuator})"


@dataclass(frozen=True)
class PrefixExpression(Expression):
    """A prefix unary arithmetic expression like "!a" or "-b"."""

    operator: TokenType
    right: Expression

    def __str__(self):
        return f"({self.operator.punctuator}{self.right})"
