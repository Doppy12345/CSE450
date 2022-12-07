from solution import lex_spartytalk
from rply import Token

def test_test001():
    program = """
    gogreen;
    nvar a = -10.5;
    svar b = "hello\n";
    svar c = "world";
    svar d = b + c + c;
    nvar e = a * 2;
    nvar f = 3.5 / a;
    f = f / 7.5 * 3;
    spartysays "hi " + e;
    gowhite;
    """

    expected = [
    Token('GOGREEN', 'gogreen'),
    Token('SEMICOLON', ';'),
    Token('NVAR', 'nvar'),
    Token('IDENTIFIER', 'a'),
    Token('ASSIGNMENT', '='),
    Token('NUMBER', '-10.5'),
    Token('SEMICOLON', ';'),
    Token('SVAR', 'svar'),
    Token('IDENTIFIER', 'b'),
    Token('ASSIGNMENT', '='),
    Token('STRING', '"hello\n"'),
    Token('SEMICOLON', ';'),
    Token('SVAR', 'svar'),
    Token('IDENTIFIER', 'c'),
    Token('ASSIGNMENT', '='),
    Token('STRING', '"world"'),
    Token('SEMICOLON', ';'),
    Token('SVAR', 'svar'),
    Token('IDENTIFIER', 'd'),
    Token('ASSIGNMENT', '='),
    Token('IDENTIFIER', 'b'),
    Token('PLUS', '+'),
    Token('IDENTIFIER', 'c'),
    Token('PLUS', '+'),
    Token('IDENTIFIER', 'c'),
    Token('SEMICOLON', ';'),
    Token('NVAR', 'nvar'),
    Token('IDENTIFIER', 'e'),
    Token('ASSIGNMENT', '='),
    Token('IDENTIFIER', 'a'),
    Token('MUL', '*'),
    Token('NUMBER', '2'),
    Token('SEMICOLON', ';'),
    Token('NVAR', 'nvar'),
    Token('IDENTIFIER', 'f'),
    Token('ASSIGNMENT', '='),
    Token('NUMBER', '3.5'),
    Token('DIV', '/'),
    Token('IDENTIFIER', 'a'),
    Token('SEMICOLON', ';'),
    Token('IDENTIFIER', 'f'),
    Token('ASSIGNMENT', '='),
    Token('IDENTIFIER', 'f'),
    Token('DIV', '/'),
    Token('NUMBER', '7.5'),
    Token('MUL', '*'),
    Token('NUMBER', '3'),
    Token('SEMICOLON', ';'),
    Token('SPARTYSAYS', 'spartysays'),
    Token('STRING', '"hi "'),
    Token('PLUS', '+'),
    Token('IDENTIFIER', 'e'),
    Token('SEMICOLON', ';'),
    Token('GOWHITE', 'gowhite'),
    Token('SEMICOLON', ';')
    ]

    tokens, l, c = lex_spartytalk(program)
    assert tokens != None
    assert tokens == expected


def test_test002():
    program = """"""

    expected = []
    tokens, l, c = lex_spartytalk(program)

    assert l == -1
    assert c == -1
    assert tokens == expected



def test_test003():
    program = """gogreen; gowhite;"""

    expected = [
        Token('GOGREEN', 'gogreen'),
        Token('SEMICOLON', ';'),
        Token('GOWHITE', 'gowhite'),
        Token('SEMICOLON', ';')
    ]

    tokens, l, c = lex_spartytalk(program)
    assert tokens != None
    assert tokens == expected



def test_test004():
    program = """gogreen;
    nvar a1 = 10.1;
    gowhite;"""

    expected = [
        Token('GOGREEN', 'gogreen'), 
        Token('SEMICOLON', ';'),
        Token('NVAR', 'nvar'),
        Token('IDENTIFIER', 'a1'),
        Token('ASSIGNMENT', '='),
        Token('NUMBER', '10.1'),
        Token('SEMICOLON', ';'),
        Token('GOWHITE', 'gowhite'),
        Token('SEMICOLON', ';')
    ]

    tokens, l, c = lex_spartytalk(program)
    assert tokens != None
    assert tokens == expected




def test_test005():
    program = """gogreen;
    nvar a = .1;
    gowhite;"""

    expected = None

    tokens, l, c = lex_spartytalk(program)
    assert tokens == expected
    assert l == 2


