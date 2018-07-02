# All permuations of an array A(n, n)
# Give a chance to each element to be at the front, and the rest is recurrsion
"""
[1  (2 3 4)]
[2  (1 3 4)]
[3  (2 1 4)]
[4  (2 3 1)]
"""
def permutations(nums):
    def helper(start, result):
        if start == len(nums):
            result.append(list(nums))
            return result
        for i in range(start, len(nums)):
            nums[i], nums[start] = nums[start], nums[i]
            helper(start + 1, result)
            nums[i], nums[start] = nums[start], nums[i]
        return result
    return helper(0, [])

"""
[1  (1 2 3)]
[2  (1 1 3)]
[3  (1 2 1)]
"""
from collections import Counter
def permutationsWithDup(nums):
    def helper(nums, start, result):
        if start == len(nums):
            result.append(nums)
            return result
        for i in range(start, len(nums)):
            if i == start or nums[i] != nums[start]:
                nums[i], nums[start] = nums[start], nums[i]
                helper(list(nums), start + 1, result)
                #nums[i], nums[start] = nums[start], nums[i]
        return result
    return helper(nums, 0, [])
