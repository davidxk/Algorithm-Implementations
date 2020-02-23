from collections import Counter
def is_tree(n, edges):
    indegree = Counter()
    for u, v in edges:
        indegree[v] += 1
    hasRoot = False
    for node in range(n):
        if indegree[node] > 1:
            return False
        elif indegree[node] == 0:
            if not hasRoot:
                hasRoot = True
            else:
                return False
    return hasRoot
