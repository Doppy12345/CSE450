import solution as sol

def test_test01():
    arg1 = "This is a line"
    result = sol.question01(arg1)
    expected = "14: This is a line"
    assert expected == result

def test_test02():
    arg2 = "My class's name is CSE 450."
    result2 = sol.question01(arg2)
    expected2 = "27: My class's name is CSE 450."
    assert expected2 == result2

def test_test03():
    sentence = "Some words with repeated words"
    expected = {'words', 'repeated', 'Some', 'with'}
    result = sol.question02(sentence)
    assert expected == result


def test_test04():
    sentence = "some other input but this time it is serious, there is nothing tricky here"
    expected = {'but',
    'here',
    'input',
    'is',
    'it',
    'nothing',
    'other',
    'serious,',
    'some',
    'there',
    'this',
    'time',
    'tricky'}
    result = sol.question02(sentence)
    assert expected == result
    

def test_test05():
    try:
        sentence = "happy 30th birthday"
        sol.question02(sentence)
        assert False
    except Exception:
        assert True
    
    sentence = "one two two three"
    result = sol.question02(sentence)
    expected = {"one", "two", "three"}
    assert result == expected
    
def testSol():
    test_test01()
    test_test02()
    test_test03()
    test_test04()
    test_test05()
    print('completed')
    

testSol()