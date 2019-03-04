def palindromic_substrings(s):
    n = len(s)
    OPT = [[False] * n for i in range(n)]
    count = n
    for i in range(n):
        OPT[i][i] = True
    for i in range(n - 1):
        OPT[i][i + 1] = s[i] == s[i + 1]
        count += OPT[i][i + 1]
    # 0 + delta < n
    for delta in range(2, n):
        # i + delta < n
        for i in range(n - delta):
            j = i + delta
            OPT[i][j] = OPT[i + 1][j - 1] and s[i] == s[j]
            count += OPT[i][j]
    return count

def palindromic_substrings(s):
    n = len(s)
    pprev = None
    prev = [True for i in range(n)]                 # OPT[0][*]
    OPT = [s[i] == s[i + 1] for i in range(n - 1)]  # OPT[1][*]
    count = n + sum(OPT)
    # 0 + delta < n
    for delta in range(2, n):
        pprev, prev = prev, OPT
        OPT = [False] * (n - delta)
        # i + delta < n
        for i in range(n - delta):
            OPT[i] = pprev[i + 1] and s[i] == s[i + delta]
            count += OPT[i]
    return count

def longest_palindromic_substr_explicit(s):
    OPT = [[False] * len(s) for i in range(len(s))]
    start, end = 0, 0
    # 0 + delta < n
    for delta in range(len(s)):
        # i + delta < n
        for i in range(len(s) - delta):
            if delta is 0:
                OPT[0][i] = True
            elif delta is 1:
                if i < len(s) - 1:
                    OPT[1][i] = s[i] == s[i + 1]
            else:
                OPT[delta][i] = OPT[delta-2][i + 1] and s[i] == s[i + delta]
            if OPT[delta][i]:
                start, end = i, i + delta + 1
    return s[start: end]
