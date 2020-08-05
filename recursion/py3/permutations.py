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

# In-place solution
# To iterate through distinct elements in the array, the right-hand side must
# always be kept in sorted order. To achieve this, always exchange the current
# number at index [0] with the leftmost next greater element in the array.
# Note: The swap during the recursion MUST NOT be undone.
"""
[1   1 2 2 3 3 3 4 4 4]
 ^     ^
[2   1 1 2 3 3 3 4 4 4]
 ^         ^
[3   1 1 2 2 3 3 4 4 4]
 ^               ^
[4   1 1 2 2 3 3 3 4 4]
"""
def permutationsWithDup(nums):
    def helper(nums, start, result):
        if start == len(nums):
            result.append(nums)
            return result
        for i in range(start, len(nums)):
            if i == start or nums[i] != nums[start]:
                nums[i], nums[start] = nums[start], nums[i]
                helper(list(nums), start + 1, result)
        return result
    nums.sort()
    return helper(nums, 0, [])

# Counter solution
# Time:  O(n)
# Space: O(distinct nums)
from collections import Counter
def permsDedupCounter(nums):
    def helper(buf, result):
        if len(buf) == len(nums):
            result.append(list(buf))
            return result
        for num in cnt.keys():
            if cnt[num] > 0:
                buf.append(num)
                cnt[num] -= 1
                helper(buf, result)
                cnt[num] += 1
                buf.pop()
        return result
    cnt = Counter(nums)
    return helper([], [])

# Array solution
# Time:  O(n log n)
# Space: O(n)
#
# [1 1 1 2]
#
# First recursion call branch
# 1       -> 1 1 1 2 (i-equals-zero)
#            u
# 1 1     -> 1 1 1 2 (next-in-line)
#            u u
# 1 1 1   -> 1 1 1 2 (next-in-line)
#            u u u
# 1 1 1 2 -> 1 1 1 2 (first-in-group)
#            u u u u
#
# Top level iterations
# 1:        if block (i-equals-zero)
# 1:      else block (prev-not-used)
# 1:      else block (prev-not-used)
# 2:        if block (first-in-group)
def permsDedupArray(nums):
    def helper(used, buf, result):
        if len(buf) == len(nums):
            result.append(list(buf))
            return result
        for i in range(len(nums)):
            '''There are easy-to-write-hard-to-understand ways to write this'''
            firstInGroup = (i == 0) or (i > 0 and nums[i - 1] != nums[i])
            nextInLine = (i > 0 and nums[i - 1] == nums[i] and used[i - 1])
            if not used[i] and (firstInGroup or nextInLine):
                buf.append(nums[i])
                used[i] = True
                helper(used, buf, result)
                used[i] = False
                buf.pop()
        return result
    used = [False] * len(nums)
    nums.sort()
    return helper(used, [], [])
