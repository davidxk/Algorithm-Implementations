# These problems have n! permutation search space, n2^n sub-problems

# ~ Android Unlock Patterns ~
# OPT[subset][i]: # of patterns consist of subset and ending with a[i]
# OPT[subset][i] = sum(OPT[subset-{i}][j]), j in subset-{i} and j in adjList[i]
# OPT[{i}][i] = 1
# return sum(sum(OPT[subset]) for subset that n <= len(subset) <= m)
# Time:  O(n2^n)
# Space: O(n2^n)
def android_unlock_patterns(m, n):
    OPT = [[0] * 9 for _ in range(1 << 9)]
    magic = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    mid = {(i, k): 1 << j for i, j, k in magic}
    for i, j, k in magic:
        mid[(k, i)] = mid[(i, k)]
    test = lambda i, j, subset: (i, j) not in mid or subset & mid[(i, j)]

    front = []
    for i in range(9):
        OPT[1 << i][i] = 1
        front.append((subset, i))

    mapping = {1 << i: i for i in range(9)}
    result, cntOnes = 0, 1
    while front:
        children = []
        if m <= cntOnes <= n:
            for subset, i in front:
                result += OPT[subset][i]
            if cntOnes == n:
                break
        for subset, i in front:
            for j in range(9):
                mask = (1 << j)
                if mask & subset == 0 and test(i, j, subset): 
                    child = subset | mask
                    if OPT[child][j] == 0:
                        children.append((child, j))
                    OPT[child][j] += OPT[subset][i]
        front = children
        cntOnes += 1
    return result

# ~ Shortest Path Through All Nodes ~
# OPT[subset][i]: len of shortest through all nodes of subset ending with a[i]
# OPT[subset][i] = min(OPT[subset-{i}][j] + dist[j][i]), j in subset-{i}
# OPT[{i}][i] = 1
# return min(OPT[universe])
# Time:  O(n2^n)
# Space: O(n2^n)
def shortest_path_thru_all_nodes(graph):
    # Floyd Warshall
    dist = [[len(graph)] * len(graph) for _ in graph]
    for i in range(len(graph)):
        for j in graph[i]:
            dist[i][j] = 1
        dist[i][i] = 0
    for k in range(len(graph)):
        for j in range(len(graph)):
            for i in range(len(graph)):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    # Initialize OPT
    MAX = 1 << len(graph)
    front = []
    OPT = [[MAX] * len(graph) for _ in range(1 << len(graph))]
    for i in range(len(graph)):
        OPT[1 << i][i] = 0
        front.append((1 << i, i))
    # Level order BFS
    while front:
        children = []
        for subset, i in front:
            for j in range(len(graph)):
                mask = (1 << j)
                if mask & subset == 0:
                    child = subset | mask
                    if OPT[child][j] == MAX:
                        children.append((child, j))
                    OPT[child][j] = min(OPT[subset][i] + dist[i][j], OPT[child][j])
        front = children
    return min(OPT[(1 << len(graph)) - 1])

# ~ Seat Arrangement in a Row ~
# OPT[subset][i]: best utility of arranging subset ending with a[i]
# OPT[subset][i] = max(OPT[subset-{i}][j] + dist[j][i]), j in subset-{i}
# OPT[{i}][i] = 0
# return max(OPT[universe])
def seat_arrangement(matrix):
    # Initialize OPT
    front = []
    OPT = [[0] * len(matrix) for _ in range(1 << len(matrix))]
    then = [[None] * len(matrix) for _ in range(1 << len(matrix))]
    for i in range(len(matrix)):
        OPT[1 << i][i] = 0
        front.append((1 << i, i))
    # Level order BFS
    while front:
        children = []
        for subset, i in front:
            for j in range(len(matrix)):
                mask = (1 << j)
                if mask & subset == 0:
                    child = subset | mask
                    if OPT[child][j] == 0:
                        children.append((child, j))
                    if OPT[subset][i] + matrix[i][j] > OPT[child][j]:
                        OPT[child][j] = OPT[subset][i] + matrix[i][j]
                        then[child][j] = (subset, i)
        front = children
    subset = (1 << len(matrix)) - 1
    i = max(range(len(matrix)), key=lambda i: OPT[subset][i])
    result = [i]
    while then[subset][i]:
        subset, i = then[subset][i]
        result.append(i)
    return result

# ~ Can I Win ~
# OPT[subset][i]: the game played till subset with ending move a[i]
# if sum(subset) < target and sum(subset) + a[i] >= target
#     OPT[subset][i] = (subset) % 2
# else {sum(subset) + a[i] < target}
#     OPT[subset][i] = None
def can_i_win(maxInt, target):
        #maxInt, target = maxChoosableInteger, desiredTotal
        def cntOnes(num):
            cnt = 0
            while num:
                num -= num & (-num)
                cnt += 1
            return cnt
        summ = [0] * (1 << maxInt)
        nums = range(1, maxInt + 1)
        for subset in range(1 << maxInt):
            for i in range(maxInt):
                mask = 1 << i
                if subset & mask == 0:
                    summ[subset | mask] = summ[subset] + nums[i]
                else:
                    if summ[subset ^ mask] < target and summ[subset] >= target:
                        if cntOnes(subset) % 2 == 0:
                            return False
        return True

print can_i_win(10, 11), False
print can_i_win(4, 6), True
