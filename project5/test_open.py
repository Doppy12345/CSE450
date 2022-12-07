from solution import interpret_spartytalk

def test_test001(capsys):
    inp = """
    gogreen;
    nvar a = 10;
    nvar b = 20;
    nvar c = a / b;
    spartysays c;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""0.5
"""


def test_test002(capsys):
    inp = """
    gogreen;
    nvar a = 10;
    nvar b = a * 2.2;
    spartysays b;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""22.0
"""


def test_test003(capsys):
    inp = """
    gogreen;
    nvar a = 10;
    a = 100;
    nvar b = a * 3;
    spartysays b;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""300
"""


def test_test004(capsys):
    inp = """
    gogreen;
    nvar a = 10;
    a = 100;
    nvar b = a * 3;
    spartysays b;
    nvar c = a * b;
    spartysays c;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""300
30000
"""


def test_test004(capsys):
    inp = """
    gogreen;
    nvar a = 10;
    a = 100;
    nvar b = a * 3;
    spartysays b;
    nvar c = a * b;
    spartysays c;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""300
30000
"""


def test_test005(capsys):
    inp = """
    gogreen;
    spartysays "hello";
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""hello
"""



def test_test006(capsys):
    inp = """
    gogreen;
    nvar a = 10;
    spartysays "a=" + a;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""a=10
"""


def test_test007(capsys):
    inp = """
    gogreen;
    svar s = "world";
    spartysays "hello" + " " + s;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""hello world
"""

def test_test008(capsys):
    inp = """
    gogreen;
    nvar f = 10 + 50 * 7;
    spartysays "f: " + f;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""f: 360
"""


def test_test009(capsys):
    inp = """
    gogreen;
    nvar var1 = 1 + 1 / 2;
    spartysays var1;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""1.5
"""

def test_test010(capsys):
    inp = """
    gogreen;
    nvar var1 = 1 + 1 / 2 / 2;
    spartysays var1;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""1.25
"""


def test_test011(capsys):
    inp = """
    gogreen;
    nvar a = 3 / 2 + 3 / 2 + 0.14;
    spartysays a;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""3.14
"""

def test_test012(capsys):
    inp = """
    gogreen;
    nvar a = 3 / 2 + 3 / 2 + (0.07 + 0.07);
    spartysays a;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""3.14
"""


def test_test013(capsys):
    inp = """
    gogreen;
    nvar a = 10 - 5.5;
    spartysays a;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""4.5
"""


def test_test014(capsys):
    inp = """
    gogreen;
    nvar a = 10 - 5.5;
    a = a * 2;
    spartysays a;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""9.0
"""


def test_test015(capsys):
    inp = """
    gogreen;
    svar s = "hello" + "world" + 2;
    spartysays s;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""helloworld2
"""

def test_test016(capsys):
    inp = """
    gogreen;
    svar s = "hello" + (1 + 1);
    spartysays s;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""hello2
"""

def test_test017(capsys):
    inp = """
    gogreen;
    spartysays (4 + 3 * 2);
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""10
"""

def test_test018(capsys):
    inp = """
    gogreen;
    spartysays "1+2: " + (1 + 2);
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""1+2: 3
"""


def test_test019(capsys):
    inp = """
    gogreen;
    nvar a = 10;
    svar b = "hello" + 10;
    spartysays b;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""hello10
"""

def test_test020(capsys):
    inp = """
    gogreen;
    nvar a = 10;
    svar b = "hello" + (10*2);
    spartysays b;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""hello20
"""