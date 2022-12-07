from solution import parse_spartytalk

def test_test001(capsys):
    program = """
gogreen;
spartysays "hi";
nvar b = 7;
nvar a = 10 + 20 - 10 * (b * 255) + (a + b);
spartysays a;
spartysays a + b;
spartysays (n + k);
gowhite;
"""
    parse_spartytalk(program)

    captured = capsys.readouterr()
    assert captured.out == r"""<expression> ::= Token('STRING', '"hi"')
<statement> ::= Token('SPARTYSAYS', 'spartysays') <expression> Token('SEMICOLON', ';')
<statements> ::= <statement>
<expression> ::= Token('NUMBER', '7')
<statement> ::= Token('NVAR', 'nvar') Token('IDENTIFIER', 'b') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<expression> ::= Token('NUMBER', '10')
<expression> ::= Token('NUMBER', '20')
<expression> ::= <expression> Token('PLUS', '+') <expression>
<expression> ::= Token('NUMBER', '10')
<expression> ::= Token('IDENTIFIER', 'b')
<expression> ::= Token('NUMBER', '255')
<expression> ::= <expression> Token('MUL', '*') <expression>
<expression> ::= Token('OPEN_PARENS', '(') <expression> Token('CLOSE_PARENS', ')')
<expression> ::= <expression> Token('MUL', '*') <expression>
<expression> ::= <expression> Token('MINUS', '-') <expression>
<expression> ::= Token('IDENTIFIER', 'a')
<expression> ::= Token('IDENTIFIER', 'b')
<expression> ::= <expression> Token('PLUS', '+') <expression>
<expression> ::= Token('OPEN_PARENS', '(') <expression> Token('CLOSE_PARENS', ')')
<expression> ::= <expression> Token('PLUS', '+') <expression>
<statement> ::= Token('NVAR', 'nvar') Token('IDENTIFIER', 'a') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<expression> ::= Token('IDENTIFIER', 'a')
<statement> ::= Token('SPARTYSAYS', 'spartysays') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<expression> ::= Token('IDENTIFIER', 'a')
<expression> ::= Token('IDENTIFIER', 'b')
<expression> ::= <expression> Token('PLUS', '+') <expression>
<statement> ::= Token('SPARTYSAYS', 'spartysays') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<expression> ::= Token('IDENTIFIER', 'n')
<expression> ::= Token('IDENTIFIER', 'k')
<expression> ::= <expression> Token('PLUS', '+') <expression>
<expression> ::= Token('OPEN_PARENS', '(') <expression> Token('CLOSE_PARENS', ')')
<statement> ::= Token('SPARTYSAYS', 'spartysays') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<program> ::= Token('GOGREEN', 'gogreen') Token('SEMICOLON', ';') <statements> Token('GOWHITE', 'gowhite') Token('SEMICOLON', ';')
"""
def test_test002():
    program = """
gogreen;
gowhite;
"""
    
    try:
        parse_spartytalk(program)
        assert False
    except Exception:
        assert True



def test_test003(capsys):
    program = """
gogreen;
a = 17; b = 20;
gowhite;
"""
    parse_spartytalk(program)

    captured = capsys.readouterr()
    assert captured.out == r"""<expression> ::= Token('NUMBER', '17')
<statement> ::= Token('IDENTIFIER', 'a') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statement>
<expression> ::= Token('NUMBER', '20')
<statement> ::= Token('IDENTIFIER', 'b') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<program> ::= Token('GOGREEN', 'gogreen') Token('SEMICOLON', ';') <statements> Token('GOWHITE', 'gowhite') Token('SEMICOLON', ';')
"""


def test_test004():
    program = """
gogreen;
a = 17; b = 20;;
gowhite;
"""
    
    try:
        parse_spartytalk(program)
        assert False
    except Exception:
        assert True


def test_test005(capsys):
    program = """
gogreen;
nvar var1020 = 1020;
gowhite;
"""
    parse_spartytalk(program)

    captured = capsys.readouterr()
    assert captured.out == r"""<expression> ::= Token('NUMBER', '1020')
<statement> ::= Token('NVAR', 'nvar') Token('IDENTIFIER', 'var1020') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statement>
<program> ::= Token('GOGREEN', 'gogreen') Token('SEMICOLON', ';') <statements> Token('GOWHITE', 'gowhite') Token('SEMICOLON', ';')
"""



def test_test006(capsys):
    program = """
gogreen;
nvar car10 = 180;
spartysays car10;
gowhite;
"""
    parse_spartytalk(program)

    captured = capsys.readouterr()
    assert captured.out == r"""<expression> ::= Token('NUMBER', '180')
<statement> ::= Token('NVAR', 'nvar') Token('IDENTIFIER', 'car10') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statement>
<expression> ::= Token('IDENTIFIER', 'car10')
<statement> ::= Token('SPARTYSAYS', 'spartysays') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<program> ::= Token('GOGREEN', 'gogreen') Token('SEMICOLON', ';') <statements> Token('GOWHITE', 'gowhite') Token('SEMICOLON', ';')
"""


