import unittest
import random
from HashSet import HashSet

class TestHashSet(unittest.TestCase):
    def setUp(self):
        self.size = 1000
        self.array = {random.randrange(self.size) for i in range(self.size)}
        self.set = HashSet()
        for elem in self.array:
            self.set.add(elem)

    def testAdd(self):
        self.array = range(self.size)
        self.set = HashSet()
        for i, elem in enumerate(self.array):
            self.assertEqual(len(self.set), i)
            self.set.add(elem)
        self.assertEqual(len(self.set), len(self.array))

    def testContains(self):
        for elem in self.array:
            self.assertTrue(elem in self.set)

    def testRemove(self):
        for i, elem in enumerate(self.array):
            self.assertTrue(elem in self.set)
            self.assertEqual(len(self.array) - i, len(self.set))
            self.set.remove(elem)
            self.assertEqual(len(self.array) - i - 1, len(self.set))
            self.assertFalse(elem in self.set)
    
    def testClear(self):
        self.set.clear()
        for elem in self.array:
            self.assertFalse(elem in self.set)
        self.assertEqual(len(self.set), 0)

if __name__ == '__main__':
    unittest.main()
