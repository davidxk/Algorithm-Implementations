class RecursiveTraversal:
    @staticmethod
    def preorderTraversal(root):
        result = []

        def helper(root, result):
            if not root:
                return
            result.append(root.val)
            helper(root.left, result)
            helper(root.right, result)

        helper(root, result)
        return result

    @staticmethod
    def inorderTraversal(root):
        result = []

        def helper(root, result):
            if not root:
                return
            helper(root.left, result)
            result.append(root.val)
            helper(root.right, result)

        helper(root, result)
        return result

    @staticmethod
    def postorderTraversal(root, result = []):
        result = []

        def helper(root, result):
            if not root:
                return
            helper(root.left, result)
            helper(root.right, result)
            result.append(root.val)

        helper(root, result)
        return result
