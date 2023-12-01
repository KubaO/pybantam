#!/usr/bin/env python
""" generated source for module PrefixExpression """
# package: com.stuffwithstuff.bantam.expressions
# /**
#  * A prefix unary arithmetic expression like "!a" or "-b".
#  */
class PrefixExpression(Expression):
    """ generated source for class PrefixExpression """
    def __init__(self, operator, right):
        """ generated source for method __init__ """
        super(PrefixExpression, self).__init__()
        mOperator = operator
        mRight = right

    def print(self, builder):
        """ generated source for method print """
        builder.append("(").append(mOperator.punctuator())
        mRight.print(builder)
        builder.append(")")

    mOperator = None
    mRight = None

