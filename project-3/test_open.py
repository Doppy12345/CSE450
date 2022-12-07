
from solution import parse_spartytalk

def test_test001():
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
    output = parse_spartytalk(program)
    
    expected = {
        "type": "program",
        "statements": [
            {
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "type": "expression",
                    "expression_type": "string",
                    "value": "hi"
                }
            },
            {
                "type": "statement",
                "statement_type": "nvar",
                "identifier": "b",
                "expression": {
                    "type": "expression",
                    "expression_type": "number",
                    "value": "7"
                }
            },
            {
                "type": "statement",
                "statement_type": "nvar",
                "identifier": "a",
                "expression": {
                    "type": "expression",
                    "expression_type": "plus",
                    "left": {
                        "type": "expression",
                        "expression_type": "minus",
                        "left": {
                            "type": "expression",
                            "expression_type": "plus",
                            "left": {
                                "type": "expression",
                                "expression_type": "number",
                                "value": "10"
                            },
                            "right": {
                                "type": "expression",
                                "expression_type": "number",
                                "value": "20"
                            }
                        },
                        "right": {
                            "type": "expression",
                            "expression_type": "mul",
                            "left": {
                                "type": "expression",
                                "expression_type": "number",
                                "value": "10"
                            },
                            "right": {
                                "type": "expression",
                                "expression_type": "parentheses",
                                "expression": {
                                    "type": "expression",
                                    "expression_type": "mul",
                                    "left": {
                                        "type": "expression",
                                        "expression_type": "identifier",
                                        "identifier": "b"
                                    },
                                    "right": {
                                        "type": "expression",
                                        "expression_type": "number",
                                        "value": "255"
                                    }
                                }
                            }
                        }
                    },
                    "right": {
                        "type": "expression",
                        "expression_type": "parentheses",
                        "expression": {
                            "type": "expression",
                            "expression_type": "plus",
                            "left": {
                                "type": "expression",
                                "expression_type": "identifier",
                                "identifier": "a"
                            },
                            "right": {
                                "type": "expression",
                                "expression_type": "identifier",
                                "identifier": "b"
                            }
                        }
                    }
                }
            },
            {
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "type": "expression",
                    "expression_type": "identifier",
                    "identifier": "a"
                }
            },
            {
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "type": "expression",
                    "expression_type": "plus",
                    "left": {
                        "type": "expression",
                        "expression_type": "identifier",
                        "identifier": "a"
                    },
                    "right": {
                        "type": "expression",
                        "expression_type": "identifier",
                        "identifier": "b"
                    }
                }
            },
            {
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "type": "expression",
                    "expression_type": "parentheses",
                    "expression": {
                        "type": "expression",
                        "expression_type": "plus",
                        "left": {
                            "type": "expression",
                            "expression_type": "identifier",
                            "identifier": "n"
                        },
                        "right": {
                            "type": "expression",
                            "expression_type": "identifier",
                            "identifier": "k"
                        }
                    }
                }
            }
        ]
    }

    assert output == expected
    print('sueccess')

def test_test002():
    program = """
gogreen;
gowhite;
"""
    
    expected = {
        "type": "error",
        "tokentype": "GOWHITE",
        "line": 3,
        "column": 1
    }

    try:
        output = parse_spartytalk(program)
        assert False
    except Exception as e:
        assert expected == e.args[0]



def test_test003():
    program = """
gogreen;
a = 17; b = 20;
gowhite;
"""
    output = parse_spartytalk(program)

    expected = {
        "type": "program",
        "statements": [
            {
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "a",
                "expression": {
                    "type": "expression",
                    "expression_type": "number",
                    "value": "17"
                }
            },
            {
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "b",
                "expression": {
                    "type": "expression",
                    "expression_type": "number",
                    "value": "20"
                }
            }
        ]
    }


    assert output == expected


def test_test004():
    program = """
gogreen;
a = 17; b = 20;;
gowhite;
"""

    expected = {
        "type": "error",
        "tokentype": "SEMICOLON",
        "line": 3,
        "column": 16
    }

    try:
        output = parse_spartytalk(program)
        assert False
    except Exception as e:
        assert expected == e.args[0]


def test_test005():
    program = """
gogreen;
nvar var1020 = 1020;
gowhite;
"""
    
    output = parse_spartytalk(program)
    print(output)
    expected = {
        "type": "program",
        "statements": [
            {
                "type": "statement",
                "statement_type": "nvar",
                "identifier": "var1020",
                "expression": {
                    "type": "expression",
                    "expression_type": "number",
                    "value": "1020"
                }
            }
        ]
    }


    assert output == expected


