# ~ House Robber ~
# OPT[i]: maximum gold robbed of houses [0, i]
# OPT[i] = max(OPT[i - 1], OPT[i - 2] + a[i])
# OPT[0] = a[0]
# OPT[1] = max(a[0], a[1])
# return OPT[n - 1]
# Time:  O(n)
# Space: O(n)
def house_robber_explicit(nums):
    n = len(nums)
    OPT = [0] * len(nums)
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    OPT[0] = nums[0]
    OPT[1] = max(nums[0], nums[1])
    for i in range(2, n):
        OPT[i] = max(OPT[i - 1], OPT[i - 2] + nums[i])
    return OPT[n - 1]

# Time:  O(n)
# Space: O(1)
def house_robber(nums):
    "No need to init OPT[0] OPT[1] since OPT[-1] OPT[-2] also follow the rule"
    pprev = prev = OPT = 0
    for i in range(len(nums)):
        pprev, prev = prev, OPT
        OPT = max(prev, pprev + nums[i])
    return OPT

# ~ House Robber II ~
# OPT[?][i]: maximum gold robbed of houses [0, i] given whether rob the first
# OPT[?][i] = max(OPT[?][i - 1], OPT[?][i - 2] + a[i])
# OPT[T][0] = a[0] OPT[T][1] = a[0]
# OPT[F][0] = 0    OPT[F][1] = a[1]
# return max(OPT[T][n - 1], OPT[F][n - 1])
# Time:  O(2n)
# Space: O(2n)
def house_robber_ii_explicit(nums):
    n = len(nums)
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    OPT = [[0] * n for i in range(2)]
    OPT[False][0] = 0
    OPT[False][1] = nums[1]
    for i in range(2, n):
        OPT[False][i] = max(OPT[False][i - 1], OPT[False][i - 2] + nums[i])

        OPT[True][0] = nums[0]
        OPT[True][1] = nums[0]
        for i in range(2, n - 1):
            OPT[True][i] = max(OPT[True][i - 1], OPT[True][i - 2] + nums[i])
        return max(OPT[True][n - 2], OPT[False][n - 1])

# Time:  O(2n)
# Space: O(1)
def house_robber_ii(nums):
    if not nums:
        return 0
    result = []
    # Rob first
    pprev, prev, OPT = 0, 0, nums[0]
    for i in range(1, len(nums) - 1):
        pprev, prev = prev, OPT
        OPT = max(prev, pprev + nums[i])
    result.append(OPT)
    # No rob first
    pprev, prev, OPT = 0, 0, 0
    for i in range(1, len(nums)):
        pprev, prev = prev, OPT
        OPT = max(prev, pprev + nums[i])
    result.append(OPT)
    return max(result)

# ~ Delete and Earn ~
# Reduce to House Robber
def delete_and_earn(nums):
    count = [0] * 10000
    for num in nums:
        count[num] += num
    pprev, prev, OPT = 0, 0, 0
    for cnt in count:
        pprev, prev = prev, OPT
        OPT = max(prev, pprev + cnt)
    return OPT
