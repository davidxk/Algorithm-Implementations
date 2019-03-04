# Guess Number Low or High ~
# OPT[i][j]: min cost for [i: j]
# OPT[i][j] = min(max(OPT[i][k], OPT[k+1][j]) + k), (i+j)/2 <= k < j
# OPT[i][i] = 0
# OPT[i][i+1] = 0
# return OPT[1][n]
# Time:  O(n^3)
# Space: O(n^2)
def guess_number(n):
    OPT = [[0] * (n + 2) for _ in range(n + 1)]
    for i in range(n):
        if i + 1 < n:
            OPT[i][i + 1] = 0
        OPT[i][i] = 0
    # 0 + delta <= j <= n + 1
    for delta in range(2, n + 2):
        # j = i + delta <= n + 1
        for i in range(1, n - delta + 2):
            j = i + delta
            minimum = j * delta
            # k + 1 < j
            for k in range((i+j)/2 - 1, j - 1):
                minimum = min(max(OPT[i][k], OPT[k+1][j]) + k, minimum)
            OPT[i][j] = minimum
    return OPT[1][-1]

# ~ Partition K Equal Sum ~
# State: which numbers has been used
# Choice: choose a number not used to add to the total without crossing the line
# OPT[subset]: is it possible to partition subset into some sum k and a residual
# OPT[subset] = any(OPT[subset-{num[j]}] and num[j] < tar - (sum(subset) % tar))
# OPT[{}] = True
# return OPT[{nums}]
# Time:  O(n 2^n)
# Space: O(2^n)
# However, not all subproblems are valid - there is pruning involved
def partition_equal_sum_k_tablefilling_pull(nums, k):
    target, rem = divmod(sum(nums), k)
    if rem != 0 or max(nums) > target:
        return False

    mapping = {1 << i: nums[i] for i in range(len(nums))}
    summ = [0] * (1 << len(nums))
    OPT = [False] * (1 << len(nums))
    OPT[0] = True
    for subset in xrange(1, 1 << len(nums)):
        mask = (subset & -subset)
        summ[subset] = summ[subset - mask] + mapping[mask]
        for i in range(len(nums)):
            mask = (1 << i)
            if subset & mask:
                if OPT[subset - mask] and nums[i] <= (summ[subset] - 1) % target + 1:
                    OPT[subset] = True
                    break
    return OPT[-1]

def partition_equal_sum_k_tablefilling_push(nums, k):
    nums.sort()
    target, rem = divmod(sum(nums), k)
    if rem or nums[-1] > target: return False

    OPT = [False] * (1 << len(nums))
    OPT[0] = True
    total = [0] * (1 << len(nums))

    for subset in xrange(1 << len(nums)):
        if not OPT[subset]: continue
        for i, num in enumerate(nums):
            mask = 1 << i
            child = subset | mask
            if subset == child:
                continue
            if not OPT[child] and num <= target - (total[subset] % target):
                OPT[child] = True
                total[child] = total[subset] + num
    return OPT[-1]

def partition_equal_sum_k(nums, k):
    nums.sort()
    total = sum(nums) 
    target = total / k
    if total % k != 0 or max(nums) > target:
        return False
    dest = (1 << len(nums)) - 1
    summ = {0: 0}
    visited = {0}
    front = [0]
    while front:
        subset = front.pop()
        for i, num in enumerate(nums):
            mask = (1 << i)
            if subset & mask == 0:
                child = subset | mask
                if child not in visited and num <= target - (summ[subset] % target):
                    if child == dest:
                        return True
                    summ[child] = summ[subset] + num
                    visited.add(child)
                    front.append(child)
    return False

def partition_equal_sum_k(nums, k):
    nums.sort()
    total = sum(nums) 
    target = total / k
    if total % k != 0 or max(nums) > target:
        return False
    mapping = {1 << i: nums[i] for i in range(len(nums))}
    dest = (1 << len(nums)) - 1
    summ = {0: 0}
    front = [0]
    while front:
        subset = front.pop()
        temp = subset ^ dest
        while temp:
            mask = temp & (-temp)
            num = mapping[mask]
            child = subset | mask
            if child not in summ and num <= target - (summ[subset] % target):
                if child == dest:
                    return True
                summ[child] = summ[subset] + num
                front.append(child)
            temp -= mask
    return False

