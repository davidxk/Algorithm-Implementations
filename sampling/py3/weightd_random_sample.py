import random
from bisect import bisect

# 1   2   3   4
# 1   3   6   10
# 0 1~2 3~5 6~9
# Find upper bound use bisect

# Input [weight]; output sampled index
# Compute prefix sum once and sample with replacement O(log n) every time after
# Time:  O(n) + O(log n)
# Space: O(n)
def weighted_random_sample(weights):
    if not weights:
        raise IndexError("Cannot choose from an empty sequence")
    sums = list(weights)
    for i in range(1, len(weights)):
        sums[i] += sums[i - 1]
    rand = random.randrange(sums[-1])
    return bisect(sums, rand)
