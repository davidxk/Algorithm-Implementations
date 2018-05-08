class StackTraversal:
    # Output after stack push
    def preorderTraversal(self, root):
        stack, curr = [], root
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
    def inorderTraversal(self, root):
        stack, curr = [], root
        result = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result

    # Reverse left right, reverse result of preorder
    def psudoPostorderTraversal(self, root):
        stack, curr = [], root
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

    # Store call stack with context, output after second visit
    def postorderTraversal(self, root):
        stack, curr = [], root
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

#   def stackVsRecursive(self, root):           def helper(root, result):
#       stack, curr = [], root
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
