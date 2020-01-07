import unittest
import random
from subset_sum import *

def subsetsSums(nums):
    def helper(start, summ, result):
        result.append(summ)
        for i in range(start, len(nums)):
            helper(i + 1, summ + nums[i], result)
        return result
    return helper(0, 0, [])

def subsetSumHaomo(nums, capacity):
    middle = len(nums) // 2
    left, right = nums[:middle], nums[middle:]
    sumsLeft, sumsRight = subsetsSums(left), subsetsSums(right)
    sumsRight.sort()
    import bisect
    maximum = 0
    for sumLeft in sumsLeft:
        higher = bisect.bisect(sumsRight, capacity - sumLeft)
        if higher == 0:
            continue
        floor = higher - 1
        if sumLeft + sumsRight[floor] > maximum:
            maximum = sumLeft + sumsRight[floor]
    return maximum

class TestSubsetSum(unittest.TestCase):
    def __gen_cases__(self):
        nums = [random.randrange(100) for i in range(25)]
        capacity = random.randrange(sum(nums))
        return nums, capacity

    def testSubsetSum(self):
        for i in range(30):
            nums, capacity = self.__gen_cases__()
            max0 = subsetSumHaomo(nums, capacity)
            max1 = subset_sum(nums, capacity)
            max2 = subset_sum_memoization(nums, capacity)
            self.assertEqual(max0, max1)
            self.assertEqual(max0, max2)

if __name__ == "__main__":
    unittest.main()
