import json
def question01(text):
    # The argument of this function is a JSON string.
    # The corresponding JSON object is a binary tree, each node of which
    # has the following format:
    #
    # {
    #   "value": <VALUE>,        
    #   "left": <LEFT_BRANCH>,
    #   "right": <RIGHT_BRANCH>
    # }
    #
    # where <LEFT_BRANCH> and <RIGHT_BRANCH> are nodes,
    # and each <VALUE> is an integer. If "left" or "right" do not exist,
    # then the node does not have corresponding branches. Intuitively,
    # a node with both "left" and "right" keys absent is a leaf.
    # 
    # Traverse the tree using pre-order depth-first order (i.e., root-left-right),
    # and add an integer element "order" into every node of the tree. The
    # value of the "order" element should indicate the order of traversal starting
    # from 1 (which is the root of the tree). Return a JSON object with the modified
    # tree. See the tests to better understand the requirements of the assignment.
    # For example, if the input tree is this:
    # {
    #    "value": 314,
    #    "left": {
    #        "value": 5
    #    },
    #    "right": {
    #         "value": 6
    #    }
    # }
    #
    # the output tree should be as follows:
    # {
    #     "value": 314,
    #     "left": {
    #         "value": 5,
    #         "order": 2
    #     },
    #     "right": {
    #         "value": 6,
    #         "order": 3
    #     },
    #     "order": 1
    # }    
    #
    # Assume the JSON string is always legitimate (i.e., no formating errors).

    tree = json.loads(text)
    
    preOrder(tree, 1)

    return tree


def preOrder(node, position):
    if "left" not  in node and "right" not in node:
        node['order'] = position
        return position 
    
    
    node['order'] = position
    if "left" in node:
        position = preOrder(node['left'], position + 1)
    if "right" in node:
        position = preOrder(node['right'], position + 1)
    return position



s1 = """
{
    "key1": "value1",
    "key2": "value2"
}
"""

s2 = """
{
    "key2": "value2",
    "key1": "value1"
}
"""

json1 = json.loads(s1)
json2 = json.loads(s2)

print(s1 == s2, json1 == json2)