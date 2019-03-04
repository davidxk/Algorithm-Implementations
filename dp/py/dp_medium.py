# ~ Arithmetic Slices ~
# OPT[i]: the number of arithmatic slices ending with a[i]
# OPT[i] = OPT[i - 1] + 1 if a[i] - a[i - 1] == a[i - 1] - a[i - 2] else 0
# OPT[0] = 0
# OPT[1] = 0
# return sum(OPT)
# Time:  O(n)
# Space: O(n)
def arithmetic_slices_explicit(A):
    n = len(array)
    OPT = [0] * n
    for i in range(2, n):
        OPT[i] = OPT[i - 1] + 1 if A[i] - A[i - 1] == A[i - 1] - A[i - 2] else 0
    return sum(OPT)

# Time:  O(n)
# Space: O(1)
def arithmetic_slices(A):
    OPT = 0
    summation = 0
    for i in range(2, len(array)):
        OPT = OPT + 1 if A[i] - A[i - 1] == A[i - 1] - A[i - 2] else 0
        summation += OPT
    return summation

# ~ !Pair Chain! ~
# Interval Scheduling. Chapter Greedy.
# OPT[i]: the longest pair chain ending with a[i]
# OPT[i] = max(OPT[j]) + 1, j < i and a[j][1] < a[i][0]
# return max(OPT)
# Time:  O(n log n)
# Space: O(1)
def pair_chain(pairs):
    pairs.sort(key=lambda pair: pair[1])
    tail = [-float("inf"), -float("inf")]
    result = 0
    for pair in pairs:
        if tail[1] < pair[0]:
            result += 1
            tail = pair
    return result

"""Minimax solved with recursion"""
# ~ Take Coin ~
# OPT[i][j]: max coin take from a [i, j]
# OPT[i][j] = max(OPT[i + 1][j] + a[i], OPT[i][j - 1] + a[j])
# OPT[i][i] = a[i]
# return OPT[0][n - 1]
# Time:  O(n^2)
# Space: O(n^2)
def take_coin_explicit(nums):
    OPT = [[0] * len(nums) for i in range(len(nums))]
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            OPT[i][j] = max(nums[i] - OPT[i + 1][j], nums[j] - OPT[i][j - 1])
    return OPT[0][-1] >= 0

# Time:  O(n^2)
# Space: O(n)
def take_coin(nums):
    OPT = [[0] * len(nums) for i in range(2)]
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            OPT[i%2][j] = max(nums[i] - OPT[(i+1)%2][j],nums[j] - OPT[i%2][j-1])
    return OPT[0][-1] >= 0

# ~ Longest Increasing Subsequence ~
# OPT[i]: length of longest inc subseq ending with a[i]
# OPT[i] = max(OPT[j] + 1), j < i and a[j] < a[i]
# OPT[0] = 1
# return max(OPT)
# Time:  O(n^2)
# Space: O(n)
def longest_inc_subseq_simple(nums):
    OPT = [0] * len(nums)
    maximum = 0
    for i in range(len(nums)):
        tmpMax = 1
        for j in range(i):
            if nums[j] < nums[i]:
                tmpMax = max(tmpMax, OPT[j] + 1)
        OPT[i] = tmpMax
        maximum = max(maximum, OPT[i])
    return maximum

# Time:  O(n log n)
# Space: O(n)
from bisect import bisect_left
def longest_inc_subseq(nums):
    tails = []
    for num in nums:
        idx = bisect_left(tails, num)
        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num
    return len(tails)

# ~ Perfect Squares ~
# At each step a square number is chosen, the cost is 1
# OPT[i]: the minimum number of perfect square numbers that sums up to i
# OPT[i] = min(OPT[i - k^2] + 1), k in [1, int(sqrt(i))]
# OPT[0] = 0
# return OPT[n]
# Time:  O(?)
# Space: O(n)
def perfect_squares_memo(n):
    def helper(n, limit):
        if limit <= 1:
            return 1
        elif n in cache:
            return cache[n]
        minimum = n
        for i in range(int(n ** 0.5), 0, -1):
            local = 1 + helper(n - i ** 2, minimum - 1)
            if local < minimum:
                minimum = local
        cache[n] = minimum
        return minimum
    cache = {i * i: 1 for i in range(1, int(n ** 0.5) + 1)}
    return helper(n, n)

def perfect_squares(n):
    OPT = [0] * (n + 1)
    for i in range(1, n + 1):
        OPT[i] = min(OPT[i - k*k] + 1 for k in range(1, int(math.sqrt(i)) + 1))
    return OPT[-1]

