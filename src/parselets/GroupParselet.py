#!/usr/bin/env python
""" generated source for module GroupParselet """
# package: com.stuffwithstuff.bantam.parselets
# /**
#  * Parses parentheses used to group an expression, like "a * (b + c)".
#  */
class GroupParselet(PrefixParselet):
    """ generated source for class GroupParselet """
    def parse(self, parser, token):
        """ generated source for method parse """
        expression = parser.parseExpression()
        parser.consume(TokenType.RIGHT_PAREN)
        return expression

