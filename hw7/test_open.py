import solution as sol

def test_test01():
    arg1 = """
        { 
            "value": 3
        }
    """

    result = sol.question01(arg1)
    expected = {
        "value": 3,
        "order": 1
    }
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
    expected = {
        "value": 7,
        "left": {
            "value": 3,
            "order": 2
        },
        "right": {
            "value": 5,
            "order": 3
        },
        "order": 1
    }
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
    expected = {
        "value": 55,
        "left": {
            "value": 33,
            "left": {
                "value": 77,
                "order": 3
            },
            "right": {
                "value": 88,
                "order": 4
            },
            "order": 2
        },
        "right": {
            "value": 99,
            "order": 5
        },
        "order": 1
    }
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
    expected = {
        "value": 3,
        "left": {
            "value": 5,
            "order": 2
        },
        "right": {
            "value": 55,
            "left": {
                "value": 11,
                "left": {
                    "value": 22,
                    "order": 5
                },
                "order": 4
            },
            "right": {
                "value": 999,
                "order": 6
            },
            "order": 3
        },
        "order": 1
    }
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
    expected = {
        "value": 15,
        "left": {
            "value": 225,
            "left": {
                "value": 177,
                "left": {
                    "value": 45,
                    "order": 4
                },
                "right": {
                    "value": 122,
                    "order": 5
                },
                "order": 3
            },
            "right": {
                "value": 277,
                "left": {
                    "value": 11118,
                    "order": 7
                },
                "right": {
                    "value": 289,
                    "order": 8
                },
                "order": 6
            },
            "order": 2
        },
        "right": {
            "value": 555,
            "left": {
                "value": 3555,
                "left": {
                    "value": 5531,
                    "order": 11
                },
                "right": {
                    "value": 7744,
                    "order": 12
                },
                "order": 10
            },
            "right": {
                "value": 707777,
                "left": {
                    "value": 676,
                    "order": 14
                },
                "right": {
                    "value": 97430,
                    "order": 15
                },
                "order": 13
            },
            "order": 9
        },
        "order": 1
    }
    assert expected == result

