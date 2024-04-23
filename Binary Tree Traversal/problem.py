# Pre-order traversal
def pre_order(node):
    if not node:
        return []
    result=[]
    def recursive(node,result):
        result.append(node.data)
        if node.left:
            recursive(node.left,result)
        if node.right:
            recursive(node.right,result)
        return result
    return recursive(node,result)

# In-order traversal
def in_order(node):
    if not node:
        return []
    result=[]
    def recursive(node,result):
        if node.left:
            recursive(node.left,result)
        result.append(node.data)
        if node.right:
            recursive(node.right,result)
        return result
    return recursive(node,result)

# Post-order traversal
def post_order(node):
    if not node:
        return []
    result=[]
    def recursive(node,result):
        if node.left:
            recursive(node.left,result)
        if node.right:
            recursive(node.right,result)
        result.append(node.data)
        return result
    return recursive(node,result)
