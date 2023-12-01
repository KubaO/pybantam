#!/usr/bin/env python
""" generated source for module PostfixExpression """
# package: com.stuffwithstuff.bantam.expressions
# /**
#  * A postfix unary arithmetic expression like "a!".
#  */
class PostfixExpression(Expression):
    """ generated source for class PostfixExpression """
    def __init__(self, left, operator):
        """ generated source for method __init__ """
        super(PostfixExpression, self).__init__()
        mLeft = left
        mOperator = operator

    def print(self, builder):
        """ generated source for method print """
        builder.append("(")
        mLeft.print(builder)
        builder.append(mOperator.punctuator()).append(")")

    mLeft = None
    mOperator = None

