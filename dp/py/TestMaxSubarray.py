import random
import itertools
import unittest
from max_subarray import *

class TestMaxSubarray(unittest.TestCase):
    def setUp(self):
        size = 500;
        self.array = [random.randrange(-size, size) for i in range(size)]

    def naiveMaxSubarray(self, array):
        presum = list(array)
        for i in range(1, len(array)):
            presum[i] += presum[i - 1]
        presum = [0] + presum
        subsums = [presum[j] - presum[i]
                for i, j in itertools.combinations(range(len(presum)), 2)]
        return max(subsums)

    def testMaxSubarray(self):
        for i in range(50):
            retval = maximum_subarray(self.array)
            expect = self.naiveMaxSubarray(self.array)
            self.assertEqual(retval, expect)

if __name__ == "__main__":
    unittest.main()
