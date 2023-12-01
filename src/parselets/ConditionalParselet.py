#!/usr/bin/env python
""" generated source for module ConditionalParselet """
# package: com.stuffwithstuff.bantam.parselets
# /**
#  * Parselet for the condition or "ternary" operator, like "a ? b : c".
#  */
class ConditionalParselet(InfixParselet):
    """ generated source for class ConditionalParselet """
    def parse(self, parser, left, token):
        """ generated source for method parse """
        thenArm = parser.parseExpression()
        parser.consume(TokenType.COLON)
        elseArm = parser.parseExpression(Precedence.CONDITIONAL - 1)
        return ConditionalExpression(left, thenArm, elseArm)

    def getPrecedence(self):
        """ generated source for method getPrecedence """
        return Precedence.CONDITIONAL

