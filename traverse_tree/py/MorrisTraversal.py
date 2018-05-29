# First pass by node, next pass by curr, third pass by node again

from TreeNode import TreeNode

class MorrisTraversal:
    # Print before curr move to curr.left
    def preorderTraversal(self, root):
        curr = root
        result = []
        while curr:
            if curr.left is None:
                result.append(curr.val)
                curr = curr.right
            else:
                node = curr.left
                while node.right and node.right != curr:
                    node = node.right

                if node.right is None:
                    node.right = curr
                    result.append(curr.val)
                    curr = curr.left
                else:
                    node.right = None
                    curr = curr.right
        return result

    # Print before curr move to curr.right
    def inorderTraversal(self, root):
        curr = root
        result = []
        while curr:
            if curr.left is None:
                result.append(curr.val)
                curr = curr.right
            else:
                node = curr.left
                while node.right and node.right != curr:
                    node = node.right

                if node.right is None:
                    node.right = curr
                    curr = curr.left
                else:
                    node.right = None
                    result.append(curr.val)
                    curr = curr.right
        return result

    # Print 
    def postorderTraversal(self, root):
        dummy = TreeNode(0)
        dummy.left = root
        curr = dummy
        result = []
        while curr:
            if curr.left is None:
                curr = curr.right
            else:
                node = curr.left
                while node.right and node.right != curr:
                    node = node.right

                if node.right is None:
                    node.right = curr
                    curr = curr.left
                else:
                    result += self.traceBack(curr.left, node)
                    node.right = None
                    curr = curr.right
        return result

    # Print path from node to curr.left
    def traceBack(self, frm, to):
        curr = frm
        result = []
        while curr != to:
            result.append(curr.val)
            curr = curr.right
        result.append(to.val)
        result.reverse()
        return result

#   def preorderTraversal(self, root):
#       curr = root
#       result = []
#       while curr:
#           if curr.left is not None:      # Traverse left subtree of curr
#               last = curr.left           # Find the last node in left subtree
#               while last.right and last.right != curr:
#                   last = last.right      # before moving curr
#               if last.right is None:     # (LNLS: last node in left subtree)
#                   last.right = curr      # Make curr its right child
#                   result.append(curr.val)# So that curr is the last node LNLS
#                   curr = curr.left       # And move curr to the left child
#               else:                      # So upon finishing the left subtree
#                   last.right = None      # curr is again at the root
#                   curr = curr.right      # And find itself the last node LNLS
#           else:                          # So unmake root LNLS and move right
#               result.append(curr.val)    # In the case left subtree not exist
#               curr = curr.right          # Simply move to the right child
#       return result
