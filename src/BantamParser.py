#!/usr/bin/env python
""" generated source for module BantamParser """
# package: com.stuffwithstuff.bantam
# 
#  * Extends the generic Parser class with support for parsing the actual Bantam
#  * grammar.
#  */
class BantamParser(Parser):
    """ generated source for class BantamParser """
    def __init__(self, lexer):
        """ generated source for method __init__ """
        super(BantamParser, self).__init__(lexer)
        # // Register all of the parselets for the grammar.
        # // Register the ones that need special parselets.
        register(TokenType.NAME, NameParselet())
        register(TokenType.ASSIGN, AssignParselet())
        register(TokenType.QUESTION, ConditionalParselet())
        register(TokenType.LEFT_PAREN, GroupParselet())
        register(TokenType.LEFT_PAREN, CallParselet())
        # // Register the simple operator parselets.
        prefix(TokenType.PLUS, Precedence.PREFIX)
        prefix(TokenType.MINUS, Precedence.PREFIX)
        prefix(TokenType.TILDE, Precedence.PREFIX)
        prefix(TokenType.BANG, Precedence.PREFIX)
        # // For kicks, we'll make "!" both prefix and postfix, kind of like ++.
        postfix(TokenType.BANG, Precedence.POSTFIX)
        infixLeft(TokenType.PLUS, Precedence.SUM)
        infixLeft(TokenType.MINUS, Precedence.SUM)
        infixLeft(TokenType.ASTERISK, Precedence.PRODUCT)
        infixLeft(TokenType.SLASH, Precedence.PRODUCT)
        infixRight(TokenType.CARET, Precedence.EXPONENT)

    # /**
    #    * Registers a postfix unary operator parselet for the given token and
    #    * precedence.
    #    */
    def postfix(self, token, precedence):
        """ generated source for method postfix """
        register(token, PostfixOperatorParselet(precedence))

    # /**
    #    * Registers a prefix unary operator parselet for the given token and
    #    * precedence.
    #    */
    def prefix(self, token, precedence):
        """ generated source for method prefix """
        register(token, PrefixOperatorParselet(precedence))

    # /**
    #    * Registers a left-associative binary operator parselet for the given token
    #    * and precedence.
    #    */
    def infixLeft(self, token, precedence):
        """ generated source for method infixLeft """
        register(token, BinaryOperatorParselet(precedence, False))

    # /**
    #    * Registers a right-associative binary operator parselet for the given token
    #    * and precedence.
    #    */
    def infixRight(self, token, precedence):
        """ generated source for method infixRight """
        register(token, BinaryOperatorParselet(precedence, True))

