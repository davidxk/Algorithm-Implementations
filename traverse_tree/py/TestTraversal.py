from TreeNode import *
from random import *
from collections import deque

class TestTraversal:
    def generate_random_tree(self, size):
        pool = set( [str(i) for i in range(size)] )
        cnt = 1
        root = TreeNode( pool.pop() )
        queue = deque([root])
        while queue and cnt < size:
            node = queue.popleft()
            if random() < 0.7:
                node.left = TreeNode( pool.pop() )
                queue.append( node.left )
            if random < 0.7 or not queue:
                node.right = TreeNode( pool.pop() )
                queue.append( node.right )
            cnt += 1
        return root

    def test_traversal_method(self, impl, size = 100, case = None):
        root = case or self.generate_random_tree(size)
        tag = ["preorder", "inorder", "postorder"]

        ans = [0 for i in range(3)]
        ans[0] = RecursiveTraversal().preorderTraversal(root)
        ans[1] = RecursiveTraversal().inorderTraversal(root)
        ans[2] = RecursiveTraversal().postorderTraversal(root)

        ret = [0 for i in range(3)]
        ret[0] = impl.preorderTraversal(root)
        ret[1] = impl.inorderTraversal(root)
        ret[2] = impl.postorderTraversal(root)

        for i in range(3):
            if ret[i] != ans[i]:
                print tag[i], "error: "
                print "returned: ", ret[i]
                print "expected: ", ans[i]
        
        return ret == ans



from StackTraversal import StackTraversal
from MorrisTraversal import MorrisTraversal
from RecursiveTraversal import RecursiveTraversal

if __name__ == '__main__':
    for impl in [StackTraversal(), MorrisTraversal()]:
        print "Testing", impl
        cases = 500
        for i in range(cases):
            if not TestTraversal().test_traversal_method(impl, 200):
                print "WA: ", impl
