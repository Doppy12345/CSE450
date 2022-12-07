import solution as sol

def test_test01():
    arg1 = ""
    try:
        result = sol.question01(arg1)
        assert True
    except Exception:
        assert False

    arg1 = ""
    try:
        result = sol.question01(arg1)
        assert True
    except Exception:
        assert False

    arg1 = "."
    try:
        result = sol.question01(arg1)
        assert False
    except Exception:
        assert True

    arg1 = "!"
    try:
        result = sol.question01(arg1)
        assert False
    except Exception:
        assert True


def test_test02():
    arg1 = "()"
    try:
        result = sol.question01(arg1)
        assert True
    except Exception:
        assert False

    arg1 = "(())"
    try:
        result = sol.question01(arg1)
        assert True
    except Exception:
        assert False

    arg1 = "("
    try:
        result = sol.question01(arg1)
        assert False
    except Exception:
        assert True

    arg1 = "())"
    try:
        result = sol.question01(arg1)
        assert False
    except Exception:
        assert True

    arg1 = "(()"
    try:
        result = sol.question01(arg1)
        assert False
    except Exception:
        assert True


def test_test03():
    arg1 = "<>(){}"
    try:
        result = sol.question01(arg1)
        assert True
    except Exception:
        assert False

    arg1 = "<<>><>"
    try:
        result = sol.question01(arg1)
        assert True
    except Exception:
        assert False

    arg1 = "<)"
    try:
        result = sol.question01(arg1)
        assert False
    except Exception:
        assert True

    arg1 = "<(>)"
    try:
        result = sol.question01(arg1)
        assert False
    except Exception:
        assert True

    arg1 = "<()>{{}()}"
    try:
        result = sol.question01(arg1)
        assert True
    except Exception:
        assert False

    arg1 = "?"
    try:
        result = sol.question01(arg1)
        assert False
    except Exception:
        assert True

    arg1 = "()()"
    try:
        result = sol.question01(arg1)
        assert True
    except Exception:
        assert False

    arg1 = "(())()"
    try:
        result = sol.question01(arg1)
        assert True
    except Exception:
        assert False


    arg1 = "())("
    try:
        result = sol.question01(arg1)
        assert False
    except Exception:
        assert True

    arg1 = ")("
    try:
        result = sol.question01(arg1)
        assert False
    except Exception:
        assert True


    arg1 = "(())(())()(())"
    try:
        result = sol.question01(arg1)
        assert True
    except Exception:
        assert False


    arg1 = "( )"
    try:
        result = sol.question01(arg1)
        assert False
    except Exception:
        assert True

def test_test04():
    arg1 = "()()"
    try:
        result = sol.question01(arg1)
        assert True
    except Exception:
        assert False

    arg1 = "(())()"
    try:
        result = sol.question01(arg1)
        assert True
    except Exception:
        assert False

    arg1 = "())("
    try:
        result = sol.question01(arg1)
        assert False
    except Exception:
        assert True

    arg1 = ")("
    try:
        result = sol.question01(arg1)
        assert False
    except Exception:
        assert True

    arg1 = "(())(())()(())"
    try:
        result = sol.question01(arg1)
        assert True
    except Exception:
        assert False

    arg1 = "(9)"
    try:
        result = sol.question01(arg1)
        assert False
    except Exception:
        assert True

        arg1 = ""
    try:
        result = sol.question01(arg1)
        assert True
    except Exception:
        assert False

    arg1 = "(())(())"
    try:
        result = sol.question01(arg1)
        assert True
    except Exception:
        assert False

def test_test05():
    arg1 = "<>(){}"
    try:
        result = sol.question01(arg1)
        assert True
    except Exception:
        assert False

    arg1 = "<<>><>"
    try:
        result = sol.question01(arg1)
        assert True
    except Exception:
        assert False

    arg1 = "<)"
    try:
        result = sol.question01(arg1)
        assert False
    except Exception:
        assert True

    arg1 = "<(>)"
    try:
        result = sol.question01(arg1)
        assert False
    except Exception:
        assert True

    arg1 = "<()>{{}()}"
    try:
        result = sol.question01(arg1)
        assert True
    except Exception:
        assert False

    arg1 = "()()<><>{}{}"
    try:
        result = sol.question01(arg1)
        assert True
    except Exception:
        assert False

    arg1 = "?"
    try:
        result = sol.question01(arg1)
        assert False
    except Exception:
        assert True

test_test01()