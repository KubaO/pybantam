#!/usr/bin/env python
""" generated source for module NameParselet """
# package: com.stuffwithstuff.bantam.parselets
# /**
#  * Simple parselet for a named variable like "abc".
#  */
class NameParselet(PrefixParselet):
    """ generated source for class NameParselet """
    def parse(self, parser, token):
        """ generated source for method parse """
        return NameExpression(token.getText())