def test_test006():
    program = """gogreen;
    svar ss1s = "hello";
    gowhite;"""

    expected = [
        Token('GOGREEN', 'gogreen'),
        Token('SEMICOLON', ';'),
        Token('SVAR', 'svar'),
        Token('IDENTIFIER', 'ss1s'),
        Token('ASSIGNMENT', '='),
        Token('STRING', '"hello"'),
        Token('SEMICOLON', ';'),
        Token('GOWHITE', 'gowhite'),
        Token('SEMICOLON', ';')
        ]

    tokens, l, c = lex_spartytalk(program)
    assert tokens != None
    assert tokens == expected



def test_test007():
    program = """gogreen;
    svar Ab5 = "hello";
    gowhite;"""

    expected = [
        Token('GOGREEN', 'gogreen'),
        Token('SEMICOLON', ';'),
        Token('SVAR', 'svar'),
        Token('IDENTIFIER', 'Ab5'),
        Token('ASSIGNMENT', '='),
        Token('STRING', '"hello"'),
        Token('SEMICOLON', ';'),
        Token('GOWHITE', 'gowhite'),
        Token('SEMICOLON', ';')
        ]

    tokens, l, c = lex_spartytalk(program)
    assert tokens != None
    assert tokens == expected


def test_test008():
    program = """gogreen;
    svar s = 'hello';
    gowhite;
    """

    expected = None

    tokens, l, c = lex_spartytalk(program)
    assert tokens == expected
    assert l == 2



def test_test009():
    program = """gogreen;
    svar 1s = "hello";
    gowhite;
    """

    expected = [
        Token('GOGREEN', 'gogreen'),
        Token('SEMICOLON', ';'),
        Token('SVAR', 'svar'),
        Token('NUMBER', '1'),
        Token('IDENTIFIER', 's'),
        Token('ASSIGNMENT', '='),
        Token('STRING', '"hello"'),
        Token('SEMICOLON', ';'),
        Token('GOWHITE', 'gowhite'),
        Token('SEMICOLON', ';')
        ]

    tokens, l, c = lex_spartytalk(program)
    assert tokens != None
    assert tokens == expected


def test_test010():
    program = """gogreen;
    nvar a = 10;
    a = a % 2;
    gowhite;
    """

    expected = None

    tokens, l, c = lex_spartytalk(program)
    assert tokens == expected
    assert l == 3


def test_test011():
    program = """gogreen;
    nvar a = 10;
    a = 3.5e-15;
    gowhite;
    """

    expected = [
        Token('GOGREEN', 'gogreen'),
        Token('SEMICOLON', ';'),
        Token('NVAR', 'nvar'),
        Token('IDENTIFIER', 'a'),
        Token('ASSIGNMENT', '='),
        Token('NUMBER', '10'),
        Token('SEMICOLON', ';'),
        Token('IDENTIFIER', 'a'),
        Token('ASSIGNMENT', '='),
        Token('NUMBER', '3.5'),
        Token('IDENTIFIER', 'e'),
        Token('NUMBER', '-15'),
        Token('SEMICOLON', ';'),
        Token('GOWHITE', 'gowhite'),
        Token('SEMICOLON', ';')
        ]

    tokens, l, c = lex_spartytalk(program)
    assert tokens != None
    assert tokens == expected

def test_test012():
    program = """
    nvar a = -3.5;
    spartysays a;
    gowhite;
    """

    expected = [
        Token('NVAR', 'nvar'),
        Token('IDENTIFIER', 'a'),
        Token('ASSIGNMENT', '='),
        Token('NUMBER', '-3.5'),
        Token('SEMICOLON', ';'),
        Token('SPARTYSAYS', 'spartysays'),
        Token('IDENTIFIER', 'a'),
        Token('SEMICOLON', ';'),
        Token('GOWHITE', 'gowhite'),
        Token('SEMICOLON', ';')
        ]

    tokens, l, c = lex_spartytalk(program)
    assert tokens != None
    assert tokens == expected


def test_test013():
    program = """
    gogreen;
    foo("hello");
    gowhite;
    """

    expected = [
        Token('GOGREEN', 'gogreen'),
        Token('SEMICOLON', ';'),
        Token('IDENTIFIER', 'foo'),
        Token('OPEN_PARENS', '('),
        Token('STRING', '"hello"'),
        Token('CLOSE_PARENS', ')'),
        Token('SEMICOLON', ';'),
        Token('GOWHITE', 'gowhite'),
        Token('SEMICOLON', ';')
        ]

    tokens, l, c = lex_spartytalk(program)
    assert tokens != None
    assert tokens == expected


