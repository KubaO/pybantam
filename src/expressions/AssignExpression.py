#!/usr/bin/env python
""" generated source for module AssignExpression """
# package: com.stuffwithstuff.bantam.expressions
# /**
#  * An assignment expression like "a = b".
#  */
class AssignExpression(Expression):
    """ generated source for class AssignExpression """
    def __init__(self, name, right):
        """ generated source for method __init__ """
        super(AssignExpression, self).__init__()
        mName = name
        mRight = right

    def print(self, builder):
        """ generated source for method print """
        builder.append("(").append(mName).append(" = ")
        mRight.print(builder)
        builder.append(")")

    mName = None
    mRight = None

