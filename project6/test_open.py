from solution import interpret_spartytalk

def test_test001(capsys):
    inp = """
    gogreen;
        spartysays 5;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""5
"""


def test_test002(capsys):
    inp = """
    gogreen;
        if 1 == 1 gogreen;
            spartysays "tautology";
        gowhite;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""tautology
"""

def test_test003(capsys):
    inp = """
    gogreen;
        if 1 == 1
        gogreen;
            spartysays "tautology";
        gowhite;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""tautology
"""


def test_test004(capsys):
    inp = """
    gogreen;
        nvar a = 1;
        if a == 1 gogreen;
            spartysays "indeed";
        gowhite;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""indeed
"""


def test_test005(capsys):
    inp = """
    gogreen;
        nvar a = 1;
        nvar b = 1;
        if a == b gogreen;
            spartysays "two variables are equal";
        gowhite;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""two variables are equal
"""


def test_test006(capsys):
    inp = """
    gogreen;
        nvar a = 1;
        nvar b = 1;
        if a == b gogreen;
            spartysays "two variables are equal";
        gowhite; else gogreen;
            spartysays "two variables are not the same";
        gowhite;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""two variables are equal
"""


def test_test007(capsys):
    inp = """
    gogreen;
        nvar a = 1;
        nvar b = 1;
        if a == b gogreen; spartysays "two variables are equal"; gowhite;
        else gogreen; spartysays "two variables are not the same"; gowhite;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""two variables are equal
"""

def test_test008(capsys):
    inp = """
    gogreen;
        nvar a = 1;
        nvar b = 1;
        if a != b gogreen;
            spartysays "topsy";
        gowhite; else gogreen;
            spartysays "turvy";
        gowhite;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""turvy
"""


def test_test009(capsys):
    inp = """
    gogreen;
        nvar a = 1;
        nvar b = 1;
        if a > b gogreen;
            spartysays "topsy";
        gowhite; else gogreen;
            spartysays "turvy";
        gowhite;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""turvy
"""


def test_test010(capsys):
    inp = """
    gogreen;
        nvar a = 1;
        nvar b = 1;
        if a >= b gogreen;
            spartysays "topsy";
        gowhite; else gogreen;
            spartysays "turvy";
        gowhite;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""topsy
"""


def test_test011(capsys):
    inp = """
    gogreen;
        nvar a = 1;
        nvar b = 1;
        if a <= b gogreen;
            spartysays "topsy";
        gowhite; else gogreen;
            spartysays "turvy";
        gowhite;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""topsy
"""

def test_test012(capsys):
    inp = """
    gogreen;
        nvar a = 1;
        nvar b = 1;
        if a < b gogreen;
            spartysays "topsy";
        gowhite; else gogreen;
            spartysays "turvy";
        gowhite;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""turvy
"""


def test_test013(capsys):
    inp = """
    gogreen;
        nvar a = 1;
        nvar b = 1;
        if a < b + 1 gogreen;
            spartysays "topsy";
        gowhite; else gogreen;
            spartysays "turvy";
        gowhite;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""topsy
"""


def test_test014(capsys):
    inp = """
    gogreen;
        nvar a = 1;
        nvar b = 1;
        if a + 2 < b + 1 gogreen;
            spartysays "topsy";
        gowhite; else gogreen;
            spartysays "turvy";
        gowhite;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""turvy
"""


def test_test015(capsys):
    inp = """
    gogreen;
        nvar a = 1;
        nvar b = 1;
        if a == 1 and b == 1 gogreen;
            spartysays "topsy";
        gowhite; else gogreen;
            spartysays "turvy";
        gowhite;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""topsy
"""

def test_test016(capsys):
    inp = """
    gogreen;
        nvar a = 1;
        nvar b = 1;
        if a == 1 and b != 1 gogreen;
            spartysays "topsy";
        gowhite; else gogreen;
            spartysays "turvy";
        gowhite;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""turvy
"""

def test_test017(capsys):
    inp = """
    gogreen;
        nvar a = 1;
        nvar b = 1;
        if a == 1 or b != 1 gogreen;
            spartysays "topsy";
        gowhite; else gogreen;
            spartysays "turvy";
        gowhite;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""topsy
"""

def test_test018(capsys):
    inp = """
    gogreen;
        nvar a = 1;
        nvar b = 1;
        if a == 1 or b != 1 gogreen;
            spartysays "topsy";
            if 7 == 7 gogreen;
                spartysays "nest";
            gowhite;
        gowhite; else gogreen;
            spartysays "turvy";
        gowhite;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""topsy
nest
"""

def test_test019(capsys):
    inp = """
    gogreen;
        nvar a = 1;
        nvar b = 1;
        if a == 1 or b != 1 gogreen;
            spartysays "topsy";
            if 7 == 8 gogreen;
                spartysays "nest";
            gowhite; else gogreen;
                spartysays "alternest";
            gowhite;
        gowhite; else gogreen;
            spartysays "turvy";
        gowhite;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""topsy
alternest
"""

def test_test020(capsys):
    inp = """
    gogreen;
        nvar a = 1;
        nvar b = 1;
        if a == 1 or b != 1 gogreen;
            spartysays "topsy";
            if 7 == 8 gogreen;
                spartysays "nest";
            gowhite; else gogreen;
                spartysays "alternest";
                a = 6;
            gowhite;
        gowhite; else gogreen;
            spartysays "turvy";
        gowhite;

        spartysays a;
    gowhite;
    """

    interpret_spartytalk(inp)

    captured = capsys.readouterr()

    assert captured.out == r"""topsy
alternest
6
"""