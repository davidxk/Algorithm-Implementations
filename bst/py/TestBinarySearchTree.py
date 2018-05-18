import unittest
from BinarySearchTree import *
from bisect import bisect, bisect_left
from random import randrange

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()
        self.array = [randrange(1000) for i in range(1000)] 
        for num in self.array:
            self.bst.add(num)

    def tearDown(self):
        self.bst = None

    def test_add(self):
        for i in range(100):
            traverse = self.bst.inorderTraversal()
            self.array = sorted(set(self.array))
            self.assertEqual(traverse, self.array, "bst.add incorrect")
            self.setUp()

    def test_remove(self):
        for i in range(100):
            for num in self.array:
                self.bst.remove(num)
            traverse = self.bst.inorderTraversal()
            self.assertEqual(traverse, [], "bst remove all test fail")
            self.setUp()

        for i in range(100):
            self.array = set(self.array)
            for i in range(50):
                num = self.array.pop()
                self.bst.remove(num)
            traverse = self.bst.inorderTraversal()
            self.array = sorted(self.array)
            self.assertEqual(traverse, self.array, "bst.remove incorrect")
            self.setUp()

    def test_contains(self):
        numset = set(self.array)
        for target in range(len(self.array)):
            self.assertEqual(target in self.bst, target in numset)

    def test_first(self):
        for i in range(100):
            self.setUp()
            self.assertEqual(self.bst.first(), min(self.array))

    def test_last(self):
        for i in range(100):
            self.setUp()
            self.assertEqual(self.bst.last(), max(self.array))

    def test_floor(self):
        self.array.sort()
        for target in range(len(self.array)):
            idx = bisect_left(self.array, target)
            if idx < len(self.array) and self.array[idx] == target:
                floor = target
            elif idx == 0:
                floor = float("-inf")
            else:
                floor = self.array[idx - 1]
            self.assertEqual(self.bst.floor(target), floor)

    def test_ceiling(self):
        self.array.sort()
        for target in range(len(self.array)):
            idx = bisect(self.array, target)
            if idx > 0 and self.array[idx - 1] == target:
                ceiling = target
            elif idx == len(self.array):
                ceiling = float("inf")
            else:
                ceiling = self.array[idx]
            self.assertEqual(self.bst.ceiling(target), ceiling)

    def test_lower(self):
        self.array.sort()
        for i in range(len(self.array)):
            x = self.array[i]
            for j in range(i - 1, -1, -1):
                if self.array[j] < x:
                    lower = self.array[j]
                    break
            else:
                lower = float("-inf")
            self.assertEqual(self.bst.lower(x), lower)

    def test_higher(self):
        self.array.sort()
        for i in range(len(self.array)):
            x = self.array[i]
            for j in range(i + 1, len(self.array)):
                if self.array[j] > x:
                    higher = self.array[j]
                    break
            else:
                higher = float("inf")
            self.assertEqual(self.bst.higher(x), higher)

    def test_iter(self):
        it = iter(self.bst)
        nums = self.bst.inorderTraversal()
        for num in nums:
            self.assertEqual(num, next(it).val)

if __name__ == '__main__':
    unittest.main()
