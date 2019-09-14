import copy
import random
import unittest
from segmented_least_squares import *

def variance(nums):
    avg = sum(nums) / len(nums)
    var = sum(map(lambda elem: (elem - avg) ** 2, nums)) / len(nums)
    return var

def get_all_segmentations(nums):
    def helper(i, buf, result):
        if i == len(nums):
            result.append(copy.deepcopy(buf))
            return result
        if i != 0:
            buf[-1].append(nums[i])
            helper(i + 1, buf, result)
            buf[-1].pop()
        buf.append([nums[i]])
        helper(i + 1, buf, result)
        buf.pop()
        return result
    return helper(0, [], [])

def evaluate_segmentation(e, segmentation, penalty):
    error = 0
    for segement in segmentation:
        error += e(segement) + penalty
    return error

def brute_force_sls(nums, error, penalty):
    return min(evaluate_segmentation(error, segmentation, penalty) \
            for segmentation in get_all_segmentations(nums))

class TestSegmentedLeastSquares(unittest.TestCase):
    def __gen_case__(self):
        nums = []
        nums += [random.randrange(0, 100) for i in range(3)]
        nums += [random.randrange(50, 150) for i in range(3)]
        nums += [random.randrange(100, 200) for i in range(3)]
        nums += [random.randrange(150, 250) for i in range(3)]
        penalty = random.randrange(30, 70)
        return nums, penalty

    def testTableFilling(self):
        for i in range(50):
            nums, penalty = self.__gen_case__()
            min1 = segmented_least_squares(nums, variance, penalty)
            min2 = brute_force_sls(nums, variance, penalty)
            self.assertEqual(min1, min2)

if __name__ == "__main__":
    unittest.main()
