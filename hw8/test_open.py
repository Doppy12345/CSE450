import solution as sol

def test_test01():
    arg1 = """Mary ((had)) a little lamb"""

    result = sol.question01(arg1)
    expected = """Mary HAD a little lamb"""
    assert expected == result


def test_test02():
    arg1 = """Mary ((had)) a little ((lamb))"""

    result = sol.question01(arg1)
    expected = """Mary HAD a little LAMB"""
    assert expected == result

def test_test03():
    arg1 = """
Mary ((had)) a little ((lamb)),
Its fleece was white as ((snow)),
And everywhere that ((Mary)) went,
The ((lamb)) was sure to go.
"""

    result = sol.question01(arg1)
    expected = """
Mary HAD a little LAMB,
Its fleece was white as SNOW,
And everywhere that MARY went,
The LAMB was sure to go.
"""
    assert expected == result


def test_test04():
    arg1 = """
((5 little monkeys)) jumping on the bed:
One fell off and bumped his head.
"""

    result = sol.question01(arg1)
    expected = """
5 LITTLE MONKEYS jumping on the bed:
One fell off and bumped his head.
"""
    assert expected == result


def test_test05():
    arg1 = """(())"""

    result = sol.question01(arg1)
    expected = """"""
    assert expected == result

