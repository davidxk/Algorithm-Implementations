# Notation: array [1, i] <==> array[1: i + 1]

# ~ $Maximum Subarray$ ~
# OPT[i]: maximum subarray ending with a[i]
# OPT[i] = max(OPT[i - 1], 0) + a[i]
# OPT[0] = a[0]
# return max(OPT)

# Time:  O(n)
# Space: O(n)
def maximum_subarray_explicit(array):
    OPT = [0] * len(array)
    OPT[0] = array[0]
    for i in range(1, len(nums)):
        OPT[i] = max(OPT[i - 1], 0) + array[i]
    return max(OPT)

# ~ Climbing Stairs ~
# Essentially Fibonacci
# OPT[i]: how many ways to climb to the ith step
# OPT[i] = OPT[i - 1] + OPT[i - 2]
# OPT[1] = 1
# OPT[2] = 2
# return OPT[n]
# Time:  O(n)
# Space: O(n)
def climb_stairs_explicit(n):
    OPT = [0] * (n + 1)
    OPT[0] = OPT[1] = 1
    for i in range(2, n + 1):
        OPT[i] = OPT[i - 1] + OPT[i - 2]
    return OPT[n]

# Time:  O(n)
# Space: O(1)
def climb_stairs(n):
    OPT = [1, 1]
    OPT_i = OPT[1]
    for i in range(2, n + 1):
        OPT_i = OPT[0] + OPT[1]
        OPT[0] = OPT[1]
        OPT[1] = OPT_i
    return OPT_i

# ~ Paint Fence ~
# House robber?
# OPT[i][?]: ways of painting fences [0, i] given the last two same color or not
# OPT[i][T] = OPT[i - 1][F]
# OPT[i][F] = (OPT[i - 1][T] + OPT[i - 1][F]) * (c - 1)
# OPT[0][F] = 1
# return sum(OPT[n - 1])

# Time:  O(n)
# Space: O(2n)
def paint_fence_explicit(n, c):
    if n is 0:
        return 0
    OPT = [[0, 0] for i in range(n)]
    OPT[0] = [c, 0]
    for i in range(1, n):
        OPT[i][True] = OPT[i - 1][False]
        OPT[i][False] = (OPT[i - 1][True] + OPT[i - 1][False]) * (c - 1)
    return sum(OPT[n - 1])

# Time:  O(n)
# Space: O(2)
def paint_fence(n, c):
    if n is 0:
        return 0
    OPT = [c, 0]
    for i in range(1, n):
        OPT[True], OPT[False] = OPT[False], (OPT[True] + OPT[False]) * (c - 1)
    return sum(OPT)

# ~ Paint House ~
# House robber?
# n steps c choices, each choice you make changes the future, maximize utility
# OPT[i][k]: the minimum cost as of state step i choice k
# OPT[i][k] = min_{j!=k}(OPT[i - 1][j]) + cost[i][k]
# OPT[0][k] = cost[0][k]
# return min(OPT[n - 1])

# Time:  O(3x3xn)
# Space: O(3n)
def paint_house_explicit(costs):
    n = len(costs)
    if n is 0:
        return 0
    OPT = [[0, 0, 0] for i in range(n)]
    OPT[0] = costs[0]
    for i in range(1, n):
        for k in range(3):
            OPT[i][k] = min(OPT[i - 1][j] for j in range(3) if j != k) + \
                    costs[i][k]
    return min(OPT[n - 1])

# Time:  O(3x3xn)
# Space: O(3)
def paint_house(costs):
    n = len(costs)
    if n is 0:
        return 0
    OPT = costs[0]
    for i in range(1, n):
        prev = OPT
        OPT  = [0] * 3
        for k in range(3):
            OPT[k] = min(prev[j] for j in range(3) if j != k) + costs[i][k]
    return min(OPT)

# ~ Paint House II ~
# Time:  O(cn)
# Space: O(c)
def paint_house_ii(costs):
    n = len(costs)
    if n is 0:
        return 0
    c = len(costs[0])
    OPT = costs[0]
    for i in range(1, n):
        prev = OPT
        OPT  = [0] * c
        minimum = [float("inf")] * 2
        minIdx = None
        for k in range(c):
            if prev[k] < minimum[0]:
                minimum[1] = minimum[0]
                minimum[0], minIdx = prev[k], k
            elif prev[k] < minimum[1]:
                minimum[1] = prev[k]
        for k in range(c):
            OPT[k] = (minimum[0] if k != minIdx else minimum[1]) + costs[i][k]
    return min(OPT)
