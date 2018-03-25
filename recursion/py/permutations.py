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
    cnt = Counter(nums)
    def helper(nums, buf, result):
        if len(buf) == len(nums):
            result.append(list(buf))
            return result

        for num in cnt.keys():
            cnt[num] -= 1
            if cnt[num] == 0:
                del cnt[num]

            buf.append(num)
            helper(nums, buf, result)
            buf.pop()

            cnt[num] += 1
        return result
    return helper(nums, [], [])
