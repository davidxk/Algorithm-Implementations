import unittest
from BinarySearchTree import BinarySearchTree
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
        for i in range(100):
            self.setUp()
            target = randrange(2000)
            self.assertEqual(self.bst.contains(target), target in self.array)

    def test_first(self):
        for i in range(100):
            self.setUp()
            self.assertEqual(self.bst.first(), min(self.array))

    def test_last(self):
        for i in range(100):
            self.setUp()
            self.assertEqual(self.bst.last(), max(self.array))

    def test_floor(self):
        self.array = set(self.array)
        for i in range(1000):
            floor = i
            for j in range(1000):
                if i - j in self.array:
                    floor = i - j
                    break
            if i >= self.bst.first():
                self.assertEqual(self.bst.floor(i), floor)

    def test_ceiling(self):
        self.array = set(self.array)
        for i in range(1000):
            ceiling = i
            for j in range(1000):
                if i + j in self.array:
                    ceiling = i + j
                    break
            if i <= self.bst.last():
                self.assertEqual(self.bst.ceiling(i), ceiling)

if __name__ == '__main__':
    unittest.main()