def test_test007(capsys):
    program = """
gogreen;
nvar car88 = 100.0;
spartysays car11 * 35;
gowhite;
"""
    parse_spartytalk(program)

    captured = capsys.readouterr()
    assert captured.out == r"""<expression> ::= Token('NUMBER', '100.0')
<statement> ::= Token('NVAR', 'nvar') Token('IDENTIFIER', 'car88') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statement>
<expression> ::= Token('IDENTIFIER', 'car11')
<expression> ::= Token('NUMBER', '35')
<expression> ::= <expression> Token('MUL', '*') <expression>
<statement> ::= Token('SPARTYSAYS', 'spartysays') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<program> ::= Token('GOGREEN', 'gogreen') Token('SEMICOLON', ';') <statements> Token('GOWHITE', 'gowhite') Token('SEMICOLON', ';')
"""


def test_test008(capsys):
    program = """
gogreen;
nvar variableX = (100.25 - 7.1) * 2;
spartysays car11 / 35.3 - 1;
gowhite;
"""
    parse_spartytalk(program)

    captured = capsys.readouterr()
    assert captured.out == r"""<expression> ::= Token('NUMBER', '100.25')
<expression> ::= Token('NUMBER', '7.1')
<expression> ::= <expression> Token('MINUS', '-') <expression>
<expression> ::= Token('OPEN_PARENS', '(') <expression> Token('CLOSE_PARENS', ')')
<expression> ::= Token('NUMBER', '2')
<expression> ::= <expression> Token('MUL', '*') <expression>
<statement> ::= Token('NVAR', 'nvar') Token('IDENTIFIER', 'variableX') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statement>
<expression> ::= Token('IDENTIFIER', 'car11')
<expression> ::= Token('NUMBER', '35.3')
<expression> ::= <expression> Token('DIV', '/') <expression>
<expression> ::= Token('NUMBER', '1')
<expression> ::= <expression> Token('MINUS', '-') <expression>
<statement> ::= Token('SPARTYSAYS', 'spartysays') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<program> ::= Token('GOGREEN', 'gogreen') Token('SEMICOLON', ';') <statements> Token('GOWHITE', 'gowhite') Token('SEMICOLON', ';')
"""



def test_test009(capsys):
    program = """
gogreen;
svar s = "hello";
spartysays s;
gowhite;
"""
    parse_spartytalk(program)

    captured = capsys.readouterr()
    assert captured.out == r"""<expression> ::= Token('STRING', '"hello"')
<statement> ::= Token('SVAR', 'svar') Token('IDENTIFIER', 's') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statement>
<expression> ::= Token('IDENTIFIER', 's')
<statement> ::= Token('SPARTYSAYS', 'spartysays') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<program> ::= Token('GOGREEN', 'gogreen') Token('SEMICOLON', ';') <statements> Token('GOWHITE', 'gowhite') Token('SEMICOLON', ';')
"""


def test_test010(capsys):
    program = """
gogreen;
svar s = "hello, ";
svar q = "world";
spartysays s + q;
gowhite;
"""
    parse_spartytalk(program)

    captured = capsys.readouterr()
    assert captured.out == r"""<expression> ::= Token('STRING', '"hello, "')
<statement> ::= Token('SVAR', 'svar') Token('IDENTIFIER', 's') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statement>
<expression> ::= Token('STRING', '"world"')
<statement> ::= Token('SVAR', 'svar') Token('IDENTIFIER', 'q') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<expression> ::= Token('IDENTIFIER', 's')
<expression> ::= Token('IDENTIFIER', 'q')
<expression> ::= <expression> Token('PLUS', '+') <expression>
<statement> ::= Token('SPARTYSAYS', 'spartysays') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<program> ::= Token('GOGREEN', 'gogreen') Token('SEMICOLON', ';') <statements> Token('GOWHITE', 'gowhite') Token('SEMICOLON', ';')
"""



def test_test011(capsys):
    program = """
gogreen;
a = 10;
a = "hello";
a = a + a;
gowhite;
"""
    parse_spartytalk(program)

    captured = capsys.readouterr()
    assert captured.out == r"""<expression> ::= Token('NUMBER', '10')
<statement> ::= Token('IDENTIFIER', 'a') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statement>
<expression> ::= Token('STRING', '"hello"')
<statement> ::= Token('IDENTIFIER', 'a') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<expression> ::= Token('IDENTIFIER', 'a')
<expression> ::= Token('IDENTIFIER', 'a')
<expression> ::= <expression> Token('PLUS', '+') <expression>
<statement> ::= Token('IDENTIFIER', 'a') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<program> ::= Token('GOGREEN', 'gogreen') Token('SEMICOLON', ';') <statements> Token('GOWHITE', 'gowhite') Token('SEMICOLON', ';')
"""


