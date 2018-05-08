class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def inorderTraversal(self):
        def helper(root, result):
            if root:
                helper(root.left, result)
                result.append(root.val)
                helper(root.right, result)
            return result
        return helper(self.root, [])


class BinarySearchTree(BinaryTree):
    def add(self, target):
        if self.root is None:
            self.root = TreeNode(target)
            return
        root = self.root
        while root:
            prev = root
            if root.val == target:
                return
            elif target < root.val:
                root = root.left
            else:
                root = root.right
        if target < prev.val:
            prev.left = TreeNode(target)
        else:
            prev.right = TreeNode(target)

    def remove(self, target):
        def helper(root, target):
            if root is None:
                return root
            elif target < root.val:
                root.left = helper(root.left, target)
            elif root.val < target:
                root.right = helper(root.right, target)
            else:
                if root.left and root.right:
                    succ = root.right
                    while succ.left:
                        succ = succ.left
                    succ.left = root.left
                    root = root.right
                else:
                    return root.left or root.right
            return root
        # Use right child to take its place, successor to take its left orphan
        self.root = helper(self.root, target)

    def contains(self, target):
        root = self.root
        while root:
            if root.val == target:
                return True
            elif target < root.val:
                root = root.left
            else:
                root = root.right
        return False

    def first(self):
        if not self.root:
            raise KeyError("get first from empty bst")
        root = self.root
        while root.left:
            root = root.left
        return root.val

    def last(self):
        if not self.root:
            raise KeyError("get last from empty bst")
        root = self.root
        while root.right:
            root = root.right
        return root.val

    def ceiling(self, target):
        root = self.root
        ceil = float("inf")
        while root:
            if target == root.val:
                return root.val
            elif target < root.val:
                ceil = root.val
                root = root.left
            else:
                root = root.right
        return ceil

    def floor(self, target):
        root = self.root
        floor = float("-inf")
        while root:
            if target == root.val:
                return root.val
            elif target < root.val:
                root = root.left
            else:
                floor = root.val
                root = root.right
        return floor

    def upper(self, target):
        root = self.root
        upper = float("inf")
        while root:
            if root.val <= target:
                root = root.right
            else: # target < root.val
                if root.val - target < upper - target:
                    upper = root.val
                root = root.left

    def lower(self, target):
        root = self.root
        lower = float("-inf")
        while root:
            if target <= root.val:
                root = root.left
            else: # root.val < target
                if target - root.val < target - lower:
                    lower = root.val
                root = root.right
