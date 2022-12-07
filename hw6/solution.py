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
    # Return the list of values obtained by in-order depth-first traversal 
    # of the tree (i.e., left-root-right) See the tests to better understand 
    # the requirements of the assignment.
    #
    # Assume the JSON string is always legitimate (i.e., no formating errors).


    import json
    tree = json.loads(text)
    path = []
    inOrder(tree, path)
    
    return path

def inOrder(node, path):
    if 'left' not in node and 'right' not in node:
        path.append(node['value'])
        return 
    
    if 'left' in node:
        inOrder(node['left'], path)
    path.append(node['value'])
    if 'right' in node:
        inOrder(node['right'], path)