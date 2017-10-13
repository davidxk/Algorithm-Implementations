import unittest
from random import randrange
from SegmentTree import RMQSegmentTree
from SegmentTree import SumSegmentTree

class TestRMQSegmentTree(unittest.TestCase):
    def testQuery(self, size = 100):
        case = [randrange(100) for i in range(size)]
        rmq = RMQSegmentTree(case)
        for k in range(50):
            i, j = randrange(size/2), randrange(size/2, size)
            minimum = min(case[i: j + 1])
            self.assertEqual(minimum, rmq.query(i, j))

    def testSimpleCase(self):
        self.testQuery(10)

    def testMoreCases(self):
        for i in range(20):
            self.testQuery(randrange(9999))

    def testUpdate(self, size = 100):
        case = [randrange(100) for i in range(size)]
        rmq = RMQSegmentTree(case)
        delta, index = randrange(-150, 50), randrange(100)
        case[index] += delta
        rmq.update(index, delta)
        for k in range(50):
            i, j = randrange(size/2), randrange(size/2, size)
            minimum = min(case[i: j + 1])
            self.assertEqual(minimum, rmq.query(i, j))

    def testUpdateRecursive(self, size = 100):
        case = [randrange(100) for i in range(size)]
        rmq = RMQSegmentTree(case)
        delta, index = randrange(-150, 50), randrange(100)
        case[index] += delta
        rmq.updateRecursive(index, delta)
        for k in range(50):
            i, j = randrange(size/2), randrange(size/2, size)
            minimum = min(case[i: j + 1])
            self.assertEqual(minimum, rmq.query(i, j))
    
    def testRecursive(self):
        for i in range(10):
            self.testUpdateRecursive()

class TestSumSegmentTree(unittest.TestCase):
    def testQuery(self, size = 100):
        case = [randrange(100) for i in range(size)]
        tree = SumSegmentTree(case)
        for k in range(50):
            i, j = randrange(size/2), randrange(size/2, size)
            summation = sum(case[i: j + 1])
            self.assertEqual(summation, tree.query(i, j))

    def testSimpleCase(self):
        self.testQuery(10)

    def testUpdate(self, size = 100):
        case = [randrange(100) for i in range(size)]
        tree = SumSegmentTree(case)
        delta, index = randrange(-50, 50), randrange(100)
        case[index] += delta
        tree.update(index, delta)
        for k in range(50):
            i, j = randrange(size/2), randrange(size/2, size)
            summation = sum(case[i: j + 1])
            self.assertEqual(summation, tree.query(i, j))

if __name__ == '__main__':
    unittest.main()