# ~ Wiggle Subsequence ~
# OPT[i][?]: length of the longest wiggle subseq ending with a[i] last is up
# OPT[i][F] = max(OPT[j][T] + 1), 0 <= j < i and a[j] > a[i]
# OPT[i][T] = max(OPT[j][F] + 1), 0 <= j < i and a[j] < a[i]
# OPT[0][?] = 1
# return max(OPT[-1])
# Time:  O(n^2)
# Space: O(n)
def wiggle_subseq_n_square(nums):
    OPT = [[0, 0] for i in range(len(nums))]
    OPT[0][False] = OPT[0][True] = 1
    for i in range(1, len(nums)):
        OPT[i][False] = max([OPT[j][True] for j in range(i) \
                if nums[j] > nums[i]] or [0]) + 1
        OPT[i][True] = max([OPT[j][False] for j in range(i) \
                if nums[j] < nums[i]] or [0]) + 1
    return max(OPT[-1])

# OPT[i][T]: length of the longest wiggle subseq ending with >= a[i] last is up
# OPT[i][F]: length of the longest wiggle subseq ending with <= a[i] last is dn
# OPT[i][F] = OPT[i - 1][T] + 1 if a[i - 1] > a[i] else OPT[i - 1][F]
# OPT[i][T] = OPT[i - 1][F] + 1 if a[i - 1] < a[i] else OPT[i - 1][T]
# Time:  O(n)
# Space: O(n)
def wiggle_subseq(nums):
    OPT = [[0, 0] for i in range(len(nums))]
    OPT[0][False] = OPT[0][True] = 1
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:   # Going down
            OPT[i][False] = OPT[i - 1][True] + 1
            OPT[i][True] = OPT[i - 1][True]
        elif nums[i - 1] < nums[i]: # Going up
            OPT[i][True] = OPT[i - 1][False] + 1
            OPT[i][False] = OPT[i - 1][False]
        else:
            OPT[i][True] = OPT[i - 1][True]
            OPT[i][False] = OPT[i - 1][False]
    return max(OPT[-1])

# ~ Longest Palindromic Subsequence ~
# OPT[i][j]: length of longest palindromic subsequence of s[i, j]
# OPT[i][j] = max(OPT[i + 1][j], OPT[i][j - 1]) if s[i] != s2[j]
#                                               else OPT[i + 1][j - 1] + 2
# OPT[i][i] = 1
# OPT[i][i + 1] = s1[i] == s2[i + 1]
# return OPT[0][n - 1]
# Time:  O(n^2)
# Space: O(n^2)
def longest_palindromic_subseq_explicit(s):
    OPT = [[0] * len(s) for i in range(len(s))]
    for i in range(len(s) - 1, -1, -1):
        OPT[i][i] = 1
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                OPT[i][j] = OPT[i + 1][j - 1] + 2
            else:
                OPT[i][j] = max(OPT[i + 1][j], OPT[i][j - 1])
    return OPT[0][-1]

# Time:  O(n^2)
# Space: O(n)
def longest_palindromic_subseq(s):
    OPT = [[0] * len(s) for i in range(2)]
    for i in range(len(s) - 1, -1, -1):
        OPT[i % 2][i] = 1
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                OPT[i % 2][j] = OPT[(i + 1) % 2][j - 1] + 2
            else:
                OPT[i % 2][j] = max(OPT[(i + 1) % 2][j], OPT[i % 2][j - 1])
    return OPT[0][-1]

"""String DP: Sequence Alignment"""
# ~ Is Subsequence ~
# OPT[i][j]: is s[:i] subsequence of t[:j]
# OPT[i][j] = OPT[i][j - 1] or OPT[i - 1][j - 1] and s[i - 1] == t[j - 1]
# OPT[0][j] = True
# OPT[i][j] = False
# return OPT[n][m]
# Time:  O(nm)
# Space: O(nm)
def is_subseq(s, t):
    OPT = [[False] * (len(t) + 1) for _ in range(len(s) + 1)]
    for j in range(len(t) + 1):
        OPT[0][j] = True
    for i in range(1, len(s) + 1):
        OPT[i][0] = False
        for j in range(1, len(t) + 1):
            OPT[i][j] = OPT[i][j-1] or OPT[i-1][j-1] and s[i-1] == t[j-1]
    print OPT
    return OPT[-1][-1]

