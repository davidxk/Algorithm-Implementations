class StackTraversal:
    # Output after stack push
    def preorderTraversal(self, root):
        stack, cur = [], root
        result = []
        while cur or stack:
            while cur:
                stack.append(cur)
                result.append(cur.val)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return result

    # Output after stack pop
    def inorderTraversal(self, root):
        stack, cur = [], root
        result = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right
        return result

    # Reverse left right, reverse result
    def postorderTraversal(self, root):
        stack, cur = [], root
        result = []
        while cur or stack:
            while cur:
                stack.append(cur)
                result.append(cur.val)
                cur = cur.right
            cur = stack.pop()
            cur = cur.left
        result.reverse()
        return result
