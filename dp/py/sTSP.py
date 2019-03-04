# ~ Seat Arrangement Round Table ~
# OPT[{i}][i] = dist[A][i]
# return max(OPT[i] + dist[i][A])
def seat_arrangement_round(dist):
    OPT = [[0] * len(dist) for _ in range(1 << len(dist))]
    front = []
    for i in range(1, len(dist)):
        OPT[1 << i][i] = dist[0][i]
        front.append((1 << i, i))
    while front:
        children = []
        for subset, i in front:
            for j in range(1, len(dist)):
                mask = (1 << j)
                if mask & subset == 0:
                    child = subset | mask
                    if OPT[child][j] == 0:
                        children.append((child, j))
                    if OPT[subset][i] + dist[i][j] > OPT[child][j]:
                        OPT[child][j] = OPT[subset][i] + dist[i][j]
        front = children
    subset = (1 << len(dist)) - 1 - 1
    return max(map(lambda i: OPT[subset][i] + dist[i][0], range(len(dist))))

def seat_arrangement_round_(dist):
    """ Held & Karp, 1962 """
    n = len(dist) - 1
    OPT = [[0] * n for _ in range(1 << n)]
    for j in range(n):
        OPT[1 << j][j] = dist[-1][j]
    for subset in range(1 << n):
        ones  = filter(lambda i: subset & (1 << i) != 0, range(n))
        zeros = filter(lambda j: subset & (1 << j) == 0, range(n))
        for i in ones:
            for j in zeros:
                child = subset | (1 << j)
                OPT[child][j] = max(OPT[subset][i] + dist[i][j], OPT[child][j])
    subset = (1 << n) - 1
    return max(map(lambda i: OPT[subset][i] + dist[i][-1], range(n)))
