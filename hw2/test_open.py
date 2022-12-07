import solution as sol

def test_test01():
    from rply import Token
    text = ""
    result = sol.question01(text)
    expected = [Token('UPPER', 'C'), Token('UPPER', 'A'), Token('UPPER', 'T')]
    assert expected == result
    text = "My name"
    result = sol.question01(text)
    expected = [Token('UPPER', 'M'),
    Token('LOWER', 'y'),
    Token('OTHER', ' '),
    Token('LOWER', 'n'),
    Token('LOWER', 'a'),
    Token('LOWER', 'm'),
    Token('LOWER', 'e')]
    assert expected == result

def test_test02():
    from rply import Token
    text = """a\nb"""
    result = sol.question01(text)
    expected = [Token('LOWER', 'a'), Token('OTHER', '\n'), Token('LOWER', 'b')]
    assert expected == result
    text = "1\n        a\n        B"
    result = sol.question01(text)
    expected = [Token('OTHER', '1'),
    Token('OTHER', '\n'),
    Token('OTHER', ' '),
    Token('OTHER', ' '),
    Token('OTHER', ' '),
    Token('OTHER', ' '),
    Token('OTHER', ' '),
    Token('OTHER', ' '),
    Token('OTHER', ' '),
    Token('OTHER', ' '),
    Token('LOWER', 'a'),
    Token('OTHER', '\n'),
    Token('OTHER', ' '),
    Token('OTHER', ' '),
    Token('OTHER', ' '),
    Token('OTHER', ' '),
    Token('OTHER', ' '),
    Token('OTHER', ' '),
    Token('OTHER', ' '),
    Token('OTHER', ' '),
    Token('UPPER', 'B')]
    assert expected == result

def test_test03():
    from rply import Token
    text = """gh34GH\n G s"""
    result = sol.question01(text)
    expected = [Token('LOWER', 'g'),
    Token('LOWER', 'h'),
    Token('OTHER', '3'),
    Token('OTHER', '4'),
    Token('UPPER', 'G'),
    Token('UPPER', 'H'),
    Token('OTHER', '\n'),
    Token('OTHER', ' '),
    Token('UPPER', 'G'),
    Token('OTHER', ' '),
    Token('LOWER', 's')]
    assert expected == result


def test_test04():
    from rply import Token
    text = "CAT"
    result = sol.question02(text)
    expected = [Token('NON_TITLE_CASE', 'CAT')]
    assert expected == result
    text = "House"
    result = sol.question02(text)
    expected = [Token('TITLE_CASE', 'House')]
    assert expected == result
    text = "!"
    result = sol.question02(text)
    expected = [Token('OTHER', '!')]
    assert expected == result

def test_test05():
    from rply import Token
    text = "The Cat in the HAT,"
    result = sol.question02(text)
    expected = [Token('TITLE_CASE', 'The'),
    Token('TITLE_CASE', 'Cat'),
    Token('NON_TITLE_CASE', 'in'),
    Token('NON_TITLE_CASE', 'the'),
    Token('NON_TITLE_CASE', 'HAT'),
    Token('OTHER', ',')]
    assert expected == result
    text = "White\tCHRISTMAS in July 14"
    result = sol.question02(text)
    expected = [Token('TITLE_CASE', 'White'),
    Token('NON_TITLE_CASE', 'CHRISTMAS'),
    Token('NON_TITLE_CASE', 'in'),
    Token('TITLE_CASE', 'July'),
    Token('OTHER', '1'),
    Token('OTHER', '4')]
    assert expected == result
    
test_test01()