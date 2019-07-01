# OPT[i][k]: maximum value from items[:i] where the total weight is <= k
# OPT[i][k] = max(OPT[i - 1][k], OPT[i - 1][k - w[i-1]] + v[i-1])
# OPT[0][k] = 0
# OPT[i][0] = 0
# return OPT[n - 1][K]
# Time:  O(nK)
# Space: O(nK)
def knapsack(weights, values, capacity):
    OPT = [[0] * (capacity + 1) for _ in range(len(weights) + 1)]
    for i in range(1, len(weights) + 1):
        for k in range(1, capacity + 1):
            weight, value = weights[i - 1], values[i - 1]
            if k - weight < 0:
                OPT[i][k] = OPT[i - 1][k]
            else:
                OPT[i][k] = max(OPT[i - 1][k], OPT[i - 1][k - weight] + value)
    return OPT[-1][-1]

def knapsack_two_rows(weights, values, capacity):
    prev = [0] * (capacity + 1)
    OPT = [0] * (capacity + 1)
    for i in range(len(weights)):
        prev, OPT = OPT, prev
        for k in range(1, capacity + 1):
            if k - weights[i] < 0:
                OPT[k] = prev[k]
            else:
                OPT[k] = max(prev[k], prev[k - weights[i]] + values[i])
    return OPT[-1]

def knapsack_one_row(weights, values, capacity):
    OPT = [0] * (capacity + 1)
    for i in range(len(weights)):
        for k in reversed(range(1, capacity + 1)):
            if weights[i] <= k:
                OPT[k] = max(OPT[k], OPT[k - weights[i]] + values[i])
    return OPT[-1]

def knapsack_memo(weights, values, capacity):
    def helper(start, capacity):
        if (start, capacity) in cache:
            return cache[(start, capacity)]
        maximum = 0
        for i in range(start, len(weights)):
            if weights[i] <= capacity:
                value = values[i] + helper(i + 1, capacity - weights[i])
                maximum = max(value, maximum)
        cache[(start, capacity)] = maximum
        return cache[(start, capacity)]
    cache = {}
    return helper(0, capacity)
