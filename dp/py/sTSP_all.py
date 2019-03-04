from collections import defaultdict

def get_path(OPT, then):
    def dfs(subset, i, buf, result):
        if not then[(subset, i)]:
            result.append(list(buf))
        for child, j in then[(subset, i)]:
            buf.append(j)
            dfs(child, j, buf, result)
            buf.pop()
        return result
    # Find all maximum in last row
    maximum = max(OPT[-1])
    front = filter(lambda i: OPT[-1][i] == maximum, range(len(OPT[-1])))
    # Track path by DFS from each max ending
    result = []
    subset = len(OPT) - 1
    for node in front:
        dfs(subset, node, [node], result)
    # Append stationary guest to each path
    lastGuest = len(OPT[0])
    for path in result:
        path.append(lastGuest)
    return result

def seat_arrangement_round(dist):
    n = len(dist) - 1
    OPT = [[0] * n for _ in range(1 << n)]
    then = defaultdict(list)
    for j in range(n):
        OPT[1 << j][j] = dist[-1][j]
    for subset in range(1 << n):
        ones  = filter(lambda i: subset & (1 << i) != 0, range(n))
        zeros = filter(lambda j: subset & (1 << j) == 0, range(n))
        for i in ones:
            for j in zeros:
                child = subset | (1 << j)
                if OPT[subset][i] + dist[i][j] > OPT[child][j]:
                    OPT[child][j] = OPT[subset][i] + dist[i][j]
                    then[(child, j)] = [(subset, i)]
                elif OPT[subset][i] + dist[i][j] == OPT[child][j]:
                    then[(child, j)].append((subset, i))
    return get_path(OPT, then)
