from BinaryIndexedTree import BinaryIndexedTree
from random import randrange
import unittest

class TestBinaryIndexedTree(unittest.TestCase):
    def testGetSum(self):
        array = [randrange(100) for i in range(100)]
        bit = BinaryIndexedTree(array)
        for cnt in range(100):
            i = randrange(100)
            summation = 0
            for k in range(i + 1):
                summation += array[k]
            self.assertEqual(summation, bit.getSum(i))

    def testUpdate(self):
        array = [randrange(100) for i in range(100)]
        bit = BinaryIndexedTree(array)
        for cnt in range(100):
            index, delta = randrange(100), randrange(-50, 50)
            array[index] += delta
            bit.update(index, delta)
            i = randrange(100)
            summation = 0
            for k in range(i + 1):
                summation += array[k]
            self.assertEqual(summation, bit.getSum(i))

    def testGetRange(self):
        array = [randrange(100) for i in range(100)]
        bit = BinaryIndexedTree(array)
        for cnt in range(100):
            i, j = randrange(50), randrange(50, 100)
            summation = 0
            for k in range(i, j + 1):
                summation += array[k]
            self.assertEqual(summation, bit.getRange(i, j))

    def testBasic(self):
        array = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
        bit = BinaryIndexedTree(array)
        expected = [0, 2, 3, 1, 7, 2, 5, 4, 21, 6, 13, 8, 30]
        self.assertEqual(bit.tree, expected)

if __name__ == '__main__':
    unittest.main()
