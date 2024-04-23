from collections import deque

def tree_by_levels(node):
    if not node:
        return []
    result=[]
    stack=deque([node])
    while stack:
        elem=stack.popleft()
        result.append(elem.value)
        if elem.left:
            stack.append(elem.left)
        if elem.right:
            stack.append(elem.right)
    return result