def test_test012(capsys):
    program = """
gogreen;
a = 17.5;
b = "relatively long string";
c = a + b;
spartysays (((c + a) * b * 10.777) / "world") * 20.55;
gowhite;
"""
    parse_spartytalk(program)

    captured = capsys.readouterr()
    assert captured.out == r"""<expression> ::= Token('NUMBER', '17.5')
<statement> ::= Token('IDENTIFIER', 'a') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statement>
<expression> ::= Token('STRING', '"relatively long string"')
<statement> ::= Token('IDENTIFIER', 'b') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<expression> ::= Token('IDENTIFIER', 'a')
<expression> ::= Token('IDENTIFIER', 'b')
<expression> ::= <expression> Token('PLUS', '+') <expression>
<statement> ::= Token('IDENTIFIER', 'c') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<expression> ::= Token('IDENTIFIER', 'c')
<expression> ::= Token('IDENTIFIER', 'a')
<expression> ::= <expression> Token('PLUS', '+') <expression>
<expression> ::= Token('OPEN_PARENS', '(') <expression> Token('CLOSE_PARENS', ')')
<expression> ::= Token('IDENTIFIER', 'b')
<expression> ::= <expression> Token('MUL', '*') <expression>
<expression> ::= Token('NUMBER', '10.777')
<expression> ::= <expression> Token('MUL', '*') <expression>
<expression> ::= Token('OPEN_PARENS', '(') <expression> Token('CLOSE_PARENS', ')')
<expression> ::= Token('STRING', '"world"')
<expression> ::= <expression> Token('DIV', '/') <expression>
<expression> ::= Token('OPEN_PARENS', '(') <expression> Token('CLOSE_PARENS', ')')
<expression> ::= Token('NUMBER', '20.55')
<expression> ::= <expression> Token('MUL', '*') <expression>
<statement> ::= Token('SPARTYSAYS', 'spartysays') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<program> ::= Token('GOGREEN', 'gogreen') Token('SEMICOLON', ';') <statements> Token('GOWHITE', 'gowhite') Token('SEMICOLON', ';')
"""


def test_test013(capsys):
    program = """
gogreen;
a = -27.5;
spartysays a;
gowhite;
"""
    parse_spartytalk(program)

    captured = capsys.readouterr()
    assert captured.out == r"""<expression> ::= Token('NUMBER', '-27.5')
<statement> ::= Token('IDENTIFIER', 'a') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statement>
<expression> ::= Token('IDENTIFIER', 'a')
<statement> ::= Token('SPARTYSAYS', 'spartysays') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<program> ::= Token('GOGREEN', 'gogreen') Token('SEMICOLON', ';') <statements> Token('GOWHITE', 'gowhite') Token('SEMICOLON', ';')
"""



def test_test014(capsys):
    program = """
gogreen;
a = 7 - -27.6;
spartysays a;
gowhite;
"""
    parse_spartytalk(program)

    captured = capsys.readouterr()
    assert captured.out == r"""<expression> ::= Token('NUMBER', '7')
<expression> ::= Token('NUMBER', '-27.6')
<expression> ::= <expression> Token('MINUS', '-') <expression>
<statement> ::= Token('IDENTIFIER', 'a') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statement>
<expression> ::= Token('IDENTIFIER', 'a')
<statement> ::= Token('SPARTYSAYS', 'spartysays') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<program> ::= Token('GOGREEN', 'gogreen') Token('SEMICOLON', ';') <statements> Token('GOWHITE', 'gowhite') Token('SEMICOLON', ';')
"""


def test_test015(capsys):
    program = """
gogreen;
a = +8.2 + +3.6;
spartysays a;
gowhite;
"""
    parse_spartytalk(program)

    captured = capsys.readouterr()
    assert captured.out == r"""<expression> ::= Token('NUMBER', '+8.2')
<expression> ::= Token('NUMBER', '+3.6')
<expression> ::= <expression> Token('PLUS', '+') <expression>
<statement> ::= Token('IDENTIFIER', 'a') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statement>
<expression> ::= Token('IDENTIFIER', 'a')
<statement> ::= Token('SPARTYSAYS', 'spartysays') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<program> ::= Token('GOGREEN', 'gogreen') Token('SEMICOLON', ';') <statements> Token('GOWHITE', 'gowhite') Token('SEMICOLON', ';')
"""


