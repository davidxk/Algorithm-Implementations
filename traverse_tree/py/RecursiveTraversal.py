class RecursiveTraversal:
    def preorderTraversal(self, root):
        result = []

        def helper(root, result):
            if not root:
                return
            result.append(root.val)
            helper(root.left, result)
            helper(root.right, result)

        helper(root, result)
        return result

    def inorderTraversal(self, root):
        result = []

        def helper(root, result):
            if not root:
                return
            helper(root.left, result)
            result.append(root.val)
            helper(root.right, result)

        helper(root, result)
        return result

    def postorderTraversal(self, root, result = []):
        result = []

        def helper(root, result):
            if not root:
                return
            helper(root.left, result)
            helper(root.right, result)
            result.append(root.val)

        helper(root, result)
        return result