# ~ Largest Divisible Subset ~
# OPT[i] size of largest divisible subset ending with in a[i]
# OPT[i] = max(OPT[j] + 1), 0 <= j < i and a[i] % a[j]
# OPT[0] = 1
# return OPT[n - 1]
# Time:  O(n^2)
# Space: O(n)
def largest_divisible_subset(nums):
    nums.sort()
    if not nums:
        return []
    OPT = [1] * len(nums)
    maximum, index = 0, 0
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                OPT[i] = max(OPT[j] + 1, OPT[i])
                if OPT[i] > maximum:
                    maximum, index = OPT[i], i
    result = []
    i = index
    while OPT[i] > 1:
        for j in range(i - 1, -1, -1):
            if OPT[i] == OPT[j] + 1 and nums[i] % nums[j] == 0:
                result.append(nums[i])
                break
        i = j
    result.append(nums[i])
    return result

# ~ Ugly Number II ~
# This is no DP, this is just a clever 3-way merge soert
# OPT[n] = max(OPT[i] * 2, OPT[j] * 3, OPT[k] * 5)
# For example if we have calculated the first 7 ugly numbers, then we have
#  2  4  6  8 10 12 16
#  3  6  9 12 15 18 24
#  5 10 15 20 25 30 40
# We maintain the pointers i, j, k on the three lanes, then we get
# 10 12 16
#  9 12 15 18 24
# 10 15 20 25 30 40
from collections import deque
import heapq
def ugly_num_ii(n):
    front = [(1, 0), (1, 1), (1, 2)]
    ugly = [2, 3, 5]
    queue = [deque() for _ in range(len(ugly))]
    for i in range(n):
        top = front[0][0]
        for i in range(len(ugly)):
            queue[i].append(top * ugly[i])
        while front[0][0] == top:
            _, idx = heapq.heappop(front)
            heapq.heappush(front, (queue[idx].popleft(), idx))
    return top

# ~ # of Longest Increasing Subseq ~
# OPT[i]: length of longest increasing subseq ending with a[i]
# OPT[i] = max(OPT[j] + 1), 0 <= j < i and a[j] < a[i]
# OPT[0] = 1
# return ...
# Time:  O(n^2)
# Space: O(n)
def cnt_longest_inc_subseq(nums):
    OPT = [1] * len(nums)
    cnt = [1] * len(nums)
    maximum = 0
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                if OPT[j] + 1 > OPT[i]:
                    OPT[i] = OPT[j] + 1
                    cnt[i] = cnt[j]
                elif OPT[j] + 1 == OPT[i]:
                    cnt[i] += cnt[j]
        maximum = max(OPT[i], maximum)
    total = 0
    for i in range(len(cnt)):
        if OPT[i] == maximum:
            total += cnt[i]
    return total

# ~ Word Break ~
# OPT[i]: is breakable s [0: i]
# OPT[i] = any(OPT[j] and s[j: i] in wordDict), 0 <= j < i
# OPT[0] = True
# return OPT[n]
# Time:  O(n^2)
# Space: O(n)
def word_break(s, wordDict):
    wordDict = set(wordDict)
    OPT = [False] * (len(s) + 1)
    OPT[0] = True
    candidates = [0]
    for i in range(1, len(s) + 1):
        OPT[i] = any(OPT[j] and s[j: i] in wordDict for j in candidates)
        if OPT[i]:
            candidates.append(i)
    return OPT[-1]

