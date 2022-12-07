import solution as sol

def test_test01():
    arg1 = """
    {
        "name": "Nick",
        "age": 99,
        "work": {
            "location": "MSU",
            "salary": 1000000000,
            "emails": [
                "abc@msu.edu",
                "def@msu.edu"
            ]
        }
    }
    """
    result = sol.question01(arg1)
    expected = {'name': 'Nick', 'age': 99, 'work': {'location': 'MSU', 'salary': 1000000000, 'emails': ['abc@msu.edu', 'def@msu.edu']}}
    assert expected == result


def test_test02():
    arg1 = """
    {
    }
    """
    result = sol.question01(arg1)
    expected = {}
    assert expected == result


def test_test03():
    arg1 = """
        [
              {
                "expression":
                {
                  "arguments":
                  [
                    {
                      "commonType":
                      {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      },
                      "id": 18,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "lValueRequested": false,
                      "leftExpression":
                      {
                        "expression":
                        {
                          "id": 15,
                          "name": "msg",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": -15,
                          "src": "220:3:0",
                          "typeDescriptions":
                          {
                            "typeIdentifier": "t_magic_message",
                            "typeString": "msg"
                          }
                        },
                        "id": 16,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "memberName": "sender",
                        "nodeType": "MemberAccess",
                        "src": "220:10:0",
                        "typeDescriptions":
                        {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      },
                      "nodeType": "BinaryOperation",
                      "operator": "==",
                      "rightExpression":
                      {
                        "id": 17,
                        "name": "_owner",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 3,
                        "src": "234:6:0",
                        "typeDescriptions":
                        {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      },
                      "src": "220:20:0",
                      "typeDescriptions":
                      {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                      }
                    }
                  ],
                  "expression":
                  {
                    "argumentTypes":
                    [
                      {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                      }
                    ],
                    "id": 14,
                    "name": "require",
                    "nodeType": "Identifier",
                    "overloadedDeclarations":
                    [
                      -18,
                      -18
                    ],
                    "referencedDeclaration": -18,
                    "src": "212:7:0",
                    "typeDescriptions":
                    {
                      "typeIdentifier": "t_function_require_pure$_t_bool_$returns$__$",
                      "typeString": "function (bool) pure"
                    }
                  },
                  "id": 19,
                  "isConstant": false,
                  "isLValue": false,
                  "isPure": false,
                  "kind": "functionCall",
                  "lValueRequested": false,
                  "names": [],
                  "nodeType": "FunctionCall",
                  "src": "212:29:0",
                  "tryCall": false,
                  "typeDescriptions":
                  {
                    "typeIdentifier": "t_tuple$__$",
                    "typeString": "tuple()"
                  }
                },
                "id": 20,
                "nodeType": "ExpressionStatement",
                "src": "212:29:0"
              },
              {
                "id": 21,
                "nodeType": "PlaceholderStatement",
                "src": "251:1:0"
              }
            ]
    """
    result = sol.question01(arg1)
    expected = [{'expression': {'arguments': [{'commonType': {'typeIdentifier': 't_address', 'typeString': 'address'}, 'id': 18, 'isConstant': False, 'isLValue': False, 'isPure': False, 'lValueRequested': False, 'leftExpression': {'expression': {'id': 15, 'name': 'msg', 'nodeType': 'Identifier', 'overloadedDeclarations': [], 'referencedDeclaration': -15, 'src': '220:3:0', 'typeDescriptions': {'typeIdentifier': 't_magic_message', 'typeString': 'msg'}}, 'id': 16, 'isConstant': False, 'isLValue': False, 'isPure': False, 'lValueRequested': False, 'memberName': 'sender', 'nodeType': 'MemberAccess', 'src': '220:10:0', 'typeDescriptions': {'typeIdentifier': 't_address', 'typeString': 'address'}}, 'nodeType': 'BinaryOperation', 'operator': '==', 'rightExpression': {'id': 17, 'name': '_owner', 'nodeType': 'Identifier', 'overloadedDeclarations': [], 'referencedDeclaration': 3, 'src': '234:6:0', 'typeDescriptions': {'typeIdentifier': 't_address', 'typeString': 'address'}}, 'src': '220:20:0', 'typeDescriptions': {'typeIdentifier': 't_bool', 'typeString': 'bool'}}], 'expression': {'argumentTypes': [{'typeIdentifier': 't_bool', 'typeString': 'bool'}], 'id': 14, 'name': 'require', 'nodeType': 'Identifier', 'overloadedDeclarations': [-18, -18], 'referencedDeclaration': -18, 'src': '212:7:0', 'typeDescriptions': {'typeIdentifier': 't_function_require_pure$_t_bool_$returns$__$', 'typeString': 'function (bool) pure'}}, 'id': 19, 'isConstant': False, 'isLValue': False, 'isPure': False, 'kind': 'functionCall', 'lValueRequested': False, 'names': [], 'nodeType': 'FunctionCall', 'src': '212:29:0', 'tryCall': False, 'typeDescriptions': {'typeIdentifier': 't_tuple$__$', 'typeString': 'tuple()'}}, 'id': 20, 'nodeType': 'ExpressionStatement', 'src': '212:29:0'}, {'id': 21, 'nodeType': 'PlaceholderStatement', 'src': '251:1:0'}]
    assert expected == result

