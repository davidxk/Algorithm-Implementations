
def check_balanced(root):
    def helper(root):
        if root is None:
            return 0, True
        lDepth, lIsBalanced = check_balanced(root.left)
        rDepth, rIsBalanced = check_balanced(root.right)
        isBalanced = lIsBalanced and rIsBalanced and (abs(lDepth - rDepth) <= 1)
        depth = max(lDepth, rDepth) + 1
        return depth, isBalanced
    depth, isBalanced = helper(root)
    return isBalanced

def check_bst(root):
    def helper(root, low, high):
        if root is None:
            return True
        if not low < root.val < high:
            return False
        return helper(root.left, low, root.val) and helper(root.right, root.val, high)
    return helper(root, -float("inf"), float("inf"))

def check_symmetric(root):
    def helper(root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None or root1.val != root2.val:
            return False
        return helper(root1.left, root2.right) and helper(root1.right, root2.left)
    if root is None:
        return True
    return helper(root.left, root.right)
