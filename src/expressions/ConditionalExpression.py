#!/usr/bin/env python
""" generated source for module ConditionalExpression """
# package: com.stuffwithstuff.bantam.expressions
# /**
#  * A ternary conditional expression like "a ? b : c".
#  */
class ConditionalExpression(Expression):
    """ generated source for class ConditionalExpression """
    def __init__(self, condition, thenArm, elseArm):
        """ generated source for method __init__ """
        super(ConditionalExpression, self).__init__()
        mCondition = condition
        mThenArm = thenArm
        mElseArm = elseArm

    def print(self, builder):
        """ generated source for method print """
        builder.append("(")
        mCondition.print(builder)
        builder.append(" ? ")
        mThenArm.print(builder)
        builder.append(" : ")
        mElseArm.print(builder)
        builder.append(")")

    mCondition = None
    mThenArm = None
    mElseArm = None

