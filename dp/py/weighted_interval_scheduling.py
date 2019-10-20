from bisect import bisect
def precompute_rightmost_compatible(startTimes, finishTimes):
    p = []
    for i, startTime in enumerate(startTimes):
        higher = bisect(finishTimes, startTime)
        floor = higher - 1
        p.append(floor) # -1 means floor not found
    return p

# Find a subset: n steps, for each element decide to include it or not
# OPT[j]: max value in intervals[0..j]
# OPT[j] = max(OPT[p(j)] + values[j], OPT[j-1])
#                  p(j) is the index of the latest-ending j-compatible interval
# OPT[0] = values[0]
# return OPT[n-1]
# Time:  O(n log n)
# Space: O(n)
# Precondition: intervals sorted by finish time
def weighted_interval_scheduling(startTimes, finishTimes, values):
    p = precompute_rightmost_compatible(startTimes, finishTimes)
    OPT = [0] * len(values)
    OPT[0] = values[0]
    for j in range(1, len(values)):
        if p[j] != -1:
            OPT[j] = max(OPT[p[j]] + values[j], OPT[j - 1])
        else:
            OPT[j] = max(values[j], OPT[j - 1])
    return OPT[len(values) - 1]

def weighted_interval_scheduling_sol(startTimes, finishTimes, values):
    p = precompute_rightmost_compatible(startTimes, finishTimes)
    OPT = [0] * len(values)
    # WARNING: Making use of OPT[-1] = 0; other languages may not support
    #          negative indices. The above implementation is more portable.
    OPT.append(0)
    for j in range(len(values)):
        OPT[j] = max(OPT[p[j]] + values[j], OPT[j - 1])

    solution = []
    j = len(values) - 1
    while j >= 0:
        if OPT[p[j]] + values[j] > OPT[j - 1]:
            solution.append(j)
            j = p[j]
        else:
            j -= 1
    return solution, OPT[len(values) - 1]

def weighted_interval_scheduling_memo(startTimes, finishTimes, values):
    p = precompute_rightmost_compatible(startTimes, finishTimes)
    def compute_opt(j):
        if j in cache:
            return cache[j]
        cache[j] = max(compute_opt(p[j]) + values[j], compute_opt(j - 1))
        return cache[j]
    cache = {-1: 0}
    return compute_opt(len(values) - 1)

def weighted_interval_scheduling_memo_sol(startTimes, finishTimes, values):
    p = precompute_rightmost_compatible(startTimes, finishTimes)
    def compute_opt(j):
        if j in cache:
            return cache[j]
        cache[j] = max(compute_opt(p[j]) + values[j], compute_opt(j - 1))
        return cache[j]
    cache = {-1: 0}
    compute_opt(len(values) - 1)
    def find_sol(j):
        if j == -1:
            return solution
        if cache[p[j]] + values[j] > cache[j - 1]:
            solution.append(j)
            find_sol(p[j])
        else:
            find_sol(j - 1)
        return solution
    solution = []
    return find_sol(len(values) - 1), cache[len(values) - 1]
