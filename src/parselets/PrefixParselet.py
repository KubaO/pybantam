#!/usr/bin/env python
""" generated source for module PrefixParselet """
from abc import ABCMeta, abstractmethod
# package: com.stuffwithstuff.bantam.parselets
# /**
#  * One of the two interfaces used by the Pratt parser. A PrefixParselet is
#  * associated with a token that appears at the beginning of an expression. Its
#  * parse() method will be called with the consumed leading token, and the
#  * parselet is responsible for parsing anything that comes after that token.
#  * This interface is also used for single-token expressions like variables, in
#  * which case parse() simply doesn't consume any more tokens.
#  * @author rnystrom
#  *
#  */
class PrefixParselet(object):
    """ generated source for interface PrefixParselet """
    __metaclass__ = ABCMeta
    @abstractmethod
    def parse(self, parser, token):
        """ generated source for method parse """

