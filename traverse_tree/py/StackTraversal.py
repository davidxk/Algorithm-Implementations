class StackTraversal:
    # Output after stack push
    @staticmethod
    def preorderTraversal(root):
        curr, stack = root, []
        result = []
        while curr or stack:
            while curr:
                result.append(curr.val)
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            curr = curr.right
        return result

    # Output after stack pop
    @staticmethod
    def inorderTraversal(root):
        curr, stack = root, []
        result = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result

    # Store call stack with context, output after second visit
    @staticmethod
    def postorderTraversal(root):
        curr, stack = root, []
        result = []
        while curr or stack:
            while curr:
                stack.append([curr, False])
                curr = curr.left
            top = stack[-1]
            if top[1] is False:
                top[1] = True;
                curr = top[0].right
            else:
                result.append(top[0].val)
                stack.pop()
        return result

    # DFS style only possible for preorder since the root cannot be revisited
    @staticmethod
    def dfsPreorderTraversal(root):
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    # Reverse left right, reverse result of preorder
    @staticmethod
    def psudoPostorderTraversal(root):
        curr, stack = root, []
        result = []
        while curr or stack:
            while curr:
                stack.append(curr)
                result.append(curr.val)
                curr = curr.right
            curr = stack.pop()
            curr = curr.left
        result.reverse()
        return result

#   def stackVsRecursive(root):           def helper(root, result):
#       curr, stack = root, []
#       result = []
#       while curr or stack:
#           while curr:                             if root:
#               stack.append([curr, False])             # build call stack
#               curr = curr.left                        helper(root.left)
#           top = stack[-1]                             # --> back here
#           if top[1] is False:                         # now curr is None
#               top[1] = True                           # save running context
#               curr = top[0].right                     helper(root.right)
#           else:                                       # --> right here
#               result.append(top[0].val)               result.append(root.val)
#               stack.pop()                             # destroy call stack
#       return result                                   return
