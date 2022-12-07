from solution import parse_spartytalk, interpret_spartytalk

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
                "id": 2,
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "id": 1,
                    "type": "expression",
                    "expression_type": "string",
                    "value": "hi"
                }
            },
            {
                "id": 4,
                "type": "statement",
                "statement_type": "nvar",
                "identifier": "b",
                "expression": {
                    "id": 3,
                    "type": "expression",
                    "expression_type": "number",
                    "value": "7"
                }
            },
            {
                "id": 20,
                "type": "statement",
                "statement_type": "nvar",
                "identifier": "a",
                "expression": {
                    "id": 19,
                    "type": "expression",
                    "expression_type": "plus",
                    "left": {
                        "id": 14,
                        "type": "expression",
                        "expression_type": "minus",
                        "left": {
                            "id": 7,
                            "type": "expression",
                            "expression_type": "plus",
                            "left": {
                                "id": 5,
                                "type": "expression",
                                "expression_type": "number",
                                "value": "10"
                            },
                            "right": {
                                "id": 6,
                                "type": "expression",
                                "expression_type": "number",
                                "value": "20"
                            }
                        },
                        "right": {
                            "id": 13,
                            "type": "expression",
                            "expression_type": "mul",
                            "left": {
                                "id": 8,
                                "type": "expression",
                                "expression_type": "number",
                                "value": "10"
                            },
                            "right": {
                                "id": 12,
                                "type": "expression",
                                "expression_type": "parentheses",
                                "expression": {
                                    "id": 11,
                                    "type": "expression",
                                    "expression_type": "mul",
                                    "left": {
                                        "id": 9,
                                        "type": "expression",
                                        "expression_type": "identifier",
                                        "identifier": "b"
                                    },
                                    "right": {
                                        "id": 10,
                                        "type": "expression",
                                        "expression_type": "number",
                                        "value": "255"
                                    }
                                }
                            }
                        }
                    },
                    "right": {
                        "id": 18,
                        "type": "expression",
                        "expression_type": "parentheses",
                        "expression": {
                            "id": 17,
                            "type": "expression",
                            "expression_type": "plus",
                            "left": {
                                "id": 15,
                                "type": "expression",
                                "expression_type": "identifier",
                                "identifier": "a"
                            },
                            "right": {
                                "id": 16,
                                "type": "expression",
                                "expression_type": "identifier",
                                "identifier": "b"
                            }
                        }
                    }
                }
            },
            {
                "id": 22,
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "id": 21,
                    "type": "expression",
                    "expression_type": "identifier",
                    "identifier": "a"
                }
            },
            {
                "id": 26,
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "id": 25,
                    "type": "expression",
                    "expression_type": "plus",
                    "left": {
                        "id": 23,
                        "type": "expression",
                        "expression_type": "identifier",
                        "identifier": "a"
                    },
                    "right": {
                        "id": 24,
                        "type": "expression",
                        "expression_type": "identifier",
                        "identifier": "b"
                    }
                }
            },
            {
                "id": 31,
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "id": 30,
                    "type": "expression",
                    "expression_type": "parentheses",
                    "expression": {
                        "id": 29,
                        "type": "expression",
                        "expression_type": "plus",
                        "left": {
                            "id": 27,
                            "type": "expression",
                            "expression_type": "identifier",
                            "identifier": "n"
                        },
                        "right": {
                            "id": 28,
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

    expected_seq = [2, 4, 20, 22, 26, 31]
    output_seq = interpret_spartytalk(output)
    assert output_seq == expected_seq



def test_test002():
    program = """
gogreen;
gowhite;
"""
    
    expected = {
        "type": "error",
        "tokentype": "GOWHITE",
        "line": 3,
        "column": 1,
        "id": 0
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
                "id": 2,
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "a",
                "expression": {
                    "id": 1,
                    "type": "expression",
                    "expression_type": "number",
                    "value": "17"
                }
            },
            {
                "id": 4,
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "b",
                "expression": {
                    "id": 3,
                    "type": "expression",
                    "expression_type": "number",
                    "value": "20"
                }
            }
        ]
    }

    assert output == expected

    expected_seq = [2, 4]
    output_seq = interpret_spartytalk(output)
    assert output_seq == expected_seq




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
        "column": 16,
        "id": 4
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

    expected = {
        "type": "program",
        "statements": [
            {
                "id": 2,
                "type": "statement",
                "statement_type": "nvar",
                "identifier": "var1020",
                "expression": {
                    "id": 1,
                    "type": "expression",
                    "expression_type": "number",
                    "value": "1020"
                }
            }
        ]
    }


    assert output == expected

    expected_seq = [2]
    output_seq = interpret_spartytalk(output)
    assert output_seq == expected_seq


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
                "id": 2,
                "type": "statement",
                "statement_type": "nvar",
                "identifier": "car10",
                "expression": {
                    "id": 1,
                    "type": "expression",
                    "expression_type": "number",
                    "value": "180"
                }
            },
            {
                "id": 4,
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "id": 3,
                    "type": "expression",
                    "expression_type": "identifier",
                    "identifier": "car10"
                }
            }
        ]
    }


    assert output == expected

    expected_seq = [2, 4]
    output_seq = interpret_spartytalk(output)
    assert output_seq == expected_seq


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
                "id": 2,
                "type": "statement",
                "statement_type": "nvar",
                "identifier": "car88",
                "expression": {
                    "id": 1,
                    "type": "expression",
                    "expression_type": "number",
                    "value": "100.0"
                }
            },
            {
                "id": 6,
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "id": 5,
                    "type": "expression",
                    "expression_type": "mul",
                    "left": {
                        "id": 3,
                        "type": "expression",
                        "expression_type": "identifier",
                        "identifier": "car11"
                    },
                    "right": {
                        "id": 4,
                        "type": "expression",
                        "expression_type": "number",
                        "value": "35"
                    }
                }
            }
        ]
    }


    assert output == expected

    expected_seq = [2, 6]
    output_seq = interpret_spartytalk(output)
    assert output_seq == expected_seq


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
                "id": 7,
                "type": "statement",
                "statement_type": "nvar",
                "identifier": "variableX",
                "expression": {
                    "id": 6,
                    "type": "expression",
                    "expression_type": "mul",
                    "left": {
                        "id": 4,
                        "type": "expression",
                        "expression_type": "parentheses",
                        "expression": {
                            "id": 3,
                            "type": "expression",
                            "expression_type": "minus",
                            "left": {
                                "id": 1,
                                "type": "expression",
                                "expression_type": "number",
                                "value": "100.25"
                            },
                            "right": {
                                "id": 2,
                                "type": "expression",
                                "expression_type": "number",
                                "value": "7.1"
                            }
                        }
                    },
                    "right": {
                        "id": 5,
                        "type": "expression",
                        "expression_type": "number",
                        "value": "2"
                    }
                }
            },
            {
                "id": 13,
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "id": 12,
                    "type": "expression",
                    "expression_type": "minus",
                    "left": {
                        "id": 10,
                        "type": "expression",
                        "expression_type": "div",
                        "left": {
                            "id": 8,
                            "type": "expression",
                            "expression_type": "identifier",
                            "identifier": "car11"
                        },
                        "right": {
                            "id": 9,
                            "type": "expression",
                            "expression_type": "number",
                            "value": "35.3"
                        }
                    },
                    "right": {
                        "id": 11,
                        "type": "expression",
                        "expression_type": "number",
                        "value": "1"
                    }
                }
            }
        ]
    }


    assert output == expected

    expected_seq = [7, 13]
    output_seq = interpret_spartytalk(output)
    assert output_seq == expected_seq



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
                "id": 2,
                "type": "statement",
                "statement_type": "svar",
                "identifier": "s",
                "expression": {
                    "id": 1,
                    "type": "expression",
                    "expression_type": "string",
                    "value": "hello"
                }
            },
            {
                "id": 4,
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "id": 3,
                    "type": "expression",
                    "expression_type": "identifier",
                    "identifier": "s"
                }
            }
        ]
    }


    assert output == expected

    expected_seq = [2, 4]
    output_seq = interpret_spartytalk(output)
    assert output_seq == expected_seq
 

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
                "id": 2,
                "type": "statement",
                "statement_type": "svar",
                "identifier": "s",
                "expression": {
                    "id": 1,
                    "type": "expression",
                    "expression_type": "string",
                    "value": "hello, "
                }
            },
            {
                "id": 4,
                "type": "statement",
                "statement_type": "svar",
                "identifier": "q",
                "expression": {
                    "id": 3,
                    "type": "expression",
                    "expression_type": "string",
                    "value": "world"
                }
            },
            {
                "id": 8,
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "id": 7,
                    "type": "expression",
                    "expression_type": "plus",
                    "left": {
                        "id": 5,
                        "type": "expression",
                        "expression_type": "identifier",
                        "identifier": "s"
                    },
                    "right": {
                        "id": 6,
                        "type": "expression",
                        "expression_type": "identifier",
                        "identifier": "q"
                    }
                }
            }
        ]
    }


    assert output == expected

    expected_seq = [2, 4, 8]
    output_seq = interpret_spartytalk(output)
    assert output_seq == expected_seq


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
                "id": 2,
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "a",
                "expression": {
                    "id": 1,
                    "type": "expression",
                    "expression_type": "number",
                    "value": "10"
                }
            },
            {
                "id": 4,
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "a",
                "expression": {
                    "id": 3,
                    "type": "expression",
                    "expression_type": "string",
                    "value": "hello"
                }
            },
            {
                "id": 8,
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "a",
                "expression": {
                    "id": 7,
                    "type": "expression",
                    "expression_type": "plus",
                    "left": {
                        "id": 5,
                        "type": "expression",
                        "expression_type": "identifier",
                        "identifier": "a"
                    },
                    "right": {
                        "id": 6,
                        "type": "expression",
                        "expression_type": "identifier",
                        "identifier": "a"
                    }
                }
            }
        ]
    }

    assert output == expected

    expected_seq = [2, 4, 8]
    output_seq = interpret_spartytalk(output)
    assert output_seq == expected_seq

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
                "id": 2,
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "a",
                "expression": {
                    "id": 1,
                    "type": "expression",
                    "expression_type": "number",
                    "value": "17.5"
                }
            },
            {
                "id": 4,
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "b",
                "expression": {
                    "id": 3,
                    "type": "expression",
                    "expression_type": "string",
                    "value": "relatively long string"
                }
            },
            {
                "id": 8,
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "c",
                "expression": {
                    "id": 7,
                    "type": "expression",
                    "expression_type": "plus",
                    "left": {
                        "id": 5,
                        "type": "expression",
                        "expression_type": "identifier",
                        "identifier": "a"
                    },
                    "right": {
                        "id": 6,
                        "type": "expression",
                        "expression_type": "identifier",
                        "identifier": "b"
                    }
                }
            },
            {
                "id": 23,
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "id": 22,
                    "type": "expression",
                    "expression_type": "mul",
                    "left": {
                        "id": 20,
                        "type": "expression",
                        "expression_type": "parentheses",
                        "expression": {
                            "id": 19,
                            "type": "expression",
                            "expression_type": "div",
                            "left": {
                                "id": 17,
                                "type": "expression",
                                "expression_type": "parentheses",
                                "expression": {
                                    "id": 16,
                                    "type": "expression",
                                    "expression_type": "mul",
                                    "left": {
                                        "id": 14,
                                        "type": "expression",
                                        "expression_type": "mul",
                                        "left": {
                                            "id": 12,
                                            "type": "expression",
                                            "expression_type": "parentheses",
                                            "expression": {
                                                "id": 11,
                                                "type": "expression",
                                                "expression_type": "plus",
                                                "left": {
                                                    "id": 9,
                                                    "type": "expression",
                                                    "expression_type": "identifier",
                                                    "identifier": "c"
                                                },
                                                "right": {
                                                    "id": 10,
                                                    "type": "expression",
                                                    "expression_type": "identifier",
                                                    "identifier": "a"
                                                }
                                            }
                                        },
                                        "right": {
                                            "id": 13,
                                            "type": "expression",
                                            "expression_type": "identifier",
                                            "identifier": "b"
                                        }
                                    },
                                    "right": {
                                        "id": 15,
                                        "type": "expression",
                                        "expression_type": "number",
                                        "value": "10.777"
                                    }
                                }
                            },
                            "right": {
                                "id": 18,
                                "type": "expression",
                                "expression_type": "string",
                                "value": "world"
                            }
                        }
                    },
                    "right": {
                        "id": 21,
                        "type": "expression",
                        "expression_type": "number",
                        "value": "20.55"
                    }
                }
            }
        ]
    }


    assert output == expected

    expected_seq = [2, 4, 8, 23]
    output_seq = interpret_spartytalk(output)
    assert output_seq == expected_seq

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
                "id": 2,
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "a",
                "expression": {
                    "id": 1,
                    "type": "expression",
                    "expression_type": "number",
                    "value": "-27.5"
                }
            },
            {
                "id": 4,
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "id": 3,
                    "type": "expression",
                    "expression_type": "identifier",
                    "identifier": "a"
                }
            }
        ]
    }


    assert output == expected

    expected_seq = [2, 4]
    output_seq = interpret_spartytalk(output)
    assert output_seq == expected_seq


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
                "id": 4,
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "a",
                "expression": {
                    "id": 3,
                    "type": "expression",
                    "expression_type": "minus",
                    "left": {
                        "id": 1,
                        "type": "expression",
                        "expression_type": "number",
                        "value": "7"
                    },
                    "right": {
                        "id": 2,
                        "type": "expression",
                        "expression_type": "number",
                        "value": "-27.6"
                    }
                }
            },
            {
                "id": 6,
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "id": 5,
                    "type": "expression",
                    "expression_type": "identifier",
                    "identifier": "a"
                }
            }
        ]
    }


    assert output == expected

    expected_seq = [4, 6]
    output_seq = interpret_spartytalk(output)
    assert output_seq == expected_seq

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
                "id": 4,
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "a",
                "expression": {
                    "id": 3,
                    "type": "expression",
                    "expression_type": "plus",
                    "left": {
                        "id": 1,
                        "type": "expression",
                        "expression_type": "number",
                        "value": "+8.2"
                    },
                    "right": {
                        "id": 2,
                        "type": "expression",
                        "expression_type": "number",
                        "value": "+3.6"
                    }
                }
            },
            {
                "id": 6,
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "id": 5,
                    "type": "expression",
                    "expression_type": "identifier",
                    "identifier": "a"
                }
            }
        ]
    }


    assert output == expected

    expected_seq = [4, 6]
    output_seq = interpret_spartytalk(output)
    assert output_seq == expected_seq


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
                "id": 17,
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "c",
                "expression": {
                    "id": 16,
                    "type": "expression",
                    "expression_type": "minus",
                    "left": {
                        "id": 11,
                        "type": "expression",
                        "expression_type": "minus",
                        "left": {
                            "id": 1,
                            "type": "expression",
                            "expression_type": "number",
                            "value": "0"
                        },
                        "right": {
                            "id": 10,
                            "type": "expression",
                            "expression_type": "mul",
                            "left": {
                                "id": 5,
                                "type": "expression",
                                "expression_type": "parentheses",
                                "expression": {
                                    "id": 4,
                                    "type": "expression",
                                    "expression_type": "div",
                                    "left": {
                                        "id": 2,
                                        "type": "expression",
                                        "expression_type": "number",
                                        "value": "50"
                                    },
                                    "right": {
                                        "id": 3,
                                        "type": "expression",
                                        "expression_type": "number",
                                        "value": "0"
                                    }
                                }
                            },
                            "right": {
                                "id": 9,
                                "type": "expression",
                                "expression_type": "parentheses",
                                "expression": {
                                    "id": 8,
                                    "type": "expression",
                                    "expression_type": "plus",
                                    "left": {
                                        "id": 6,
                                        "type": "expression",
                                        "expression_type": "number",
                                        "value": "50"
                                    },
                                    "right": {
                                        "id": 7,
                                        "type": "expression",
                                        "expression_type": "number",
                                        "value": "5.777"
                                    }
                                }
                            }
                        }
                    },
                    "right": {
                        "id": 15,
                        "type": "expression",
                        "expression_type": "parentheses",
                        "expression": {
                            "id": 14,
                            "type": "expression",
                            "expression_type": "div",
                            "left": {
                                "id": 12,
                                "type": "expression",
                                "expression_type": "string",
                                "value": "hello"
                            },
                            "right": {
                                "id": 13,
                                "type": "expression",
                                "expression_type": "string",
                                "value": "world"
                            }
                        }
                    }
                }
            },
            {
                "id": 19,
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "id": 18,
                    "type": "expression",
                    "expression_type": "identifier",
                    "identifier": "b"
                }
            }
        ]
    }


    assert output == expected

    expected_seq = [17, 19]
    output_seq = interpret_spartytalk(output)
    assert output_seq == expected_seq

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
                "id": 2,
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "a",
                "expression": {
                    "id": 1,
                    "type": "expression",
                    "expression_type": "identifier",
                    "identifier": "hello"
                }
            },
            {
                "id": 4,
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "b",
                "expression": {
                    "id": 3,
                    "type": "expression",
                    "expression_type": "identifier",
                    "identifier": "world"
                }
            },
            {
                "id": 8,
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "id": 7,
                    "type": "expression",
                    "expression_type": "plus",
                    "left": {
                        "id": 5,
                        "type": "expression",
                        "expression_type": "identifier",
                        "identifier": "a"
                    },
                    "right": {
                        "id": 6,
                        "type": "expression",
                        "expression_type": "identifier",
                        "identifier": "b"
                    }
                }
            }
        ]
    }


    assert output == expected

    expected_seq = [2, 4, 8]
    output_seq = interpret_spartytalk(output)
    assert output_seq == expected_seq

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
        "column": 9,
        "id": 1
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
                "id": 2,
                "type": "statement",
                "statement_type": "nvar",
                "identifier": "a",
                "expression": {
                    "id": 1,
                    "type": "expression",
                    "expression_type": "number",
                    "value": "777.5"
                }
            },
            {
                "id": 4,
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "b",
                "expression": {
                    "id": 3,
                    "type": "expression",
                    "expression_type": "number",
                    "value": "10"
                }
            },
            {
                "id": 11,
                "type": "statement",
                "statement_type": "assignment",
                "identifier": "a",
                "expression": {
                    "id": 10,
                    "type": "expression",
                    "expression_type": "minus",
                    "left": {
                        "id": 8,
                        "type": "expression",
                        "expression_type": "parentheses",
                        "expression": {
                            "id": 7,
                            "type": "expression",
                            "expression_type": "plus",
                            "left": {
                                "id": 5,
                                "type": "expression",
                                "expression_type": "string",
                                "value": "hello"
                            },
                            "right": {
                                "id": 6,
                                "type": "expression",
                                "expression_type": "string",
                                "value": "world"
                            }
                        }
                    },
                    "right": {
                        "id": 9,
                        "type": "expression",
                        "expression_type": "string",
                        "value": "goodbye"
                    }
                }
            },
            {
                "id": 13,
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "id": 12,
                    "type": "expression",
                    "expression_type": "identifier",
                    "identifier": "Nvar"
                }
            }
        ]
    }


    assert output == expected

    expected_seq = [2, 4, 11, 13]
    output_seq = interpret_spartytalk(output)
    assert output_seq == expected_seq

def test_test020():
    program = """
gogreen;
spartysays -10.55 / "hello";
gowhite;
"""
    output = parse_spartytalk(program)

    expected = {
        "type": "program",
        "statements": [
            {
                "id": 4,
                "type": "statement",
                "statement_type": "spartysays",
                "expression": {
                    "id": 3,
                    "type": "expression",
                    "expression_type": "div",
                    "left": {
                        "id": 1,
                        "type": "expression",
                        "expression_type": "number",
                        "value": "-10.55"
                    },
                    "right": {
                        "id": 2,
                        "type": "expression",
                        "expression_type": "string",
                        "value": "hello"
                    }
                }
            }
        ]
    }


    assert output == expected

    expected_seq = [4]
    output_seq = interpret_spartytalk(output)
    assert output_seq == expected_seq    