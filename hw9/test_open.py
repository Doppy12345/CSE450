import solution as sol

def test_test01():
    arg1 = """Here is Nick's website: [[https://nick-ivanov.com]]!"""

    result = sol.question01(arg1)
    expected = """Here is Nick's website: <a href='https://nick-ivanov.com'>[link]</a>!"""
    assert expected == result


def test_test02():
    arg1 = """You can find more information about MSU at MSU.EDU ([[https://msu.edu/]])."""

    result = sol.question01(arg1)
    expected = """You can find more information about MSU at MSU.EDU (<a href='https://msu.edu/'>[link]</a>)."""
    assert expected == result

def test_test03():
    arg1 = """
As a student in our CSE 450 class, you have to bookmark a few links:
Class website: [[https://www.cse.msu.edu/~cse450/]]
Class D2L: [[https://d2l.msu.edu/d2l/home/1579286]]
"""

    result = sol.question01(arg1)
    expected = """
As a student in our CSE 450 class, you have to bookmark a few links:
Class website: <a href='https://www.cse.msu.edu/~cse450/'>[link]</a>
Class D2L: <a href='https://d2l.msu.edu/d2l/home/1579286'>[link]</a>
"""
    assert expected == result


def test_test04():
    arg1 = """
Our class is an inclusive community free of hate, discrimination, and marginalization.
If you feel ostracized in our class, please use the anonymous by clicking this [[https://tinyurl.com/2zwa2dkt]].
Your feedback will be treated seriously. If you want me reply, please leave your e-mail.
"""

    result = sol.question01(arg1)
    expected = """
Our class is an inclusive community free of hate, discrimination, and marginalization.
If you feel ostracized in our class, please use the anonymous by clicking this <a href='https://tinyurl.com/2zwa2dkt'>[link]</a>.
Your feedback will be treated seriously. If you want me reply, please leave your e-mail.
"""
    assert expected == result


def test_test05():
    arg1 = """Text without any links."""

    result = sol.question01(arg1)
    expected = """Text without any links."""
    assert expected == result

