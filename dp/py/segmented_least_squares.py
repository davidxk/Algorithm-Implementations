def precompute_errors(points, error):
    errors = [[float("inf")] * (len(points) + 1) for _ in points]
    for i in range(len(points)):
        for j in range(i + 1, len(points) + 1):
            errors[i][j] = error(points[i: j])
    return errors

# Find a partition: variable steps, for each element j that could be a segment
# end find a preceding point i so that segment [i, j) minimizes the overall cost
# OPT[j]: min cost for segmenting points[:j]
# OPT[j] = min(e(i, j) + C + OPT[i]), 0 <= i < j
# OPT[0] = 0
# return OPT[n]
# Time:  O(n^2)
# Space: O(n^2)
def segmented_least_squares(points, error, penalty):
    errors = precompute_errors(points, error)
    n = len(points)
    OPT = [float("inf")] * (n + 1)
    OPT[0] = 0
    for j in range(1, n + 1):
        for i in range(j):
            candidate = errors[i][j] + penalty + OPT[i]
            if candidate < OPT[j]:
                OPT[j] = candidate
    return OPT[n]
