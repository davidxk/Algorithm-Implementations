from TreeNode import *
from collections import deque
import random
import unittest

from StackTraversal import StackTraversal
from MorrisTraversal import MorrisTraversal
from RecursiveTraversal import RecursiveTraversal

class TestTraversal(unittest.TestCase):
    def __random_tree__(self, size):
        pool = set( [str(i) for i in range(size)] )
        cnt = 1
        root = TreeNode( pool.pop() )
        queue = deque([root])
        while queue and cnt < size:
            node = queue.popleft()
            if pool and (random.random() < 0.7 or not queue):
                node.left = TreeNode( pool.pop() )
                queue.append( node.left )
            if pool and (random.random() < 0.7 or not queue):
                node.right = TreeNode( pool.pop() )
                queue.append( node.right )
            cnt += 1
        return root

    def __testTraversalMethod__(self, impl, size = 100, case = None):
        root = case or self.__random_tree__(size)
        tag = ["preorder", "inorder", "postorder"]

        ans = [0 for i in range(3)]
        ans[0] = RecursiveTraversal.preorderTraversal(root)
        ans[1] = RecursiveTraversal.inorderTraversal(root)
        ans[2] = RecursiveTraversal.postorderTraversal(root)

        ret = [0 for i in range(3)]
        ret[0] = impl.preorderTraversal(root)
        ret[1] = impl.inorderTraversal(root)
        ret[2] = impl.postorderTraversal(root)

        self.assertEqual(ans[0], ret[0])
        self.assertEqual(ans[1], ret[1])
        self.assertEqual(ans[2], ret[2])

    def __testOtherMethods__(self, size = 100):
        root = self.__random_tree__(size)
        tag = ["preorder", "inorder", "postorder"]

        ans = [0 for i in range(3)]
        ans[0] = RecursiveTraversal.preorderTraversal(root)
        ans[1] = RecursiveTraversal.inorderTraversal(root)
        ans[2] = RecursiveTraversal.postorderTraversal(root)

        ret = [0 for i in range(3)]
        ret[0] = StackTraversal.dfsPreorderTraversal(root)
        ret[1] = StackTraversal.inorderTraversal(root)
        ret[2] = StackTraversal.psudoPostorderTraversal(root)

        self.assertEqual(ans[0], ret[0])
        self.assertEqual(ans[1], ret[1])
        self.assertEqual(ans[2], ret[2])

    def testStackTraversal(self):
        for i in range(100):
            self.__testTraversalMethod__(StackTraversal, 200)

    def testMorrisTraversal(self):
        for i in range(100):
            self.__testTraversalMethod__(MorrisTraversal, 200)

    def testOtherMethods(self):
        for i in range(100):
            self.__testOtherMethods__()

if __name__ == '__main__':
    unittest.main()
