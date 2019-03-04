# Recursive step: return root if found p or q in tree else return None
def lca(root, p, q):
    if root is None or root == p or root == q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    return root if left and right else left or right

def subtree_with_all_deepest(root):
    def helper(root):
        if root is None:
            return 0, None
        lDepth, lNode = helper(root.left)
        rDepth, rNode = helper(root.right)
        if lDepth > rDepth:
            return lDepth + 1, lNode
        elif lDepth < rDepth:
            return rDepth + 1, rNode
        else:
            return lDepth + 1, root
        return lNode if lDepth > rDepth else rNode
    depth, node = helper(root)
    return node
