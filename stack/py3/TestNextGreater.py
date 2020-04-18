import unittest
import random
from next_greater import *

class TestNextGreater(unittest.TestCase):
    def __gen_case__(self):
        return [random.randrange(70) for i in range(100)]

    def naiveNextGreater(self, nums):
        greater = [float("inf")] * len(nums)
        for i, num in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    greater[i] = nums[j]
                    break
        return greater

    def naiveNextGtLastGe(self, nums):
        nGt = self.naiveNextGreater(nums)
        lGe = [float("inf")] * len(nums)
        for i, num in enumerate(nums):
            for j in range(i - 1, -1, -1):
                if nums[j] >= nums[i]:
                    lGe[i] = nums[j]
                    break
        return nGt, lGe

    def testNextGreater(self):
        for _ in range(100):
            nums = self.__gen_case__()
            g1 = self.naiveNextGreater(nums)
            g2 = next_greater(nums)
            g3 = next_greater_reverse(nums)
            self.assertEqual(g1, g2)
            self.assertEqual(g1, g3)

    def testCombined(self):
        for _ in range(100):
            nums = self.__gen_case__()
            nGt1, lGe1 = self.naiveNextGtLastGe(nums)
            nGt2, lGe2 = next_gt_last_ge(nums)
            self.assertEqual(nGt1, nGt2)
            self.assertEqual(lGe1, lGe2)

if __name__ == "__main__":
    unittest.main()
