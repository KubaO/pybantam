#!/usr/bin/env python
""" generated source for module NameExpression """
# package: com.stuffwithstuff.bantam.expressions
# /**
#  * A simple variable name expression like "abc".
#  */
class NameExpression(Expression):
    """ generated source for class NameExpression """
    def __init__(self, name):
        """ generated source for method __init__ """
        super(NameExpression, self).__init__()
        mName = name

    def getName(self):
        """ generated source for method getName """
        return mName

    def print(self, builder):
        """ generated source for method print """
        builder.append(mName)

    mName = None

