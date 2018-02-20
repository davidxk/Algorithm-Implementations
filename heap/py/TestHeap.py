from heap import heapify, heappush, heappop
import unittest
import random

class TestHeap(unittest.TestCase):
    def testHeapify(self):
        array = [random.randrange(100) for i in range(100)]
        copy = sorted(array)
        heapify(array)
        for elem in copy:
            self.assertEqual(heappop(array), elem)

    def testHeappush(self):
        array = [random.randrange(100) for i in range(100)]
        copy = sorted(array)
        heap = []
        for elem in array:
            heappush(heap, elem)
        for elem in copy:
            self.assertEqual(heappop(heap), elem)

if __name__ == "__main__":
    unittest.main()
