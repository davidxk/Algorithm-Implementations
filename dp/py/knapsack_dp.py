# OPT[i][k]: subset sum of k in a[:i]
# OPT[i][k] = max(OPT[i - 1][k], OPT[i - 1][k - a[i - 1]] + a[i - 1])
# OPT[0][k] = 0
# OPT[i][0] = 0
# return OPT[n - 1][K]
# Time:  O(kn)
# Space: O(kn)
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
            if nums[i] < K:
                maximum = max(nums[i] + helper(i + 1, K - nums[i]), maximum)
            elif nums[i] == K:
                cache[(start, K)] = K
                return K
        cache[(start, K)] = maximum
        return cache[(start, K)]
    cache = {}
    return helper(0, K)

from collections import defaultdict
def subset_sum_memo_better(nums, K):
    def helper(start, K):
        maximum = 0
        for i in range(start, len(nums)):
            if nums[i] < K:
                args = i + 1, K - nums[i]
                subSol = cache[args] if args in cache else helper(i + 1, K - nums[i])
                maximum = max(nums[i] + subSol, maximum)
            elif nums[i] == K:
                cache[(start, K)] = K
                return K
        cache[(start, K)] = maximum
        return maximum
    cache = {}
    return helper(0, K)

case = [66,90,7,6,32,16,2,78,69,88,85,26,3,9,58,65,30,96,11,31,99,49,63,83,79,97,20,64,81,80,25,69,9,75,23,70,26,71,25,54,1,40,41,82,32,10,26,33,50,71,5,91,59,96,9,15,46,70,26,32,49,35,80,21,34,95,51,66,17,71,28,88,46,21,31,71,42,2,98,96,40,65,92,43,68,14,98,38,13,77,14,13,60,79,52,46,9,13,25,8]
print len(case), sum(case) / 2, len(case) * sum(case) / 2
print subset_sum_memo_better(case, sum(case) / 2)
#print subset_sum_memoization(case, sum(case) / 2)
#print subset_sum(case, sum(case) / 2)

def equal_sum_partition(nums):
    summ = sum(nums)
    half = summ / 2
    return summ % 2 == 0 and subset_sum(nums, half) == half

# OPT[i][m][n]: with (m, n) resources most binary generated in a[:i]
# OPT[i][m][n] = max(OPT[i-1][m][n], OPT[i-1][m - a[i-1][0]][n - a[i-1][1]])
# OPT[0][m][n] = 0
# return OPT[-1][M][N]
# Time:  O(nMN)
# Space: O(nMN)
def zeros_and_ones_explicit(str, M, N):
    OPT = [[[0] * (N+1) for _ in range(M+1)] for _ in range(len(strs)+1)]
    items = []
    for binary in strs:
        zeros = binary.count('0')
        ones = len(binary) - zeros
        items.append((zeros, ones))
    
    for i in range(1, len(items) + 1):
        zeros, ones = items[i - 1]
        for m in range(M + 1):
            for n in range(N + 1):
                if m - zeros < 0 or n - ones < 0:
                    OPT[i][m][n] = OPT[i-1][m][n]
                else:
                    OPT[i][m][n] = max(OPT[i - 1][m][n], \
                        OPT[i - 1][m - zeros][n - ones] + 1)
    return OPT[-1][-1][-1]

# Time:  O(nMN)
# Space: O(2MN)
def zeros_and_ones(str, M, N):
    OPT =  [[0] * (N+1) for _ in range(M+1)]
    items = []
    for binary in strs:
        zeros = binary.count('0')
        ones = len(binary) - zeros
        items.append((zeros, ones))
    
    for i in range(len(items)):
        prev = [list(line) for line in OPT]
        zeros, ones = items[i]
        for m in range(zeros, M + 1):
            for n in range(ones, N + 1):
                OPT[m][n] = max(prev[m][n], prev[m - zeros][n - ones] + 1)
    return OPT[-1][-1]

# Time:  O(nMN)
# Space: O(MN)
def zeros_and_ones_rev_fill(str, M, N):
    OPT = [[0] * (N+1) for _ in range(M+1)]
    items = []
    for binary in strs:
        zeros = binary.count('0')
        ones = len(binary) - zeros
        items.append((zeros, ones))
    
    for i in range(1, len(items) + 1):
        zeros, ones = items[i - 1]
        for m in reversed(range(zeros, M + 1)):
            for n in reversed(range(ones, N + 1)):
                OPT[m][n] = max(OPT[m][n], OPT[m - zeros][n - ones] + 1)
    return OPT[-1][-1]
