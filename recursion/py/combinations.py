# Combination C(i, n)
"""
Same algorithm with subsets. Only different on stop conditions
"""
def combinations(nums, k):
    def helper(k, start, buf, result):
        if len(buf) == k:
            result.append(list(buf))
            return result
        for i in range(start, len(nums) - (k - len(buf)) + 1):
            buf.append(nums[i])
            helper(k, i + 1, buf, result)
            buf.pop()
        return result
    return helper(k, 0, [], [])

def combinationsWithDup(nums, k):
    def helper(k, start, buf, result):
        if len(buf) == k:
            result.append(list(buf))
            return result
        for i in range(start, len(nums) - (k - len(buf)) + 1):
            if i == start or nums[i] != nums[i - 1]:
                buf.append(nums[i])
                helper(k, i + 1, buf, result)
                buf.pop()
        return result
    return helper(k, 0, [], [])
