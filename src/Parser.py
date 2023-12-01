#!/usr/bin/env python
""" generated source for module Parser """
# package: com.stuffwithstuff.bantam
class Parser(object):
    """ generated source for class Parser """
    def __init__(self, tokens):
        """ generated source for method __init__ """
        mTokens = tokens

    @overloaded
    def register(self, token, parselet):
        """ generated source for method register """
        mPrefixParselets.put(token, parselet)

    @register.register(object, TokenType, InfixParselet)
    def register_0(self, token, parselet):
        """ generated source for method register_0 """
        mInfixParselets.put(token, parselet)

    @overloaded
    def parseExpression(self, precedence):
        """ generated source for method parseExpression """
        token = consume()
        prefix = mPrefixParselets.get(token.getType())
        if prefix == None:
            raise ParseException("Could not parse \"" + token.getText() + "\".")
        left = prefix.parse(self, token)
        while precedence < getPrecedence():
            token = consume()
            infix = mInfixParselets.get(token.getType())
            left = infix.parse(self, left, token)
        return left

    @parseExpression.register(object)
    def parseExpression_0(self):
        """ generated source for method parseExpression_0 """
        return self.parseExpression(0)

    def match(self, expected):
        """ generated source for method match """
        token = lookAhead(0)
        if token.getType() != expected:
            return False
        consume()
        return True

    @overloaded
    def consume(self, expected):
        """ generated source for method consume """
        token = lookAhead(0)
        if token.getType() != expected:
            raise RuntimeException("Expected token " + expected + " and found " + token.getType())
        return self.consume()

    @consume.register(object)
    def consume_0(self):
        """ generated source for method consume_0 """
        # // Make sure we've read the token.
        lookAhead(0)
        return mRead.remove(0)

    def lookAhead(self, distance):
        """ generated source for method lookAhead """
        # // Read in as many as needed.
        while distance >= len(mRead):
            mRead.add(mTokens.next())
        # // Get the queued token.
        return mRead.get(distance)

    def getPrecedence(self):
        """ generated source for method getPrecedence """
        parser = mInfixParselets.get(self.lookAhead(0).getType())
        if parser != None:
            return parser.getPrecedence()
        return 0

    mTokens = None
    mRead = ArrayList()
    mPrefixParselets = HashMap()
    mInfixParselets = HashMap()

