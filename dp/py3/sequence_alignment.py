# Find an alignment (non-crossing matching): n (or m) steps, for each character
# choose a character from the other string to match or take the gap penalty
# OPT[i][j]: minimum cost alignment between X[:i] and Y[:j]
# OPT[i][j] = min(alpha[X[i]][Y[j]] + OPT[i - 1][j - 1], delta + OPT[i - 1][j], 
#                                                        delta + OPT[i][j - 1])
# OPT[i][0] = 0
# OPT[0][j] = 0
# return OPT[m][n]
# Time:  O(mn)
# Space: O(mn)
def sequence_alignment(X, Y, delta, alpha):
    OPT = [[0] * (len(Y) + 1) for _ in range(len(X) + 1)]
    for i in range(1, len(X) + 1):
        OPT[i][0] = i * delta
    for j in range(1, len(Y) + 1):
        OPT[0][j] = j * delta
    for i in range(1, len(X) + 1):
        for j in range(1, len(Y) + 1):
            OPT[i][j] = min(alpha[X[i - 1]][Y[j - 1]] + OPT[i - 1][j - 1], \
                    delta + OPT[i - 1][j], \
                    delta + OPT[i][j - 1])
    return OPT[len(X)][len(Y)]

def sequence_alignment_memo(X, Y, delta, alpha):
    def helper(i, j):
        if (i, j) in cache:
            return cache[(i, j)]
        elif i == 0 or j == 0:
            return (i or j) * delta
        cost = min(alpha[X[i - 1]][Y[j - 1]] + helper(i - 1, j - 1), \
                delta + helper(i - 1, j), \
                delta + helper(i, j - 1))
        cache[(i, j)] = cost
        return cache[(i, j)]
    cache = {}
    return helper(len(X), len(Y))
