#!/usr/bin/env python
""" generated source for module OperatorExpression """
# package: com.stuffwithstuff.bantam.expressions
# /**
#  * A binary arithmetic expression like "a + b" or "c ^ d".
#  */
class OperatorExpression(Expression):
    """ generated source for class OperatorExpression """
    def __init__(self, left, operator, right):
        """ generated source for method __init__ """
        super(OperatorExpression, self).__init__()
        mLeft = left
        mOperator = operator
        mRight = right

    def print(self, builder):
        """ generated source for method print """
        builder.append("(")
        mLeft.print(builder)
        builder.append(" ").append(mOperator.punctuator()).append(" ")
        mRight.print(builder)
        builder.append(")")

    mLeft = None
    mOperator = None
    mRight = None

