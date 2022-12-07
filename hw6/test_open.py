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
    expected = [3, 7, 5]
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
    expected = [77, 33, 88, 55, 99]
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
    expected = [5, 3, 22, 11, 55, 999]
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
    expected = [45, 177, 122, 225, 11118, 277, 289, 15, 5531, 3555, 7744, 555, 676, 707777, 97430]
    assert expected == result

