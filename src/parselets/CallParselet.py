#!/usr/bin/env python
""" generated source for module CallParselet """
# package: com.stuffwithstuff.bantam.parselets
# /**
#  * Parselet to parse a function call like "a(b, c, d)".
#  */
class CallParselet(InfixParselet):
    """ generated source for class CallParselet """
    def parse(self, parser, left, token):
        """ generated source for method parse """
        # // Parse the comma-separated arguments until we hit, ")".
        args = ArrayList()
        # // There may be no arguments at all.
        if not parser.match(TokenType.RIGHT_PAREN):
            while True:
                args.add(parser.parseExpression())
                if not ((parser.match(TokenType.COMMA))):
                    break
            parser.consume(TokenType.RIGHT_PAREN)
        return CallExpression(left, args)

    def getPrecedence(self):
        """ generated source for method getPrecedence """
        return Precedence.CALL

