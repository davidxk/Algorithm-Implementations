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
    #return max(OPT[subset])
    i = max(range(len(matrix)), key=lambda i: OPT[subset][i])
    result = [i]
    while then[subset][i]:
        subset, i = then[subset][i]
        result.append(i)
    return result

# ~ Seat Arrangement Round Table ~
# Can be reduced to seat arrangement in a row. 
# A Row: ABCDE
# Round: ABCDEA
# Then run in-a-row on BCDE with
# OPT[{i}][i] = dist[A][i]
# return max(OPT[i] + dist[i][A])
def seat_arrangement_round(matrix):
    # Initialize OPT
    front = []
    OPT = [[0] * len(matrix) for _ in range(1 << len(matrix))]
    then = [[None] * len(matrix) for _ in range(1 << len(matrix))]
    for i in range(1, len(matrix)):
        OPT[1 << i][i] = matrix[0][i]
        front.append((1 << i, i))
    # Level order BFS
    while front:
        children = []
        for subset, i in front:
            for j in range(1, len(matrix)):
                mask = (1 << j)
                if mask & subset == 0:
                    child = subset | mask
                    if OPT[child][j] == 0:
                        children.append((child, j))
                    if OPT[subset][i] + matrix[i][j] > OPT[child][j]:
                        OPT[child][j] = OPT[subset][i] + matrix[i][j]
                        then[child][j] = (subset, i)
        front = children
    subset = (1 << len(matrix)) - 1 - 1
    i = max(range(len(matrix)), key=lambda i: OPT[subset][i] + matrix[i][0])
    #return max(map(lambda i: OPT[subset][i] + matrix[i][0], range(len(matrix))))
    result = [i]
    while then[subset][i]:
        subset, i = then[subset][i]
        result.append(i)
    return [0] + result + [0]

#print seat_arrangement_round([[0, 1, 1, 1], [1, 0, 2, 2], [1, 2, 0, 2], [1, 2, 2, 0]])
#print seat_arrangement_round([[0, 4, 1, 5], [4, 0, 8, 2], [1, 8, 0, 3], [5, 2, 3, 0]])
#print seat_arrangement_round([[0, 1, 3, 9, 6], [1, 0, 3, 7, 4], [3, 3, 0, 12, 4], [9, 7, 12, 0, 5], [6, 4, 4, 5, 0]])

# ~ Seat Arrangement Round Table All Solutions ~
from collections import defaultdict
def seat_arrangement_round_all(matrix):
    # Initialize OPT
    front = []
    OPT = [[0] * len(matrix) for _ in range(1 << len(matrix))]
    then = defaultdict(list)
    for i in range(1, len(matrix)):
        OPT[1 << i][i] = matrix[0][i]
        front.append((1 << i, i))
    # Level order BFS
    while front:
        children = []
        for subset, i in front:
            for j in range(1, len(matrix)):
                mask = (1 << j)
                if mask & subset == 0:
                    child = subset | mask
                    if OPT[child][j] == 0:
                        children.append((child, j))
                    if OPT[subset][i] + matrix[i][j] > OPT[child][j]:
                        OPT[child][j] = OPT[subset][i] + matrix[i][j]
                        then[(child, j)] = [(subset, i)]
                    elif OPT[subset][i] + matrix[i][j] == OPT[child][j]:
                        then[(child, j)].append((subset, i))
        front = children
    subset = (1 << len(matrix)) - 1 - 1
    maximum = 0
    front = []
    for i in range(len(matrix)):
        if OPT[subset][i] + matrix[i][0] > maximum:
            maximum = OPT[subset][i] + matrix[i][0]
            front = [i]
        elif OPT[subset][i] + matrix[i][0] == maximum:
            front.append(i)
    def dfs(subset, i, path, result, then):
        if not then[(subset, i)]:
            result.append(list(path))
        for child, j in then[(subset, i)]:
            path.append(j)
            dfs(child, j, path, result, then)
            path.pop()
        return result
    for node in front:
        result = dfs(subset, node, [node], [], then)
    return map(lambda path: [0] + path + [0], result)

print seat_arrangement_round_all([[0, 1, 1, 1], [1, 0, 2, 2], [1, 2, 0, 2], [1, 2, 2, 0]])
print seat_arrangement_round_all([[0, 4, 1, 5], [4, 0, 8, 2], [1, 8, 0, 3], [5, 2, 3, 0]])
print seat_arrangement_round_all([[0, 1, 3, 9, 6], [1, 0, 3, 7, 4], [3, 3, 0, 12, 4], [9, 7, 12, 0, 5], [6, 4, 4, 5, 0]])

# ~ Seat Arrangement Many Tables ~
# Reduced to Round Table
# OPT[subset]: highest utility arranging subset into tables
# OPT[subset] = max(OPT[subset-table] + round(table, k, i)), i in table

# ~ Seat Arrangement Movie ~
# OPT[subset][i]: best utility of arranging subset ending with a[i]
# OPT[subset][i] = max(OPT[subset-{i}][j] + dist[j][i] + dist[i][len(subset)])
# OPT[{i}][i] = dist[i][len(subset)]
# return max(OPT[len(subset) == n])
# Time:  O(C_n^n * n)

# ~ Seat Arrangement Grid ~
# Reduced to One Row
# OPT[subset][row perm] = max(OPT[subset-row][k perm] + util(k perm, row perm))
# k perm elements in subset - row

