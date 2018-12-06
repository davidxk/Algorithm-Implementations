from collections import Counter
from collections import defaultdict

# Verified and tested
def topo_sort(edges):
    """ Kahn, 1962 """
    adjList = defaultdict(list)
    indegree = Counter()
    for u, v in edges:
        adjList[u].append(v)
        indegree[u] = indegree[u]
        indegree[v] += 1

    front = [node for node in indegree if indegree[node] is 0]
    for node in front:
        indegree.pop(node)
    result = []
    while front:
        node = front.pop()
        result.append(node)
        for child in adjList[node]:
            indegree[child] -= 1
            if indegree[child] is 0:
                indegree.pop(child)
                front.append(child)
    return result if not indegree else []

def viterbi_shortest_path(edges):
    adjList = defaultdict(list)
    indegree = Counter()
    for u, v, w in edges:
        adjList[u].append((v, w))
        indegree[u] = indegree[u]
        indegree[v] += 1

    front = [node for node in indegree if indegree[node] is 0]
    dist = {node: 0 for node in front}
    while front:
        node = front.pop()
        for child, weight in adjList[node]:
            if child not in dist or dist[node] + weight < dist[child]:
                dist[child] = dist[node] + weight
            indegree[child] -= 1
            if indegree[child] is 0:
                indegree.pop(child)
                front.append(child)
    return dist

# Reverse the edges in the adjacency list
def dfs_based(edges):
    WHITE, GREY, BLACK = 0, 1, 2
    color = defaultdict(lambda: WHITE)
    result = []

    def visit(node):
        if color[node] is GREY:
            return []
        color[node] = GREY
        for child in adjList[node]:
            if color[child] is not BLACK:
                if not visit(child):
                    return []
        color[node] = BLACK
        result.append(node)
        return result

    adjList = defaultdict(list)
    for v, u in edges:
        adjList[u].append(v)
        adjList[v] = adjList[v]
    for node in adjList:
        if node not in color:
            if not visit(node):
                return []
    return result

def dp_shortest_path(edges):
    def visit(node):
        if node in dist:
            return dist[node]
        for child, weight in adjList[node]:
            dist[node] = min(visit(child) + weight, dist[node])
        if dist[node] == float("inf"):
            dist[node] = 0
        return dist[node]
    adjList = defaultdict(list)
    for v, u, w in edges:
        adjList[u].append((v, w))
    dist = defaultdict(lambda: float("inf"))
    for node in adjList.keys():
        visit(node)
    return dist
