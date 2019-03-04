# ~ Decode Ways ~
# OPT[i][?]: number of ways s [0, i] given whether the last digit is alone
# OPT[i][F] = OPT[i - 1][T] if int(s [i - 1, i]) < 27 else 0
# OPT[i][T] = sum(OPT[i - 1]) if s[i] != "0" else 0
# OPT[0][T] = s[i] != "0"
# OPT[0][F] = 0
# return sum(OPT[n - 1])
# Time:  O(2n)
# Space: O(2n)
def decode_ways_explicit(s):
        n = len(s)
        if n is 0:
            return 0
        OPT = [[0, 0] for i in range(n)]
        OPT[0] = [0, s[0] != "0"]
        for i in range(1, n):
            OPT[i][False] = OPT[i - 1][True] if int(s[i - 1: i + 1]) < 27 else 0
            OPT[i][True]  = sum(OPT[i - 1]) if s[i] != "0" else 0
        return sum(OPT[n - 1])

# Time:  O(2n)
# Space: O(2)
def decode_ways(s):
    OPT = [0, s[0] != "0"]
    for i in range(1, len(s)):
        prev, OPT = OPT, [0, 0]
        OPT[False] = prev[True] if int(s[i - 1: i + 1]) < 27 else 0
        OPT[True]  = sum(prev) if s[i] != "0" else 0
    return sum(OPT)

# ~ !Word Break! ~
# Segment Least Squares. Chapter DP.
# OPT[i]: if s[0: i] can be segmented
# OPT[i] = any(OPT[j] and s[j: i] in wordDict), 0 <= j < i
# OPT[0] = True
# return OPT[0][n]
# Time:  O(n^2)
# Space: O(n)
def word_break(s, wordDict):
    wordDict = set(wordDict)
    n = len(s)
    OPT = [False] * (n + 1)
    for i in range(1, n + 1):
        OPT[0] = True
        OPT[i] = any(OPT[j] and s[j: i] in wordDict for j in range(i))
    return OPT[n]

# Time:  O(n^2)
# Space: O(n)
def word_break_cached_dfs(s, wordDict):
    def helper(end):
        if end in cache:
            return cache[end]
        for middle in range(end):
            if helper(middle) and s[middle: end] in wordDict:
                cache[end] = True
                return True
        cache[end] = False
        return False
    wordDict = set(wordDict)
    cache = {0: True}
    return helper(len(s))

# ~ Min Path Sum ~
# OPT[i][j]: minimum cost from top left to a[i][j]
# OPT[i][j] = min(OPT[i - 1][j], OPT[i][j - 1]) + a[i][j]
# OPT[0][0] = grid[0][0]
# OPT[i][0] = OPT[i - 1][0] + a[i][0]
# OPT[0][j] = OPT[0][j - 1] + a[0][j]
# return OPT[n - 1][m - 1]
# Time:  O(n^2)
# Space: O(n^2)
def min_path_sum_explicit(grid):
        n, m = len(grid), len(grid[0])
        OPT = [[0] * m for i in range(n)]
        OPT[0][0] = grid[0][0]
        for j in range(1, m):
            OPT[0][j] = OPT[0][j - 1] + grid[0][j]
        for i in range(1, n):
            OPT[i][0] = OPT[i - 1][0] + grid[i][0]
            for j in range(1, m):
                OPT[i][j] = min(OPT[i - 1][j], OPT[i][j - 1]) + grid[i][j]
        return OPT[n - 1][m - 1]

# Time:  O(n^2)
# Space: O(n)
def min_path_sum(grid):
        n, m = len(grid), len(grid[0])
        OPT = list(grid[0])
        for j in range(1, m):
            OPT[j] += OPT[i - 1]
        for i in range(1, n):
            prev, OPT = OPT, [0] * m
            OPT[0] = prev[0] + grid[i][0]
            for j in range(1, m):
                OPT[j] = min(OPT[j - 1], prev[j]) + grid[i][j]
        return OPT[m - 1]