# ~ Longest Common Substring ~
# OPT[i][j]: length of longest common substring ending with s1[i] and s2[j]
# OPT[i][j] = s1[i] == s2[j] and OPT[i - 1][j - 1] + 1
# OPT[0][j] = int(s1[0] == s2[j])
# OPT[i][0] = int(s1[i] == s2[0])
# return max(OPT)
# Time:  O(nm)
# Space: O(nm)
def longest_common_substr_explicit(s, t):
    OPT = [[0] * len(s2) for i in range(len(s1))]
    for j in range(len(s2)):
        OPT[0][j] = int(s1[0] == s2[j])
    for i in range(1, len(s1)):
        OPT[i][0] = int(s1[i] == s2[0])
        for j in range(1, len(s2)):
            if s1[i] == s2[j]:
                OPT[i][j] = OPT[i - 1][j - 1] + 1
        return max(max(line) for line in OPT)

# ~ !Delete Char! ~
# Sequence Alignment. Chapter DP.
# OPT[i][j]: make s1[:i] and s2[:j] equal through min deletion
# OPT[i][j] = min(OPT[i-1][j], OPT[i][j-1]) + 1 if s1[i-1] != s2[j-1]
#                                               else OPT[i-1][j-1]
# OPT[0][j] = j
# OPT[i][0] = i
# return OPT[n][m]
# Time:  O(nm)
# Space: O(nm)
def min_del_explicit(word1, word2):
    OPT = [[0] * (len(word2) + 1) for i in range(len(word1) + 1)]
    for j in range(len(word2) + 1):
        OPT[0][j] = j
    for i in range(1, len(word1) + 1):
        OPT[i][0] = i
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                OPT[i][j] = OPT[i - 1][j - 1]
            else:
                OPT[i][j] = min(OPT[i - 1][j], OPT[i][j - 1]) + 1
    return OPT[-1][-1]

# Time:  O(nm)
# Space: O(m)
def min_del(word1, word2):
    prev = [0] * (len(word2) + 1)
    OPT = [j for j in range(len(word2) + 1)]
    for i in range(1, len(word1) + 1):
        prev, OPT = OPT, prev
        OPT[0] = i
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                OPT[j] = prev[j - 1]
            else:
                OPT[j] = min(prev[j], OPT[j - 1]) + 1
    return OPT[-1]


# ~ !ASCII Delete! ~
# OPT[i][j]: min ASCII deletion for matching s1[0: i] and s2[0: j]
# OPT[i][j] = min(OPT[i-1][j] + ord(s1[i-1]), OPT[i][j-1] + ord(s2[j-1]))
#             if s1[i-1] != s[j-1] else OPT[i-1][j-1]
# OPT[0][0] = min(ord(s1[i]), ord(s2[j])) if s1[i] != s[j] else 0
# OPT[0][1] = min(ord(s1[i]), OPT[i][j-1] + ord(s2[j])) if s1[i] != s[j] else 0
# OPT[1][0] = min(OPT[i-1][j] + ord(s1[i]), ord(s2[j])) if s1[i] != s[j] else 0
# return OPT[n][m]
# Time:  O(nm)
# Space: O(nm)
def ascii_delete_explicit(s1, s2):
    n, m = len(s1), len(s2)
    OPT = [[0] * (m + 1) for i in range(n + 1)]
    for j in range(1, m + 1):
        OPT[0][j] += OPT[0][j - 1] + ord(s2[j - 1])
    for i in range(1, n + 1):
        OPT[i][0] += OPT[i - 1][0] + ord(s1[i - 1])
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                OPT[i][j] = OPT[i - 1][j - 1]
            else:
                OPT[i][j] = min(OPT[i - 1][j] + ord(s1[i - 1]), \
                                OPT[i][j - 1] + ord(s2[j - 1]))
    return OPT[n][m]

# Time:  O(nm)
# Space: O(min(m, n))
def ascii_delete(s1, s2):
    n, m = len(s1), len(s2)
    if n < m:
        return ascii_delete(s2, s1)
    prev = [0] * (m + 1)
    OPT = [0] * (m + 1)
    for j in range(1, m + 1):
        OPT[j] += OPT[j - 1] + ord(s2[j - 1])
    for i in range(1, n + 1):
        prev, OPT = OPT, prev
        OPT[0] = prev[0] + ord(s1[i - 1])
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                OPT[j] = prev[j - 1]
            else:
                OPT[j] = min(prev[j] + ord(s1[i-1]), OPT[j-1] + ord(s2[j-1]))
    return OPT[m]