# ~ Maximal Square ~
# OPT[i][j]: maximum square ending with a[i][j]
# OPT[i][j] = max(OPT[i - 1][j], OPT[i][j - 1], OPT[i - 1][j - 1]) + 1
# OPT[0][j] = (a[i][j] == 1)
# OPT[i][0] = (a[i][j] == 1)
# return max(max(line) for line in OPT)
# Time:  O(n^2)
# Space: O(n)
def max_square(matrix):
    if not matrix:
        return 0
    prev = [0] * len(matrix[0])
    OPT = map(eval, matrix[0])
    maximum = max(OPT)
    for i in range(1, len(matrix)):
        prev, OPT = OPT, [0] * len(matrix[0])
        for j in range(len(matrix[0])):
            if j == 0:
                OPT[j] = int(matrix[i][j] == "1")
            elif matrix[i][j] == "1":
                OPT[j] = min(OPT[j - 1], prev[j], prev[j - 1]) + 1
            maximum = max(OPT[j], maximum)
    return maximum ** 2

# ~ Min Swap Make Sequences Inc ~
# OPT[i][?]: min swap to make sequences [0, i] increasing given swap last or not
# OPT[i][?] = min(OPT[i-1]) + (? == True)   { if can choose}
# OPT[i][?] = OPT[i-1][?] + (? == True)     { if cannot swap}
# OPT[i][?] = OPT[i-1][not ?] + (? == True) { if must swap}
# OPT[0][?] = 0
# return min(OPT[n - 1])
# Time:  O(n)
# Space: O(n)
def min_swap(A, B):
    OPT = [[0, 1] for i in range(len(A))]
    for i in range(1, len(A)):
        if A[i-1] < A[i] and A[i-1] < B[i] and B[i-1] < B[i] and B[i-1] < A[i]:
            OPT[i][False] = min(OPT[i - 1][True], OPT[i - 1][False])
            OPT[i][True] = OPT[i][False] + 1
        elif not A[i-1] < A[i] or not B[i-1] < B[i]:
            OPT[i][False] = OPT[i - 1][True]
            OPT[i][True] = OPT[i - 1][False] + 1
        else:
            OPT[i][False] = OPT[i - 1][False]
            OPT[i][True] = OPT[i - 1][True] + 1
    return min(OPT[-1])

# ~ Cheapest Flight Within K Stops ~
# Something like bellman-ford
# OPT[k][i]: shortest path within k stops starting from src, ending with a[i]
# OPT[k][i] = min(OPT[k - 1][j] + edge[j][i])
# OPT[0][i] = edge[src][i]
# return min(OPT[k][dst] for k in range(K))
# Time:  O(VK)
# Space: O(VK)
def cheapest_flight(n, flights, src, dst, K):
    OPT = [[float("inf")] * n for k in range(K + 1)]
    for u, v, w in flights:
        if u == src:
            OPT[0][v] = w
    for k in range(1, K + 1):
        #for i in range(n):
            #for j in range(n):
                #if (i, j) in edges:
        for u, v, w in flights:
            OPT[k][v] = min(OPT[k - 1][u] + w, OPT[k][v])
    result = min(OPT[k][dst] for k in range(K + 1))
    return result if result != float("inf") else -1

# ~ Maximum Product Subarray ~
# OPT[?][i]: maximum/minimum product subarray ending with a[i]
# OPT[T][i] = max(OPT[T][i - 1], 1) * a[i] if a[i] >= 0
# OPT[T][i] = min(OPT[F][i - 1], 1) * a[i] else
# OPT[F][i] = min(OPT[F][i - 1], 1) * a[i] if a[i] >= 0
# OPT[F][i] = max(OPT[T][i - 1], 1) * a[i] else
# OPT[i] = min(OPT[i - 1], 1) * a[i] else
# OPT[0] = a[i]
# return max(OPT[True])
# Time:  O(n)
# Space: O(n)
def maximum_proc_subarr(nums):
    if not nums:
        return 0
    OPT = [[0] * len(nums) for i in range(2)]
    OPT[True][0] = OPT[False][0] = nums[0]
    for i in range(1, len(nums)):
        if nums[i] >= 0:
            OPT[True][i] = max(OPT[True][i - 1], 1) * nums[i]
            OPT[False][i] = min(OPT[False][i - 1], 1) * nums[i]
        else:
            OPT[True][i] = min(OPT[False][i - 1], 1) * nums[i]
            OPT[False][i] = max(OPT[True][i - 1], 1) * nums[i]
    return max(OPT[True])

