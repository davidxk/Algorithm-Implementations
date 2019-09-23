# ** A sequence alignment problem **
# Find an alignment (non-crossing matching): n (or m) steps, for each character
# find a matching character from the other string or skip it
# OPT[i][j]: longest common subsequence in str1[:i] and str2[:j]
# OPT[i][j] = max(OPT[i - 1][j - 1] + (s1[i - 1] == s2[j - 1]), OPT[i - 1][j],
#                                                               OPT[i][j - 1])
# OPT[0][j] = 0
# OPT[i][0] = 0
# return OPT[n][m]
# Time:  O(mn)
# Space: O(mn)
def longest_common_subsequence(str1, str2):
    OPT = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            OPT[i][j] = max(OPT[i - 1][j], OPT[i][j - 1], \
                    OPT[i - 1][j - 1] + (str1[i - 1] == str2[j - 1]))
    return OPT[-1][-1]

def longest_common_subsequence_memo(str1, str2):
    def helper(end1, end2):
        if end1 == 0 or end2 == 0:
            return 0
        elif (end1, end2) in cache:
            return cache[(end1, end2)]
        cache[(end1, end2)] = max(
                helper(end1 - 1, end2 - 1) + (str1[end1 - 1] == str2[end2 - 1]),
                helper(end1 - 1, end2),
                helper(end1, end2 - 1))
        return cache[(end1, end2)]
    cache = {}
    return helper(len(str1), len(str2))
