#!/usr/bin/env python
""" generated source for module BinaryOperatorParselet """
# package: com.stuffwithstuff.bantam.parselets
# /**
#  * Generic infix parselet for a binary arithmetic operator. The only
#  * difference when parsing, "+", "-", "*", "/", and "^" is precedence and
#  * associativity, so we can use a single parselet class for all of those.
#  */
class BinaryOperatorParselet(InfixParselet):
    """ generated source for class BinaryOperatorParselet """
    def __init__(self, precedence, isRight):
        """ generated source for method __init__ """
        super(BinaryOperatorParselet, self).__init__()
        mPrecedence = precedence
        mIsRight = isRight

    def parse(self, parser, left, token):
        """ generated source for method parse """
        # // To handle right-associative operators like "^", we allow a slightly
        # // lower precedence when parsing the right-hand side. This will let a
        # // parselet with the same precedence appear on the right, which will then
        # // take *this* parselet's result as its left-hand argument.
        right = parser.parseExpression(mPrecedence - (1 if mIsRight else 0))
        return OperatorExpression(left, token.getType(), right)

    def getPrecedence(self):
        """ generated source for method getPrecedence """
        return mPrecedence

    mPrecedence = int()
    mIsRight = bool()

