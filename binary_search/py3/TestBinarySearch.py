from binary_search import *
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
            ret1 = binary_search(self.array, target)
            target_is_gt = lambda i: self.array[i] < target
            ret2 = general_binary_search(0, len(self.array) - 1, target_is_gt)
            target_is_ge = lambda i: self.array[i] <= target
            ret3 = general_binary_search2(0, len(self.array) - 1, target_is_ge)
            if 0 <= ret1 < len(self.array):
                self.assertEqual(self.array[ret1], target)
                self.assertEqual(self.array[ret2], target)
                self.assertEqual(self.array[ret3], target)
            else:
                self.assertEqual(ret1, -1)
                self.assertTrue(ret2 == 0 or ret2 == len(self.array) - 1)
                self.assertTrue(target < self.array[0] or self.array[-1] < target)

if __name__ == '__main__':
    unittest.main()