# ~ Coin Change ~
# OPT[i]: fewest amount of money to make up i
# OPT[i] = min(OPT[i - coin[k]]) + 1
# OPT[0] = 0
# return OPT[n]
# Time:  O(kn)
# Space: O(n)
def coin_change(coins, amount):
        OPT = [float("inf")] * (amount + 1)
        OPT[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    OPT[i] = min(OPT[i - coin] + 1, OPT[i])
        return OPT[-1] if OPT[-1] != float("inf") else -1

# ~ Knight Probability ~
# OPT[k][pos]: probability of ending in pos after k moves
# OPT[k][pos] = sum(OPT[k-1][ppos] / 8.0), prev knight move to pos
# OPT[0][(r, c)] = 1
# return sum(OPT[K])
# Time:  O(kn^2)
# Space: O(n^2)
def knight_probability(N, K, r, c):
    OPT = [[0] * N for _ in range(N)]
    OPT[r][c] = 1
    moves = [(2,1),(1,2),(2,-1),(1,-2),(-2,1),(-1,2),(-2,-1),(-1,-2)]
    for k in range(1, K + 1):
        prev, OPT = OPT, [[0] * N for _ in range(N)]
        for row in range(N):
            for col in range(N):
                for move in moves:
                    ppos = (row - move[0], col - move[1])
                    if 0 <= ppos[0] < N and 0 <= ppos[1] < N:
                        OPT[row][col] += prev[ppos[0]][ppos[1]] / 8.0
    return sum(OPT[row][col] for row in range(N) for col in range(N))

def knight_probability_bfs(N, K, r, c):
    front = [(r, c)]
    OPT = [[0] * N for _ in range(N)]
    OPT[r][c] = 1
    moves = [(2,1),(1,2),(2,-1),(1,-2),(-2,1),(-1,2),(-2,-1),(-1,-2)]
    for i in range(K):
        children = []
        prev, OPT = OPT, [[0] * N for _ in range(N)]
        for node in front:
            for move in moves:
                child = (node[0] + move[0], node[1] + move[1])
                if 0 <= child[0] < N and 0 <= child[1] < N:
                    if OPT[child[0]][child[1]] is 0:
                        children.append(child)
                    OPT[child[0]][child[1]] += prev[node[0]][node[1]] / 8.0
        front = children
    return sum(OPT[row][col] for row in range(N) for col in range(N))

# ~ Out of Boundary ~
# OPT[k][pos]: path to pos within k moves
# OPT[k][pos] = sum(OPT[k-1][ppos]), ppos can move to pos
# OPT[0][(i, j)] = 1
# return sum(OPT[K]) % prime
# Time:  O(kmn)
# Space: O(mn)
def out_of_boundary(m, n, N, i, j):
    OPT = [[0] * n for _ in range(m)]
    OPT[i][j] = 1
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    result = 0
    for k in range(N):
        prev, OPT = OPT, [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for move in moves:
                    child = (i + move[0], j + move[1])
                    if 0 <= child[0] < m and 0 <= child[1] < n:
                        OPT[child[0]][child[1]] += prev[i][j]
                    elif child[0] < 0 or child[0] >= m or child[1] < 0 or child[1] >= n:
                        result += prev[i][j]
    prime = 10 ** 9 + 7
    return result % prime

def out_of_boundary_bfs(m, n, N, i, j):
    OPT = [[0] * n for _ in range(m)]
    OPT[i][j] = 1
    front = [(i, j)]
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    result = 0
    for i in range(N):
        prev, OPT = OPT, [[0] * n for _ in range(m)]
        children = []
        for node in front:
            for move in moves:
                child = (node[0] + move[0], node[1] + move[1])
                if 0 <= child[0] < m and 0 <= child[1] < n:
                    if OPT[child[0]][child[1]] is 0:
                        children.append(child)
                    OPT[child[0]][child[1]] += prev[node[0]][node[1]]
                elif child[0] < 0 or child[0] >= m or child[1] < 0 or child[1] >= n:
                    result += prev[node[0]][node[1]]
        front = children
    prime = 10 ** 9 + 7
    return result % prime
