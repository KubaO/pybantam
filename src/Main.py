#!/usr/bin/env python
""" generated source for module Main """
# package: com.stuffwithstuff.bantam
class Main(object):
    """ generated source for class Main """
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        # // Function call.
        test("a()", "a()")
        test("a(b)", "a(b)")
        test("a(b, c)", "a(b, c)")
        test("a(b)(c)", "a(b)(c)")
        test("a(b) + c(d)", "(a(b) + c(d))")
        test("a(b ? c : d, e + f)", "a((b ? c : d), (e + f))")
        # // Unary precedence.
        test("~!-+a", "(~(!(-(+a))))")
        test("a!!!", "(((a!)!)!)")
        # // Unary and binary predecence.
        test("-a * b", "((-a) * b)")
        test("!a + b", "((!a) + b)")
        test("~a ^ b", "((~a) ^ b)")
        test("-a!", "(-(a!))")
        test("!a!", "(!(a!))")
        # // Binary precedence.
        test("a = b + c * d ^ e - f / g", "(a = ((b + (c * (d ^ e))) - (f / g)))")
        # // Binary associativity.
        test("a = b = c", "(a = (b = c))")
        test("a + b - c", "((a + b) - c)")
        test("a * b / c", "((a * b) / c)")
        test("a ^ b ^ c", "(a ^ (b ^ c))")
        # // Conditional operator.
        test("a ? b : c ? d : e", "(a ? b : (c ? d : e))")
        test("a ? b ? c : d : e", "(a ? (b ? c : d) : e)")
        test("a + b ? c * d : e / f", "((a + b) ? (c * d) : (e / f))")
        # // Grouping.
        test("a + (b + c) + d", "((a + (b + c)) + d)")
        test("a ^ (b + c)", "(a ^ (b + c))")
        test("(!a)!", "((!a)!)")
        # // Show the results.
        if sFailed == 0:
            print("Passed all " + sPassed + " tests.")
        else:
            print("----")
            print("Failed " + sFailed + " out of " + (sFailed + sPassed) + " tests.")

    # /**
    #    * Parses the given chunk of code and verifies that it matches the expected
    #    * pretty-printed result.
    #    */
    @classmethod
    def test(cls, source, expected):
        """ generated source for method test """
        lexer = Lexer(source)
        parser = BantamParser(lexer)
        try:
            result = parser.parseExpression()
            builder = StringBuilder()
            result.print(builder)
            actual = builder.__str__()
            if expected == actual:
                sPassed += 1
            else:
                sFailed += 1
                print("[FAIL] Expected: " + expected)
                print("         Actual: " + actual)
        except ParseException as ex:
            sFailed += 1
            print("[FAIL] Expected: " + expected)
            print("          Error: " + ex.getMessage())

    sPassed = 0
    sFailed = 0


if __name__ == '__main__':
    import sys
    Main.main(sys.argv)