def test_test006():
    program = """
gogreen;
nvar car10 = 180;
spartysays car10;
gowhite;
"""
    output = parse_spartytalk(program)

    expected = {
        "type": "program",
        "statements": [
            {
                "type": "statement",
                "statement_type": "nvar",
                "identifier": "car10",
                "expression": {
                    "type": "expression",
                    "expression_type": "number",
                    "value": "180"
                }
            },
            {
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "type": "expression",
                    "expression_type": "identifier",
                    "identifier": "car10"
                }
            }
        ]
    }


    assert output == expected


def test_test007():
    program = """
gogreen;
nvar car88 = 100.0;
spartysays car11 * 35;
gowhite;
"""
    output = parse_spartytalk(program)

    expected = {
        "type": "program",
        "statements": [
            {
                "type": "statement",
                "statement_type": "nvar",
                "identifier": "car88",
                "expression": {
                    "type": "expression",
                    "expression_type": "number",
                    "value": "100.0"
                }
            },
            {
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "type": "expression",
                    "expression_type": "mul",
                    "left": {
                        "type": "expression",
                        "expression_type": "identifier",
                        "identifier": "car11"
                    },
                    "right": {
                        "type": "expression",
                        "expression_type": "number",
                        "value": "35"
                    }
                }
            }
        ]
    }


    assert output == expected



def test_test008():
    program = """
gogreen;
nvar variableX = (100.25 - 7.1) * 2;
spartysays car11 / 35.3 - 1;
gowhite;
"""
    output = parse_spartytalk(program)

    expected = {
        "type": "program",
        "statements": [
            {
                "type": "statement",
                "statement_type": "nvar",
                "identifier": "variableX",
                "expression": {
                    "type": "expression",
                    "expression_type": "mul",
                    "left": {
                        "type": "expression",
                        "expression_type": "parentheses",
                        "expression": {
                            "type": "expression",
                            "expression_type": "minus",
                            "left": {
                                "type": "expression",
                                "expression_type": "number",
                                "value": "100.25"
                            },
                            "right": {
                                "type": "expression",
                                "expression_type": "number",
                                "value": "7.1"
                            }
                        }
                    },
                    "right": {
                        "type": "expression",
                        "expression_type": "number",
                        "value": "2"
                    }
                }
            },
            {
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "type": "expression",
                    "expression_type": "minus",
                    "left": {
                        "type": "expression",
                        "expression_type": "div",
                        "left": {
                            "type": "expression",
                            "expression_type": "identifier",
                            "identifier": "car11"
                        },
                        "right": {
                            "type": "expression",
                            "expression_type": "number",
                            "value": "35.3"
                        }
                    },
                    "right": {
                        "type": "expression",
                        "expression_type": "number",
                        "value": "1"
                    }
                }
            }
        ]
    }


    assert output == expected




def test_test009():
    program = """
gogreen;
svar s = "hello";
spartysays s;
gowhite;
"""
    output = parse_spartytalk(program)

    expected = {
        "type": "program",
        "statements": [
            {
                "type": "statement",
                "statement_type": "svar",
                "identifier": "s",
                "expression": {
                    "type": "expression",
                    "expression_type": "string",
                    "value": "hello"
                }
            },
            {
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "type": "expression",
                    "expression_type": "identifier",
                    "identifier": "s"
                }
            }
        ]
    }


    assert output == expected


def test_test010():
    program = """
gogreen;
svar s = "hello, ";
svar q = "world";
spartysays s + q;
gowhite;
"""
    output = parse_spartytalk(program)

    expected = {
        "type": "program",
        "statements": [
            {
                "type": "statement",
                "statement_type": "svar",
                "identifier": "s",
                "expression": {
                    "type": "expression",
                    "expression_type": "string",
                    "value": "hello, "
                }
            },
            {
                "type": "statement",
                "statement_type": "svar",
                "identifier": "q",
                "expression": {
                    "type": "expression",
                    "expression_type": "string",
                    "value": "world"
                }
            },
            {
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "type": "expression",
                    "expression_type": "plus",
                    "left": {
                        "type": "expression",
                        "expression_type": "identifier",
                        "identifier": "s"
                    },
                    "right": {
                        "type": "expression",
                        "expression_type": "identifier",
                        "identifier": "q"
                    }
                }
            }
        ]
    }


    assert output == expected




def test_test011():
    program = """
gogreen;
a = 10;
a = "hello";
a = a + a;
gowhite;
"""
    output = parse_spartytalk(program)

    expected = {
        "type": "program",
        "statements": [
            {
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "a",
                "expression": {
                    "type": "expression",
                    "expression_type": "number",
                    "value": "10"
                }
            },
            {
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "a",
                "expression": {
                    "type": "expression",
                    "expression_type": "string",
                    "value": "hello"
                }
            },
            {
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "a",
                "expression": {
                    "type": "expression",
                    "expression_type": "plus",
                    "left": {
                        "type": "expression",
                        "expression_type": "identifier",
                        "identifier": "a"
                    },
                    "right": {
                        "type": "expression",
                        "expression_type": "identifier",
                        "identifier": "a"
                    }
                }
            }
        ]
    }


    assert output == expected