def test_test016(capsys):
    program = """
gogreen;
c = 0 - (50 / 0) * (50 + 5.777) - ("hello" / "world");
spartysays b;
gowhite;
"""
    parse_spartytalk(program)

    captured = capsys.readouterr()
    assert captured.out == r"""<expression> ::= Token('NUMBER', '0')
<expression> ::= Token('NUMBER', '50')
<expression> ::= Token('NUMBER', '0')
<expression> ::= <expression> Token('DIV', '/') <expression>
<expression> ::= Token('OPEN_PARENS', '(') <expression> Token('CLOSE_PARENS', ')')
<expression> ::= Token('NUMBER', '50')
<expression> ::= Token('NUMBER', '5.777')
<expression> ::= <expression> Token('PLUS', '+') <expression>
<expression> ::= Token('OPEN_PARENS', '(') <expression> Token('CLOSE_PARENS', ')')
<expression> ::= <expression> Token('MUL', '*') <expression>
<expression> ::= <expression> Token('MINUS', '-') <expression>
<expression> ::= Token('STRING', '"hello"')
<expression> ::= Token('STRING', '"world"')
<expression> ::= <expression> Token('DIV', '/') <expression>
<expression> ::= Token('OPEN_PARENS', '(') <expression> Token('CLOSE_PARENS', ')')
<expression> ::= <expression> Token('MINUS', '-') <expression>
<statement> ::= Token('IDENTIFIER', 'c') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statement>
<expression> ::= Token('IDENTIFIER', 'b')
<statement> ::= Token('SPARTYSAYS', 'spartysays') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<program> ::= Token('GOGREEN', 'gogreen') Token('SEMICOLON', ';') <statements> Token('GOWHITE', 'gowhite') Token('SEMICOLON', ';')
"""

def test_test017(capsys):
    program = """
gogreen;
a = hello;
b = world;
spartysays a + b;
gowhite;
"""
    parse_spartytalk(program)

    captured = capsys.readouterr()
    assert captured.out == r"""<expression> ::= Token('IDENTIFIER', 'hello')
<statement> ::= Token('IDENTIFIER', 'a') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statement>
<expression> ::= Token('IDENTIFIER', 'world')
<statement> ::= Token('IDENTIFIER', 'b') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<expression> ::= Token('IDENTIFIER', 'a')
<expression> ::= Token('IDENTIFIER', 'b')
<expression> ::= <expression> Token('PLUS', '+') <expression>
<statement> ::= Token('SPARTYSAYS', 'spartysays') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<program> ::= Token('GOGREEN', 'gogreen') Token('SEMICOLON', ';') <statements> Token('GOWHITE', 'gowhite') Token('SEMICOLON', ';')
"""

def test_test018():
    program = """
gogreen;
a = ((10+2);
gowhite;
"""
    
    try:
        parse_spartytalk(program)
        assert False
    except Exception:
        assert True



def test_test019(capsys):
    program = """
gogreen;
nvar a = 777.5; b = 10; a = ("hello" + "world") - "goodbye";
spartysays Nvar;
gowhite;
"""
    parse_spartytalk(program)

    captured = capsys.readouterr()
    assert captured.out == r"""<expression> ::= Token('NUMBER', '777.5')
<statement> ::= Token('NVAR', 'nvar') Token('IDENTIFIER', 'a') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statement>
<expression> ::= Token('NUMBER', '10')
<statement> ::= Token('IDENTIFIER', 'b') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<expression> ::= Token('STRING', '"hello"')
<expression> ::= Token('STRING', '"world"')
<expression> ::= <expression> Token('PLUS', '+') <expression>
<expression> ::= Token('OPEN_PARENS', '(') <expression> Token('CLOSE_PARENS', ')')
<expression> ::= Token('STRING', '"goodbye"')
<expression> ::= <expression> Token('MINUS', '-') <expression>
<statement> ::= Token('IDENTIFIER', 'a') Token('ASSIGNMENT', '=') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<expression> ::= Token('IDENTIFIER', 'Nvar')
<statement> ::= Token('SPARTYSAYS', 'spartysays') <expression> Token('SEMICOLON', ';')
<statements> ::= <statements> <statement>
<program> ::= Token('GOGREEN', 'gogreen') Token('SEMICOLON', ';') <statements> Token('GOWHITE', 'gowhite') Token('SEMICOLON', ';')
"""

def test_test020(capsys):
    program = """
gogreen;
spartysays -10.55 / "hello";
gowhite;
"""
    parse_spartytalk(program)

    captured = capsys.readouterr()
    assert captured.out == r"""<expression> ::= Token('NUMBER', '-10.55')
<expression> ::= Token('STRING', '"hello"')
<expression> ::= <expression> Token('DIV', '/') <expression>
<statement> ::= Token('SPARTYSAYS', 'spartysays') <expression> Token('SEMICOLON', ';')
<statements> ::= <statement>
<program> ::= Token('GOGREEN', 'gogreen') Token('SEMICOLON', ';') <statements> Token('GOWHITE', 'gowhite') Token('SEMICOLON', ';')
"""




