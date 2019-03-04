# OPT[subset][i]: best utility of arranging subset ending with a[i]
# OPT[subset][i] = max(OPT[subset-{i}][j] + dist[j][i]), j in subset-{i}
# OPT[subset+{j}][j] = max(OPT[subset][i] + dist[i][j], OPT[subset+{j}][j])
#     j not in subset
# OPT[{i}][i] = 0
# return max(OPT[universe])

def seat_arrangement(dist):
    OPT = [[0] * len(dist) for _ in range(1 << len(dist))]
    front = []
    for i in range(len(dist)):
        OPT[1 << i][i] = 0
        front.append((1 << i, i))
    while front:
        children = []
        for subset, i in front:
            for j in range(len(dist)):
                mask = (1 << j)
                if mask & subset == 0:
                    child = subset | mask
                    if OPT[child][j] == 0:
                        children.append((child, j))
                    if OPT[subset][i] + dist[i][j] > OPT[child][j]:
                        OPT[child][j] = OPT[subset][i] + dist[i][j]
        front = children
    subset = (1 << len(dist)) - 1
    return max(OPT[subset])

def seat_arrangement_(dist):
    OPT = [[0] * len(dist) for _ in range(1 << len(dist))]
    for subset in range(1 << len(dist)):
        ones  = filter(lambda i: subset & (1 << i) != 0, range(len(dist)))
        zeros = filter(lambda j: subset & (1 << j) == 0, range(len(dist)))
        for i in ones:
            for j in zeros:
                child = subset | (1 << j)
                OPT[child][j] = max(OPT[subset][i] + dist[i][j], OPT[child][j])
    subset = (1 << len(dist)) - 1
    return max(OPT[subset])
