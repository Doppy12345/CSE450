import solution as sol

def test_test01():
    arg1 = """
        { 
            "value": 3
        }
    """

    result = sol.question01(arg1)
    expected = [3]
    assert expected == result



def test_test02():
    arg1 = """
        { 
            "value": 7,


            "left": {
                "value": 3
            },

            "right": {
                "value": 5
            }
        }
    """

    result = sol.question01(arg1)
    expected = [3, 5, 7]
    assert expected == result



def test_test03():
    arg1 = """
        { 
            "value": 55,


            "left": {
                "value": 33,
                "left": {
                    "value": 77
                },
                "right": {
                    "value": 88
                }
            },

            "right": {
                "value": 99
            }
        }
    """

    result = sol.question01(arg1)
    expected = [77, 88, 33, 99, 55]
    assert expected == result


def test_test04():
    arg1 = """
            { 
                "value": 3,
                "left": {
                    "value": 5
                },
                "right": {
                    "value": 55,
                    "left": {
                        "value": 11,
                        "left": {
                            "value": 22
                        }
                    },
                    "right": {
                        "value": 999
                    }
                }
            }
        """

    result = sol.question01(arg1)
    expected = [5, 22, 11, 999, 55, 3]
    assert expected == result



def test_test05():
    arg1 = """
        {
            "value": 15,

            "left": {
                "value": 225,
                
                "left": {
                    "value": 177,

                    "left": {
                        "value": 45
                    },

                    "right": {
                        "value": 122
                    }
                },

                "right": {
                    "value": 277,

                    "left": {
                        "value": 11118
                    },

                    "right": {
                        "value": 289
                    }
                }
            },

            "right": {
                "value": 555,
                
                "left": {
                    "value": 3555,

                    "left": {
                        "value": 5531
                    },

                    "right": {
                        "value": 7744
                    }
                },

                "right": {
                    "value": 707777,

                    "left": {
                        "value": 676
                    },

                    "right": {
                        "value": 97430
                    }
                }
            }
        }
    """

    result = sol.question01(arg1)
    expected = [45, 122, 177, 11118, 289, 277, 225, 5531, 7744, 3555, 676, 97430, 707777, 555, 15]
    assert expected == result

