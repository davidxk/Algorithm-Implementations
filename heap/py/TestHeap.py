from heap import heapify, heappush, heappop, heappushpop
import unittest
import random

class TestHeap(unittest.TestCase):
    def checkHeapProperty(self, heap):
        for i in range(1, len(heap)):
            parent = (i - 1) / 2
            self.assertGreaterEqual(heap[i], heap[parent])

    def testHeapify(self):
        size = 100
        array = [random.randrange(size) for i in range(size)]
        copy = sorted(array)
        heapify(array)
        self.checkHeapProperty(array)
        for elem in copy:
            self.assertEqual(heappop(array), elem)

    def testHeappush(self):
        size = 100
        array = [random.randrange(size) for i in range(size)]
        copy = sorted(array)
        heap = []
        for elem in array:
            heappush(heap, elem)
        self.checkHeapProperty(heap)
        for elem in copy:
            self.assertEqual(heappop(heap), elem)

    def testHeappushpop(self):
        size = 100
        array = [random.randrange(size) for i in range(size)]
        copy = sorted(array)
        heapify(array)
        self.checkHeapProperty(array)
        for i in range(100):
            elem = random.randrange(size)
            minimum = min(array + [elem])
            self.assertEqual(heappushpop(array, elem), minimum)
            self.assertEqual(len(array), size)
            self.checkHeapProperty(array)

if __name__ == "__main__":
    unittest.main()
