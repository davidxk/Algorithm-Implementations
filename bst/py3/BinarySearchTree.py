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
        prev = None
        curr = self.root
        while curr:
            prev = curr
            if curr.val == target:
                return
            elif target < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        if target < prev.val:
            prev.left = TreeNode(target)
        else:
            prev.right = TreeNode(target)

    def remove(self, target):
        # FIXME: Mistyrious performance issue with Py2
        prev = None
        curr = self.root
        while curr and target != curr.val:
            prev = curr
            if target < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        if curr is None:
            return
        if curr.left and curr.right:
            succ = curr.right
            while succ.left:
                succ = succ.left
            succ.left = curr.left
            curr = curr.right
        else:
            curr = curr.left or curr.right
        if prev is None:
            self.root = curr
        elif target < prev.val:
            prev.left = curr
        else:
            prev.right = curr

    def __contains__(self, target):
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

    def higher(self, target):
        root = self.root
        higher = float("inf")
        while root:
            if target == root.val:
                root = root.right
            elif target < root.val:
                higher = root.val
                root = root.left
            else: # root.val < target
                root = root.right
        return higher

    def lower(self, target):
        root = self.root
        lower = float("-inf")
        while root:
            if target == root.val:
                root = root.left
            elif target < root.val:
                root = root.left
            else: # root.val < target
                lower = root.val
                root = root.right
        return lower

    def __iter__(self):
        return BSTIterator(self.root)

class RecursiveImpl(BinarySearchTree):
    def add(self, target):
        def helper(root, target):
            if root is None:
                return TreeNode(target)
            elif target == root.val:
                pass
            elif target < root.val:
                root.left = helper(root.left, target)
            else:
                root.right = helper(root.right, target)
            return root
        self.root = helper(self.root, target)

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

    def __contains__(self, target):
        def helper(root, target):
            if root is None:
                return False
            elif target == root.val:
                return True
            elif target < root.val:
                return helper(root.left, target)
            else:
                return helper(root.right, target)
        return helper(self.root, target)

    def first(self):
        def helper(root):
            if root is None:
                raise KeyError("get first from empty bst")
            elif root.left:
                return helper(root.left)
            else:
                return root.val
        return helper(self.root)

    def last(self):
        def helper(root):
            if root is None:
                raise KeyError("get last from empty bst")
            elif root.right:
                return helper(root.right)
            else:
                return root.val
        return helper(self.root)

class BSTIterator(object):
    def __init__(self, root):
        self.root = root
        self.curr = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr is None:
            self.curr = self.root
            while self.curr.left:
                self.curr = self.curr.left
        elif self.curr.right:
            succ = self.curr.right
            while succ.left:
                succ = succ.left
            self.curr = succ
        else:
            succ = None
            root = self.root
            while self.curr.val != root.val:
                if self.curr.val < root.val:
                    succ = root
                    root = root.left
                else:
                    root = root.right
            self.curr = succ
        if self.curr is None:
            raise StopIteration
        return self.curr
