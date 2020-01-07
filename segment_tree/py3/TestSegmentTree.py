import unittest
from random import randrange
from SegmentTree import RMQSegmentTree
from SegmentTree import RSQSegmentTree

class TestRMQSegmentTree(unittest.TestCase):
    def testQuery(self, size = 100):
        case = [randrange(100) for i in range(size)]
        rmq = RMQSegmentTree(case)
        for k in range(50):
            i, j = randrange(size//2), randrange(size//2, size)
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
        delta, index = randrange(-150, 50), randrange(size)
        case[index] += delta
        rmq.update(index, delta)
        for k in range(50):
            i, j = randrange(size//2), randrange(size//2, size)
            minimum = min(case[i: j + 1])
            self.assertEqual(minimum, rmq.query(i, j))

    def testRecursiveUpdate(self, size = 100):
        case = [randrange(100) for i in range(size)]
        rmq = RMQSegmentTree(case)
        delta, index = randrange(-150, 50), randrange(size)
        case[index] += delta
        rmq.recursiveUpdate(index, delta)
        for k in range(50):
            i, j = randrange(size//2), randrange(size//2, size)
            minimum = min(case[i: j + 1])
            self.assertEqual(minimum, rmq.query(i, j))
    
    def testRecursive(self):
        for i in range(10):
            self.testRecursiveUpdate()

class TestRSQSegmentTree(unittest.TestCase):
    def testQuery(self, size = 100):
        case = [randrange(100) for i in range(size)]
        rsq = RSQSegmentTree(case)
        for k in range(50):
            i, j = randrange(size//2), randrange(size//2, size)
            summation = sum(case[i: j + 1])
            self.assertEqual(summation, rsq.query(i, j))

    def testSimpleCase(self):
        self.testQuery(10)

    def testUpdate(self, size = 100):
        case = [randrange(100) for i in range(size)]
        rsq = RSQSegmentTree(case)
        delta, index = randrange(-50, 50), randrange(size)
        case[index] += delta
        rsq.update(index, delta)
        for k in range(50):
            i, j = randrange(size//2), randrange(size//2, size)
            summation = sum(case[i: j + 1])
            self.assertEqual(summation, rsq.query(i, j))

    def testRangeUpdate(self, size = 100, scale = 100, nUpdate = 10):
        case = [randrange(scale) for i in range(size)]
        rsq = RSQSegmentTree(case)
        for i in range(nUpdate):
            delta = randrange(-scale//2, scale//2)
            left, right = randrange(size//2), randrange(size//2, size)
            for i in range(left, right + 1):
                case[i] += delta
            rsq.rangeUpdate(left, right, delta)
        for k in range(50):
            i, j = randrange(size//2), randrange(size//2, size)
            summation = sum(case[i: j + 1])
            self.assertEqual(summation, rsq.query(i, j))

    def testRange(self):
        for i in range(20):
            self.testRangeUpdate(10, 10, 1)
        for i in range(20):
            self.testRangeUpdate()

if __name__ == '__main__':
    unittest.main()
