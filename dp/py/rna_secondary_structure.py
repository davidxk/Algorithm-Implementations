# Find a set of non-crossing interval pairs: n steps, for each element choose
# a mathcing element to pair with or discard this element
# OPT[i][j]: maximum number of base pairs in a secondary structure on b[i, j]
# OPT[i][j] = max(OPT[i][j - 1], max(1 + OPT[i][t - 1] + OPT[t + 1][j - 1]))
#                                for all t in [j - 1] where b[t] matches b[j]
#                                OPT[i][t - 1] = 0 for all i > t - 1
# OPT[i][0, i + 4] = 0
# return OPT[0][n-1]
# Time:  O(n^3)
# Space: O(n^2)
def rna_secondary_structure(rna):
    complement = {"A": "U", "U": "A", "C": "G", "G": "C"}
    OPT = [[0] * len(rna) for _ in range(len(rna))]
    for length in range(5, len(rna)):
        for i in range(len(rna) - length):
            j = i + length
            OPT[i][j] = OPT[i][j - 1]
            for t in range(i, j - 4):
                if rna[t] == complement[rna[j]]:
                    num = 1 + OPT[t + 1][j - 1] + (i <= t - 1 and OPT[i][t - 1])
                    if num > OPT[i][j]:
                        OPT[i][j] = num
    return OPT[0][-1]

def rna_secondary_structure_memo(rna):
    complement = {"A": "U", "U": "A", "C": "G", "G": "C"}
    def helper(left, right):
        if right - left + 1 < 4:
            return 0
        elif (left, right) in cache:
            return cache[(left, right)]
        maximum = 0
        for t in range(left + 5, right + 1):
            if rna[t] == complement[rna[left]]:
                pairs = 1 + helper(left + 1, t - 1) + helper(t + 1, right)
                maximum = max(pairs, maximum)
        pairs = helper(left + 1, right)
        maximum = max(pairs, maximum)
        cache[(left, right)] = maximum
        return maximum
    cache = {}
    return helper(0, len(rna) - 1)
