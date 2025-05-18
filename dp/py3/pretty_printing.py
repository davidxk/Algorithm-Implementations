
def line_slack(words, max_line_len):
    line_length = sum(map(len, words)) + len(words) - 1
    return max_line_len - line_length


def precompute_slack_squares(words, max_line_len):
    slack_sqares = [[float("inf")] * (len(words) + 1) for _ in words]
    for j in range(len(words) + 1):
        for i in range(j - 1, -1, -1):
            slack = line_slack(words[i:j], max_line_len)
            if slack < 0:
                break
            slack_sqares[i][j] = slack ** 2
    return slack_sqares


# Find a partition: variable steps, for each element j that could be a segment
# end find a preceding point i so that segment [i, j) minimizes the overall cost
# OPT[j]: min cost for segmenting points[:j]
# OPT[j] = min(c(i, j) + OPT[i]), 0 <= i < j
# OPT[0] = 0
# return OPT[n]
# Time:  O(n^2)
# Space: O(n^2)

def pretty_printing(words, max_line_len):
    slack_sqares = precompute_slack_squares(words, max_line_len)
    n = len(words)
    OPT = [float("inf")] * (n + 1)
    OPT[0] = 0
    for j in range(1, n + 1):
        for i in range(j):
            candidate = slack_sqares[i][j] + OPT[i]
            if candidate < OPT[j]:
                OPT[j] = candidate
    return OPT[n]


def pretty_printing_sol(words, max_line_len):
    slack_sqares = precompute_slack_squares(words, max_line_len)
    n = len(words)
    OPT = [float("inf")] * (n + 1)
    OPT[0] = 0
    for j in range(1, n + 1):
        for i in range(j):
            candidate = slack_sqares[i][j] + OPT[i]
            if candidate < OPT[j]:
                OPT[j] = candidate

    solution = []
    j = n
    while j > 0:
        for i in range(j):
            if OPT[j] == slack_sqares[i][j] + OPT[i]:
                solution.append((i, j))
                j = i
                break
    result = []
    for i, j in reversed(solution):
        result.append(' '.join(words[i:j]))
    return result, OPT[n]


def pretty_printing_memo(words, max_line_len):
    slack_sqares = precompute_slack_squares(words, max_line_len)
    def compute_opt(j):
        if j in cache:
            return cache[j]
        minimum = float("inf")
        for i in range(j):
            candidate = slack_sqares[i][j] + compute_opt(i)
            if candidate < minimum:
                minimum = candidate
        cache[j] = minimum
        return minimum
    cache = {0: 0}
    return compute_opt(len(words))