def test_test012():
    program = """
gogreen;
a = 17.5;
b = "relatively long string";
c = a + b;
spartysays (((c + a) * b * 10.777) / "world") * 20.55;
gowhite;
"""
    output = parse_spartytalk(program)

    expected = {
        "type": "program",
        "statements": [
            {
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "a",
                "expression": {
                    "type": "expression",
                    "expression_type": "number",
                    "value": "17.5"
                }
            },
            {
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "b",
                "expression": {
                    "type": "expression",
                    "expression_type": "string",
                    "value": "relatively long string"
                }
            },
            {
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "c",
                "expression": {
                    "type": "expression",
                    "expression_type": "plus",
                    "left": {
                        "type": "expression",
                        "expression_type": "identifier",
                        "identifier": "a"
                    },
                    "right": {
                        "type": "expression",
                        "expression_type": "identifier",
                        "identifier": "b"
                    }
                }
            },
            {
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "type": "expression",
                    "expression_type": "mul",
                    "left": {
                        "type": "expression",
                        "expression_type": "parentheses",
                        "expression": {
                            "type": "expression",
                            "expression_type": "div",
                            "left": {
                                "type": "expression",
                                "expression_type": "parentheses",
                                "expression": {
                                    "type": "expression",
                                    "expression_type": "mul",
                                    "left": {
                                        "type": "expression",
                                        "expression_type": "mul",
                                        "left": {
                                            "type": "expression",
                                            "expression_type": "parentheses",
                                            "expression": {
                                                "type": "expression",
                                                "expression_type": "plus",
                                                "left": {
                                                    "type": "expression",
                                                    "expression_type": "identifier",
                                                    "identifier": "c"
                                                },
                                                "right": {
                                                    "type": "expression",
                                                    "expression_type": "identifier",
                                                    "identifier": "a"
                                                }
                                            }
                                        },
                                        "right": {
                                            "type": "expression",
                                            "expression_type": "identifier",
                                            "identifier": "b"
                                        }
                                    },
                                    "right": {
                                        "type": "expression",
                                        "expression_type": "number",
                                        "value": "10.777"
                                    }
                                }
                            },
                            "right": {
                                "type": "expression",
                                "expression_type": "string",
                                "value": "world"
                            }
                        }
                    },
                    "right": {
                        "type": "expression",
                        "expression_type": "number",
                        "value": "20.55"
                    }
                }
            }
        ]
    }


    assert output == expected



def test_test013():
    program = """
gogreen;
a = -27.5;
spartysays a;
gowhite;
"""
    output = parse_spartytalk(program)

    expected = {
        "type": "program",
        "statements": [
            {
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "a",
                "expression": {
                    "type": "expression",
                    "expression_type": "number",
                    "value": "-27.5"
                }
            },
            {
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "type": "expression",
                    "expression_type": "identifier",
                    "identifier": "a"
                }
            }
        ]
    }


    assert output == expected




def test_test014():
    program = """
gogreen;
a = 7 - -27.6;
spartysays a;
gowhite;
"""
    output = parse_spartytalk(program)

    expected = {
        "type": "program",
        "statements": [
            {
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "a",
                "expression": {
                    "type": "expression",
                    "expression_type": "minus",
                    "left": {
                        "type": "expression",
                        "expression_type": "number",
                        "value": "7"
                    },
                    "right": {
                        "type": "expression",
                        "expression_type": "number",
                        "value": "-27.6"
                    }
                }
            },
            {
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "type": "expression",
                    "expression_type": "identifier",
                    "identifier": "a"
                }
            }
        ]
    }


    assert output == expected



def test_test015():
    program = """
gogreen;
a = +8.2 + +3.6;
spartysays a;
gowhite;
"""
    output = parse_spartytalk(program)

    expected = {
        "type": "program",
        "statements": [
            {
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "a",
                "expression": {
                    "type": "expression",
                    "expression_type": "plus",
                    "left": {
                        "type": "expression",
                        "expression_type": "number",
                        "value": "+8.2"
                    },
                    "right": {
                        "type": "expression",
                        "expression_type": "number",
                        "value": "+3.6"
                    }
                }
            },
            {
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "type": "expression",
                    "expression_type": "identifier",
                    "identifier": "a"
                }
            }
        ]
    }


    assert output == expected



