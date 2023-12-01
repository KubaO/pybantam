#!/usr/bin/env python
""" generated source for module CallExpression """
# package: com.stuffwithstuff.bantam.expressions
# /**
#  * A function call like "a(b, c, d)".
#  */
class CallExpression(Expression):
    """ generated source for class CallExpression """
    def __init__(self, function_, args):
        """ generated source for method __init__ """
        super(CallExpression, self).__init__()
        mFunction = function_
        mArgs = args

    def print(self, builder):
        """ generated source for method print """
        mFunction.print(builder)
        builder.append("(")
        i = 0
        while i < len(mArgs):
            mArgs.get(i).print(builder)
            if i < len(mArgs) - 1:
                builder.append(", ")
            i += 1
        builder.append(")")

    mFunction = None
    mArgs = None

