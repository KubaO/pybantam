#!/usr/bin/env python
""" generated source for module TokenType """
# package: com.stuffwithstuff.bantam
class TokenType:
    """ generated source for enum TokenType """
    LEFT_PAREN = 'LEFT_PAREN'
    RIGHT_PAREN = 'RIGHT_PAREN'
    COMMA = 'COMMA'
    ASSIGN = 'ASSIGN'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    ASTERISK = 'ASTERISK'
    SLASH = 'SLASH'
    CARET = 'CARET'
    TILDE = 'TILDE'
    BANG = 'BANG'
    QUESTION = 'QUESTION'
    COLON = 'COLON'
    NAME = 'NAME'
    EOF = 'EOF'

    # /**
    #    * If the TokenType represents a punctuator (i.e. a token that can split an
    #    * identifier like '+', this will get its text.
    #    */
    def punctuator(self):
        """ generated source for method punctuator """
        if self == LEFT_PAREN:
            return '('
        elif self == RIGHT_PAREN:
            return ')'
        elif self == COMMA:
            return ','
        elif self == ASSIGN:
            return '='
        elif self == PLUS:
            return '+'
        elif self == MINUS:
            return '-'
        elif self == ASTERISK:
            return '*'
        elif self == SLASH:
            return '/'
        elif self == CARET:
            return '^'
        elif self == TILDE:
            return '~'
        elif self == BANG:
            return '!'
        elif self == QUESTION:
            return '?'
        elif self == COLON:
            return ':'
        else:
            return None

