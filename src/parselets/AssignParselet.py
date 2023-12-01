#!/usr/bin/env python
""" generated source for module AssignParselet """
# package: com.stuffwithstuff.bantam.parselets
# /**
#  * Parses assignment expressions like "a = b". The left side of an assignment
#  * expression must be a simple name like "a", and expressions are
#  * right-associative. (In other words, "a = b = c" is parsed as "a = (b = c)").
#  */
class AssignParselet(InfixParselet):
    """ generated source for class AssignParselet """
    def parse(self, parser, left, token):
        """ generated source for method parse """
        right = parser.parseExpression(Precedence.ASSIGNMENT - 1)
        if not (isinstance(left, (NameExpression, ))):
            raise ParseException("The left-hand side of an assignment must be a name.")
        name = (left).__name__
        return AssignExpression(name, right)

    def getPrecedence(self):
        """ generated source for method getPrecedence """
        return Precedence.ASSIGNMENT