def test_test016():
    program = """
gogreen;
c = 0 - (50 / 0) * (50 + 5.777) - ("hello" / "world");
spartysays b;
gowhite;
"""
    output = parse_spartytalk(program)

    expected = {
        "type": "program",
        "statements": [
            {
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "c",
                "expression": {
                    "type": "expression",
                    "expression_type": "minus",
                    "left": {
                        "type": "expression",
                        "expression_type": "minus",
                        "left": {
                            "type": "expression",
                            "expression_type": "number",
                            "value": "0"
                        },
                        "right": {
                            "type": "expression",
                            "expression_type": "mul",
                            "left": {
                                "type": "expression",
                                "expression_type": "parentheses",
                                "expression": {
                                    "type": "expression",
                                    "expression_type": "div",
                                    "left": {
                                        "type": "expression",
                                        "expression_type": "number",
                                        "value": "50"
                                    },
                                    "right": {
                                        "type": "expression",
                                        "expression_type": "number",
                                        "value": "0"
                                    }
                                }
                            },
                            "right": {
                                "type": "expression",
                                "expression_type": "parentheses",
                                "expression": {
                                    "type": "expression",
                                    "expression_type": "plus",
                                    "left": {
                                        "type": "expression",
                                        "expression_type": "number",
                                        "value": "50"
                                    },
                                    "right": {
                                        "type": "expression",
                                        "expression_type": "number",
                                        "value": "5.777"
                                    }
                                }
                            }
                        }
                    },
                    "right": {
                        "type": "expression",
                        "expression_type": "parentheses",
                        "expression": {
                            "type": "expression",
                            "expression_type": "div",
                            "left": {
                                "type": "expression",
                                "expression_type": "string",
                                "value": "hello"
                            },
                            "right": {
                                "type": "expression",
                                "expression_type": "string",
                                "value": "world"
                            }
                        }
                    }
                }
            },
            {
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "type": "expression",
                    "expression_type": "identifier",
                    "identifier": "b"
                }
            }
        ]
    }


    assert output == expected


def test_test017():
    program = """
gogreen;
a = hello;
b = world;
spartysays a + b;
gowhite;
"""
    output = parse_spartytalk(program)

    expected = {
        "type": "program",
        "statements": [
            {
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "a",
                "expression": {
                    "type": "expression",
                    "expression_type": "identifier",
                    "identifier": "hello"
                }
            },
            {
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "b",
                "expression": {
                    "type": "expression",
                    "expression_type": "identifier",
                    "identifier": "world"
                }
            },
            {
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "type": "expression",
                    "expression_type": "plus",
                    "left": {
                        "type": "expression",
                        "expression_type": "identifier",
                        "identifier": "a"
                    },
                    "right": {
                        "type": "expression",
                        "expression_type": "identifier",
                        "identifier": "b"
                    }
                }
            }
        ]
    }


    assert output == expected


def test_test018():
    program = """
gogreen;
a = ((10+2);
gowhite;
"""
    
    expected = {
        "type": "error",
        "tokentype": "NUMBER",
        "line": 3,
        "column": 9
    }

    try:
        output = parse_spartytalk(program)
        assert False
    except Exception as e:
        assert expected == e.args[0]



def test_test019():
    program = """
gogreen;
nvar a = 777.5; b = 10; a = ("hello" + "world") - "goodbye";
spartysays Nvar;
gowhite;
"""
    output = parse_spartytalk(program)

    expected = {
        "type": "program",
        "statements": [
            {
                "type": "statement",
                "statement_type": "nvar",
                "identifier": "a",
                "expression": {
                    "type": "expression",
                    "expression_type": "number",
                    "value": "777.5"
                }
            },
            {
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "b",
                "expression": {
                    "type": "expression",
                    "expression_type": "number",
                    "value": "10"
                }
            },
            {
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "a",
                "expression": {
                    "type": "expression",
                    "expression_type": "minus",
                    "left": {
                        "type": "expression",
                        "expression_type": "parentheses",
                        "expression": {
                            "type": "expression",
                            "expression_type": "plus",
                            "left": {
                                "type": "expression",
                                "expression_type": "string",
                                "value": "hello"
                            },
                            "right": {
                                "type": "expression",
                                "expression_type": "string",
                                "value": "world"
                            }
                        }
                    },
                    "right": {
                        "type": "expression",
                        "expression_type": "string",
                        "value": "goodbye"
                    }
                }
            },
            {
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "type": "expression",
                    "expression_type": "identifier",
                    "identifier": "Nvar"
                }
            }
        ]
    }


    assert output == expected


def test_test020():
    program = """
gogreen;
spartysays -10.55 / "hello";
gowhite;
"""
    output = parse_spartytalk(program)
    print(output)
    expected = {
        "type": "program",
        "statements": [
            {
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "type": "expression",
                    "expression_type": "div",
                    "left": {
                        "type": "expression",
                        "expression_type": "number",
                        "value": "-10.55"
                    },
                    "right": {
                        "type": "expression",
                        "expression_type": "string",
                        "value": "hello"
                    }
                }
            }
        ]
    }


    assert output == expected
    
test_test005()
