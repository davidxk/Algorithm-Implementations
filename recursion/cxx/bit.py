"""
[000]
[000, 100]
[000, 100, 010, 110]
[000, 100, 010, 110, 001, 101, 0l1, 111]
"""
def bitPermutations(bits):
    result = [bits]
    for i in range(len(bits)):
        for array in result:
            copy = list(array)
            copy[i] = not copy[i]
            result.append(copy)

"""
00  01  10
001 010 100
"""
# O[i][k]: set of combinations of length i with k 1s
# O[i][k] = {O[i - 1][k] + "0", [i - 1][k - 1] + "1"}
# O[i][0] += ["0" * i]
# return O[n - 1][k - 1]
def bitCombinations(n, K):
    O = [[""]]
    for i in range(1, n + 1):
        prev, O = O, [[] for _ in range(min(i + 1, K + 1))]
        O[0] = ["0" * i]
        for k in range(1, min(i + 1, K + 1)):
            if k < i:
                O[k] += map(lambda x: x + "0", prev[k])
            O[k] += map(lambda x: x + "1", prev[k - 1])
    return O[K]
