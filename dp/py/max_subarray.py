# Kadane's algorithm
# ~ $Maximum Subarray$ ~
# OPT[i]: maximum subarray ending with a[i]
# OPT[i] = max(OPT[i - 1], 0) + a[i]
# OPT[0] = a[0]
# return max(OPT)

# Time:  O(n)
# Space: O(n)
def maximum_subarray_explicit(array):
    """ Kadane """
    OPT = [0] * len(array)
    OPT[0] = array[0]
    for i in range(1, len(nums)):
        OPT[i] = max(OPT[i - 1], 0) + array[i]
    return max(OPT)

# Time:  O(n)
# Space: O(1)
def maximum_subarray(nums):
    OPT_i, maximum = None, None
    for num in nums:
        OPT_i = max(OPT_i, 0) + num
        maximum = max(OPT_i, maximum)
    return maximum

# Circular Maximum Subarray
# Negate the original array and call Kadane. Corner case must be considered.
# Time:  O(n)
# Space: O(1)
def circular_maximum_subarray(nums):
    normal = maximum_subarray(nums)
    negated = map(lambda x: -x, nums)
    wrapped = sum(nums) + maximum_subarray(negated)
    if wrapped is 0:
        return normal
    return max(normal, wrapped)

# k Maximum Subarray (at most k-1 gaps allowed)
# For each number, there is a choice of going to the first the second or neither
# OPT[k][i]: k maximum subarray of a [0, i] 
# OPT[k][i] = max(OPT[k][i - 1], sum(a [j + 1, i]) + OPT[k - 1][j]), j < i
# OPT[0][i] = 0
# OPT[k][0] = max(0, a[0])
# return OPT[2][-1]
"""
# Straightfoward, but time-consuming and does not conform to the above setup
# Time:  O(N^3)
# Space: O(KN)
def k_maximum_subarray(nums, K):
    OPT = [[0] * (len(nums) + 1) for k in range(K + 1)]
    sums = list(nums)
    for i in range(1, len(nums)):
        sums[i] += sums[i - 1]
    for k in range(1, K + 1):
        for i in range(1, len(nums) + 1):
            sumRange = lambda j, i: sums[i - 1] - (sums[j - 1] if j > 0 else 0)
            maximum = max(sumRange(j, i) + OPT[k - 1][j] for j in range(i))
            OPT[k][i] = max(OPT[k][i - 1], maximum)
    return OPT[K][-1]
"""

# OPT[k][i] = max(OPT[k][i-1], sum(a [j + 1, i]) + OPT[k-1][j]),      j < i
#           = max(OPT[k][i-1], sums[i] - sums[j] + OPT[k-1, j]),      j < i
#           = max(OPT[k][i-1], sums[i] + max(OPT[k-1, j] - sums[j])), j < i
# Time:  O(N^2)
# Space: O(KN)
def k_maximum_subarray_explicit(nums, K):
    OPT = [[0] * len(nums) for k in range(K + 1)]
    sums = list(nums)
    for i in range(1, len(nums)):
        sums[i] += sums[i - 1]
    for k in range(1, K + 1):
        tmpMax = 0
        for i in range(len(nums)):
            OPT[k][i] = max(OPT[k][i - 1], tmpMax + sums[i])
            tmpMax = max(tmpMax, OPT[k - 1][i] - sums[i])
    return OPT[K][-1]

# Time:  O(N^2)
# Space: O(N)
def k_maximum_subarray(nums, K):
    OPT = [[0] * len(nums) for k in range(2)]
    sums = list(nums)
    for i in range(1, len(nums)):
        sums[i] += sums[i - 1]
    for k in range(1, K + 1):
        tmpMax = 0
        for i in range(len(nums)):
            OPT[k % 2][i] = max(OPT[k % 2][i - 1], tmpMax + sums[i])
            tmpMax = max(tmpMax, OPT[(k - 1) % 2][i] - sums[i])
    return OPT[K % 2][-1]

# Maximum Subarray with gap penalty
# OPT[i]: maximum subarray of a [0, i]
# OPT[i] = max(OPT[i - 1], OPT[j - cd] + sum(a [j + 1, i])),          j < i
#        = max(OPT[i - 1], OPT[j - cd] + sums[i] - sums[j])),         j < i
#        = max(OPT[i - 1], max(OPT[j - cd] - sums[j]) + sums[i])
# OPT[0] = a[0]
# return OPT[n]
# Time:  O(n)
# Space: O(n)
def maximum_subarray_cooldown(nums, cd):
    OPT = [0] * len(nums)
    sums = list(nums)
    for i in range(1, len(nums)):
        sums[i] += sums[i - 1]
    tmpMax = 0
    for i in range(len(nums)):
        OPT[i] = max(OPT[i - 1], sums[i] + tmpMax)
        OPT_p = OPT[i - cd] if i - cd >= 0 else 0
        tmpMax = max(tmpMax, OPT_p - sums[i])
    return OPT[-1]

# Maximum Subarrays with fee
# OPT[i]: maximum sums of a[0, i]
# OPT[i] = max(OPT[i - 1], OPT[j - 1] - fee + sum(a [j + 1, i])) 1 <= j <= i - 1
#        = max(OPT[i - 1], OPT[j - 1] - fee + sums[i] - sums[j])
#        = max(OPT[i - 1], max(OPT[j - 1] - sums[j] - fee) + sums[i])
# OPT[0] = max(0, a[0] - fee)
# OPT[1] = OPT[0] + max(0, a[1])
# return OPT[n - 1]
# Time:  O(n)
# Space: O(n)
def maximum_subarray_fee(nums, fee):
    OPT = [0] * len(nums)
    sums = list(nums)
    for i in range(1, len(nums)):
        sums[i] += sums[i - 1]
    tmpMax = max(- fee - sums[0], -fee)
    OPT[0] = max(0, nums[0] - fee)
    for i in range(1, len(nums)):
        OPT[i] = max(OPT[i - 1], tmpMax + sums[i])
        tmpMax = max(tmpMax, OPT[i - 1] - sums[i] - fee)
    return OPT[-1]
