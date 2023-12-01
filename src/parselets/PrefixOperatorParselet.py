#!/usr/bin/env python
""" generated source for module PrefixOperatorParselet """
# package: com.stuffwithstuff.bantam.parselets
# /**
#  * Generic prefix parselet for an unary arithmetic operator. Parses prefix
#  * unary "-", "+", "~", and "!" expressions.
#  */
class PrefixOperatorParselet(PrefixParselet):
    """ generated source for class PrefixOperatorParselet """
    def __init__(self, precedence):
        """ generated source for method __init__ """
        super(PrefixOperatorParselet, self).__init__()
        mPrecedence = precedence

    def parse(self, parser, token):
        """ generated source for method parse """
        # // To handle right-associative operators like "^", we allow a slightly
        # // lower precedence when parsing the right-hand side. This will let a
        # // parselet with the same precedence appear on the right, which will then
        # // take *this* parselet's result as its left-hand argument.
        right = parser.parseExpression(mPrecedence)
        return PrefixExpression(token.getType(), right)

    def getPrecedence(self):
        """ generated source for method getPrecedence """
        return mPrecedence

    mPrecedence = int()

