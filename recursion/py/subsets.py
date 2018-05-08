# Sub-problem: subsets of nums[start:]
# Solution to the subproblem is a part of the solution to the original problem
"""
This recurssion is essentially multiple for loops. e.g. C(3, 5) is equivalent to
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for j in range(j + 1, len(nums)):
            result.append([nums[i], nums[j], nums[k]])
"""
def subsets(nums):
    def helper(start, buf, result):
        result.append(list(buf))
        for i in range(start, len(nums)):
            buf.append(nums[i])
            helper(i + 1, buf, result)
            buf.pop()
        return result
    return helper(0, [], [])

# Some solution to the subproblem are duplicates and should be excluded
"""
With duplicates, C(2, 5) is equivalent to
for i in range(len(nums)):
    if i == 0 or nums[i] != nums[i - 1]:
        for j in range(i + 1, len(nums)):
            if j == i + 1 or nums[j] != nums[j - 1]:
                result.append([nums[i], nums[j]])
"""
def subsetsWithDup(nums):
    def helper(start, buf, result):
        result.append(list(buf))
        for i in range(start, len(nums)):
            if i == start or nums[i] != nums[i - 1]:
                buf.append(nums[i])
                helper(i + 1, buf, result)
                buf.pop()
        return result
    nums.sort()
    return helper(0, [], [])

"""
[[]]
[[], [1]]
[[], [1], [2], [1, 2]]
[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
"""
def subsetsIterative(nums):
    result = [[]]
    for num in nums:
        for subset in results:
            results.append(subset + [num])
    return result

"""
00000100 >> 0 == 0
00000100 >> 1 == 0
00000100 >> 2 == 1
00000100 >> 3 == 0
"""
def subsetsBitManipulation(nums):
    result = [[] for i in nSubs]
    nSubs = 2 ** len(nums)
    for k in range(nSubs):
        for i in range(len(nums)):
            if (k >> i & 1):
                result[k].append(nums[i])
    return result

"""
[000]
[000, 100]
[000, 100, 010, 110]
[000, 100, 010, 110, 001, 101, 0l1, 111]
"""
def bitPermutations(bits):
    result = [bits]
    for i in range(len(bits)):
        for array in result:
            copy = list(array)
            copy[i] = not copy[i]
            result.append(copy)