# ~ !Edit Distance! ~
# OPT[i][j]: min edit distance of s1[:i] and s2[:j] through delete and replace
# OPT[i][j] = min(OPT[i-1][j], OPT[i][j-1], OPT[i-1][j-1]) + 1
#                 if s1[i-1] != s2[j-1] else OPT[i-1][j-1]
# OPT[0][j] = j
# OPT[i][0] = i
# return OPT[n][m]
# Time:  O(nm)
# Space: O(nm)
def edit_distance_explicit(word1, word2):
    OPT = [[0] * (len(word2) + 1) for i in range(len(word1) + 1)]
    for j in range(len(word2) + 1):
        OPT[0][j] = j
    for i in range(1, len(word1) + 1):
        OPT[i][0] = i
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                OPT[i][j] = OPT[i - 1][j - 1]
            else:
                OPT[i][j] = min(OPT[i-1][j], OPT[i][j-1], OPT[i-1][j-1]) + 1
    return OPT[-1][-1]

# Time:  O(nm)
# Space: O(m)
def edit_distance(word1, word2):
    prev = [0] * (len(word2) + 1)
    OPT = [j for j in range(len(word2) + 1)]
    for i in range(1, len(word1) + 1):
        prev, OPT = OPT, prev
        OPT[0] = i
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                OPT[j] = prev[j - 1]
            else:
                OPT[j] = min(OPT[j - 1], prev[j], prev[j - 1]) + 1
    return OPT[-1]

# Longest Common Subsequence
# OPT[i][j]: length of longest common subsequence in s1[:i] and s2[:j]
# OPT[i][j] = max(OPT[i-1][j], OPT[i][j-1]) if s1[i-1] != s2[j-1]
#                                           else OPT[i-1][j-1] + 1
# OPT[0][j] = 0
# OPT[i][0] = 0
# return OPT[n][m]
# Time:  O(nm)
# Space: O(nm)
def longest_common_subsequence_explicit(word1, word2):
    OPT = [[0] * (len(word2) + 1) for i in range(len(word1) + 1)]
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                OPT[i][j] = OPT[i - 1][j - 1] + 1
            else:
                OPT[i][j] = max(OPT[i - 1][j], OPT[i][j - 1])
    # return OPT[-1][-1]
    i, j = len(word1), len(word2)
    result = []
    while i > 0:
        if word1[i - 1] == word2[j - 1]:
            result.append(word1[i - 1])
            i -= 1; j -= 1
        else:
            if OPT[i - 1][j] > OPT[i][j - 1]:
                i -= 1
            else:
                j -= 1
    return str().join(reversed(result))

"""Palindromic Substrings can be solved with two pointers within O(1) space"""
# ~ Palindromic Substrings ~
# OPT[i][j]: whether s [i, j] is a palindrome
# OPT[i][j] = OPT[i + 1][j - 1] and s[i] == s[j]
# OPT[i][i] = True
# OPT[i][i + 1] = s[i] == s[i + 1]
# return sum(sum(line) for line in OPT)
# Time:  O(n^2)
# Space: O(n^2)
def palindromic_substrings_explicit(s):
    n = len(s)
    OPT = [[False] * n for i in range(n)]
    count = n
    for i in range(n):
        OPT[i][i] = True
    for i in range(len(s) - 1, -1, -1):
        for j in range(i + 1, len(s)):
            if j == i + 1:
                OPT[i][i + 1] = s[i] == s[i + 1]
            else:
                OPT[i][j] = OPT[i + 1][j - 1] and s[i] == s[j]
            count += OPT[i][j]
    return count

# OPT[delta][i]: whether s [i, i + delta] is a palindrome
# Time:  O(n^2)
# Space: O(n)
def palindromic_substrings(s):
    n = len(s)
    prev = [False] * len(s)
    OPT = [False] * len(s)
    count = n
    for i in range(n - 1, -1, -1):
        OPT, prev = prev, OPT
        OPT[i] = True
        for j in range(i + 1, n):
            if j == i + 1:
                OPT[j] = s[i] == s[j]
            else:
                OPT[j] = prev[j - 1] and s[i] == s[j]
            count += OPT[j]
    return count

# ~ Longest Palindromic Substring ~
# OPT[delta][i]: whether s[i, i + delta] is a palindrome
# OPT[delta][i] = OPT[delta - 2][i + 1] and s[i] == s[i + delta]
# OPT[0][i] = True
# OPT[1][i] = s[i] == s[i + 1]
# return delta + 1 for delta in range(n - 1, -1, -1) if any(OPT[delta])
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