def test_test014():
    program = """
    gogreen;
    foo(("hello");
    gowhite;
    """

    expected = [
        Token('GOGREEN', 'gogreen'),
        Token('SEMICOLON', ';'),
        Token('IDENTIFIER', 'foo'),
        Token('OPEN_PARENS', '('),
        Token('OPEN_PARENS', '('),
        Token('STRING', '"hello"'),
        Token('CLOSE_PARENS', ')'),
        Token('SEMICOLON', ';'),
        Token('GOWHITE', 'gowhite'),
        Token('SEMICOLON', ';')
        ]

    tokens, l, c = lex_spartytalk(program)
    assert tokens != None
    assert tokens == expected


def test_test015():
    program = """
    gogreen;
    varn my_variable = 14;
    gowhite;
    """

    expected = None

    tokens, l, c = lex_spartytalk(program)
    assert tokens == expected
    assert l == 3


def test_test016():
    program = """
    gogreen;
    varn a := 70.5;
    gowhite;
    """

    expected = None

    tokens, l, c = lex_spartytalk(program)
    assert tokens == expected
    assert l == 3


def test_test017():
    program = """
    gogreen;
    varn a = 70.5;
    a += 10.2;
    gowhite;
    """

    expected = [
        Token('GOGREEN', 'gogreen'),
        Token('SEMICOLON', ';'),
        Token('IDENTIFIER', 'varn'),
        Token('IDENTIFIER', 'a'),
        Token('ASSIGNMENT', '='),
        Token('NUMBER', '70.5'),
        Token('SEMICOLON', ';'),
        Token('IDENTIFIER', 'a'),
        Token('PLUS', '+'),
        Token('ASSIGNMENT', '='),
        Token('NUMBER', '10.2'),
        Token('SEMICOLON', ';'),
        Token('GOWHITE', 'gowhite'),
        Token('SEMICOLON', ';')
        ]

    tokens, l, c = lex_spartytalk(program)
    assert tokens != None
    assert tokens == expected

def test_test018():
    program = """
    gogreen;
    varn a = 70.5;
    a = - 10.2;
    gowhite;
    """

    expected = [
        Token('GOGREEN', 'gogreen'),
        Token('SEMICOLON', ';'),
        Token('IDENTIFIER', 'varn'),
        Token('IDENTIFIER', 'a'),
        Token('ASSIGNMENT', '='),
        Token('NUMBER', '70.5'),
        Token('SEMICOLON', ';'),
        Token('IDENTIFIER', 'a'),
        Token('ASSIGNMENT', '='),
        Token('MINUS', '-'),
        Token('NUMBER', '10.2'),
        Token('SEMICOLON', ';'),
        Token('GOWHITE', 'gowhite'),
        Token('SEMICOLON', ';')
        ]

    tokens, l, c = lex_spartytalk(program)
    assert tokens != None
    assert tokens == expected


def test_test019():
    program = """
    gogreen;
    varn a = 70.5;
    a = -10.2;
    gowhite;
    """

    expected = [
        Token('GOGREEN', 'gogreen'),
        Token('SEMICOLON', ';'),
        Token('IDENTIFIER', 'varn'),
        Token('IDENTIFIER', 'a'),
        Token('ASSIGNMENT', '='),
        Token('NUMBER', '70.5'),
        Token('SEMICOLON', ';'),
        Token('IDENTIFIER', 'a'),
        Token('ASSIGNMENT', '='),
        Token('NUMBER', '-10.2'),
        Token('SEMICOLON', ';'),
        Token('GOWHITE', 'gowhite'),
        Token('SEMICOLON', ';')
        ]

    tokens, l, c = lex_spartytalk(program)
    assert tokens != None
    assert tokens == expected



def test_test020():
    program = """
    gogreen;
    vars s = "'Test' he said.\n\t";
    gowhite;
    """

    expected = [
        Token('GOGREEN', 'gogreen'),
        Token('SEMICOLON', ';'),
        Token('IDENTIFIER', 'vars'),
        Token('IDENTIFIER', 's'),
        Token('ASSIGNMENT', '='),
        Token('STRING', '"\'Test\' he said.\n\t"'),
        Token('SEMICOLON', ';'),
        Token('GOWHITE', 'gowhite'),
        Token('SEMICOLON', ';')
        ]

    tokens, l, c = lex_spartytalk(program)
    assert tokens != None
    assert tokens == expected

def run_tests():

    test_test002()

run_tests()