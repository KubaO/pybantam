#!/usr/bin/env python
""" generated source for module Lexer """
# package: com.stuffwithstuff.bantam
# /**
#  * A very primitive lexer. Takes a string and splits it into a series of
#  * Tokens. Operators and punctuation are mapped to unique keywords. Names,
#  * which can be any series of letters, are turned into NAME tokens. All other
#  * characters are ignored (except to separate names). Numbers and strings are
#  * not supported. This is really just the bare minimum to give the parser
#  * something to work with.
#  */
class Lexer(Iterator, Token):
    """ generated source for class Lexer """
    # /**
    #    * Creates a new Lexer to tokenize the given string.
    #    * @param text String to tokenize.
    #    */
    def __init__(self, text):
        """ generated source for method __init__ """
        super(Lexer, self).__init__()
        mIndex = 0
        mText = text
        # // Register all of the TokenTypes that are explicit punctuators.
        for type in TokenType.values():
            punctuator = type.punctuator()
            if punctuator != None:
                mPunctuators.put(punctuator, type)

    def hasNext(self):
        """ generated source for method hasNext """
        return True

    def next(self):
        """ generated source for method next """
        __mIndex_0 = mIndex
        mIndex += 1
        while mIndex < len(mText):
            c = mText.charAt(__mIndex_0)
            if mPunctuators.containsKey(c):
                # // Handle punctuation.
                return Token(mPunctuators.get(c), Character.toString(c))
            elif Character.isLetter(c):
                # // Handle names.
                start = mIndex - 1
                while mIndex < len(mText):
                    if not Character.isLetter(mText.charAt(mIndex)):
                        break
                    mIndex += 1
                name = mText.substring(start, mIndex)
                return Token(TokenType.NAME, name)
            else:
                pass
            # // Ignore all other characters (whitespace, etc.)
        # // Once we've reached the end of the string, just return EOF tokens. We'll
        # // just keeping returning them as many times as we're asked so that the
        # // parser's lookahead doesn't have to worry about running out of tokens.
        return Token(TokenType.EOF, "")

    def remove(self):
        """ generated source for method remove """
        raise UnsupportedOperationException()

    mPunctuators = HashMap()
    mText = None
    mIndex = 0

