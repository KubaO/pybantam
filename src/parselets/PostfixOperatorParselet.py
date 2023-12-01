#!/usr/bin/env python
""" generated source for module PostfixOperatorParselet """
# package: com.stuffwithstuff.bantam.parselets
# /**
#  * Generic infix parselet for an unary arithmetic operator. Parses postfix
#  * unary "?" expressions.
#  */
class PostfixOperatorParselet(InfixParselet):
    """ generated source for class PostfixOperatorParselet """
    def __init__(self, precedence):
        """ generated source for method __init__ """
        super(PostfixOperatorParselet, self).__init__()
        mPrecedence = precedence

    def parse(self, parser, left, token):
        """ generated source for method parse """
        return PostfixExpression(left, token.getType())

    def getPrecedence(self):
        """ generated source for method getPrecedence """
        return mPrecedence

    mPrecedence = int()

