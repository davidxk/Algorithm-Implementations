# Find a subset: n steps, for each element decide to include it or not
# OPT[i][k]: maximum subset sum of a[:i] that is less than or equal to k
# OPT[i][k] = max(OPT[i - 1][k], OPT[i - 1][k - a[i - 1]] + a[i - 1])
# OPT[0][k] = 0
# OPT[i][0] = 0
# return OPT[n][K]
# Time:  O(nK)
# Space: O(nK)
def subset_sum(nums, K):
    OPT = [[0] * (K + 1) for _ in range(len(nums) + 1)]
    for i in range(1, len(nums) + 1):
        for k in range(1, K + 1):
            num = nums[i - 1]
            if k - num < 0:
                OPT[i][k] = OPT[i - 1][k]
            else:
                OPT[i][k] = max(OPT[i - 1][k], OPT[i - 1][k - num] + num)
    return OPT[-1][-1]

def subset_sum_memoization(nums, K):
    def helper(start, K):
        if (start, K) in cache:
            return cache[(start, K)]
        maximum = 0
        for i in range(start, len(nums)):
            if nums[i] <= K:
                maximum = max(nums[i] + helper(i + 1, K - nums[i]), maximum)
        cache[(start, K)] = maximum
        return cache[(start, K)]
    cache = {}
    return helper(0, K)