def test_test04():
    arg1 = """
        { "hello" }
    """
    result = sol.question01(arg1)
    expected = {'error': True}
    assert expected == result


def test_test05():
    arg1 = """
              {
                "expression":
                {
                  "arguments":
                  [
                    {
                      "commonType":
                      {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      },
                      "id": 18,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "lValueRequested": false,
                      "leftExpression":
                      {
                        "expression":
                        {
                          "id": 15,
                          "name": "msg",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": -15,
                          "src": "220:3:0",
                          "typeDescriptions":
                          {
                            "typeIdentifier": "t_magic_message",
                            "typeString": "msg"
                          }
                        },
                        "id": 16,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "memberName": "sender",
                        "nodeType": "MemberAccess",
                        "src": "220:10:0",
                        "typeDescriptions":
                        {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      },
                      "nodeType": "BinaryOperation",
                      "operator": "==",
                      "rightExpression":
                      {
                        "id": 17,
                        "name": "_owner",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 3,
                        "src": "234:6:0",
                        "typeDescriptions":
                        {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      },
                      "src": "220:20:0",
                      "typeDescriptions":
                      {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                      }
                    }
                  ],
                  "expression":
                  {
                    "argumentTypes":
                    [
                      {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                      }
                    ],
                    "id": 14,
                    "name": "require",
                    "nodeType": "Identifier",
                    "overloadedDeclarations":
                    [
                      -18,
                      -18
                    ],
                    "referencedDeclaration": -18,
                    "src": "212:7:0",
                    "typeDescriptions":
                    {
                      "typeIdentifier": "t_function_require_pure$_t_bool_$returns$__$",
                      "typeString": "function (bool) pure"
                    }
                  },
                  "id": 19,
                  "isConstant": false,
                  "isLValue": false,
                  "isPure": false,
                  "kind": "functionCall",
                  "lValueRequested": false,
                  "names": [],
                  "nodeType": "FunctionCall",
                  "src": "212:29:0",
                  "tryCall": false,
                  "typeDescriptions":
                  {
                    "typeIdentifier": "t_tuple$__$",
                    "typeString": "tuple()"
                  }
                },
                "id": 20,
                "nodeType": "ExpressionStatement",
                "src": "212:29:0"
              },
              {
                "id": 21,
                "nodeType": "PlaceholderStatement",
                "src": "251:1:0"
              }
            ]
    """
    result = sol.question01(arg1)
    expected = {'error': True}
    assert expected == result