# First pass by node, next pass by cur, third pass by node again

from TreeNode import TreeNode

class MorrisTraversal:
    # Print before cur move to cur.left
    def preorderTraversal(self, root):
        cur = root
        result = []
        while cur:
            if cur.left is None:
                result.append(cur.val)
                cur = cur.right
            else:
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right

                if node.right is None:
                    node.right = cur
                    result.append(cur.val)
                    cur = cur.left
                else:
                    node.right = None
                    cur = cur.right
        return result

    # Print before cur move to cur.right
    def inorderTraversal(self, root):
        cur = root
        result = []
        while cur:
            if cur.left is None:
                result.append(cur.val)
                cur = cur.right
            else:
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right

                if node.right is None:
                    node.right = cur
                    cur = cur.left
                else:
                    node.right = None
                    result.append(cur.val)
                    cur = cur.right
        return result

    # Print 
    def postorderTraversal(self, root):
        dummy = TreeNode(0)
        dummy.left = root
        cur = dummy
        result = []
        while cur:
            if cur.left is None:
                cur = cur.right
            else:
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right

                if node.right is None:
                    node.right = cur
                    cur = cur.left
                else:
                    result += self.traceBack(cur.left, node)
                    node.right = None
                    cur = cur.right
        return result

    # Print path from node to cur.left
    def traceBack(self, frm, to):
        cur = frm
        result = []
        while cur != to:
            result.append(cur.val)
            cur = cur.right
        result.append(to.val)
        result.reverse()
        return result
