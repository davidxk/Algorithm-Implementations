
def level_order_traversal(root):
    front = []
    if root is not None:
        front.append(root)
    result = []
    while front:
        children = []
        result.append(map(lambda node: node.val, front))
        for node in front:
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
        front = children
    return result

def bfs_depth_limited(root, depth):
    front = []
    if root is not None:
        front.append(root)
    cnt = 0
    while front and cnt < depth:
        children = []
        for node in front:
            for child in node.left, node.right:
                if child is not None:
                    children.append(child)
        front = children
        cnt += 1
    return front

def dfs_depth_limited(root, depth):
    def helper(root, currDepth, result):
        if root is None:
            return result
        elif currDepth == depth:
            result.append(root.val)
            return result
        helper(root.left, currDepth + 1, result)
        helper(root.right, currDepth + 1, result)
        return result
    return helper(root, 0, [])
