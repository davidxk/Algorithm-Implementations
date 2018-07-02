from binary_search import binary_search, lower, higher, equal_range
import bisect
import unittest
import random

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.times = 100
        self.size = 30000
        self.array = [random.randrange(self.size) for i in range(self.size)]
        self.array.sort()

    def test_equal_range(self):
        for i in range(self.times):
            target = random.randrange(int(self.size * 1.10))
            retval = equal_range(self.array, target) 
            left = bisect.bisect_left(self.array, target)
            if 0 <= left < len(self.array) and self.array[left] == target:
                right = bisect.bisect(self.array, target) - 1
            else:
                left = right = -1
            self.assertEqual(retval, (left, right))

    def test_higher(self):
        for i in range(self.times):
            target = random.randrange(int(self.size * 1.10))
            retval = higher(self.array, target) 
            expect = bisect.bisect(self.array, target)
            self.assertEqual(retval, expect)

    def test_lower(self):
        for i in range(self.times):
            target = random.randrange(int(self.size * 1.10))
            retval = lower(self.array, target) 
            expect = bisect.bisect_left(self.array, target) - 1
            self.assertEqual(retval, expect)

    def test_binary_search(self):
        self.array = [i for i in range(self.size)]
        for i in range(self.times):
            target = random.randrange(int(self.size * 1.10))
            retval = binary_search(self.array, target) 
            if 0 <= retval < len(self.array):
                self.assertEqual(self.array[retval], target)
            else:
                self.assertEqual(retval, -1)
                self.assertTrue(target < self.array[0] or self.array[-1] < target)

if __name__ == '__main__':
    unittest.main()
