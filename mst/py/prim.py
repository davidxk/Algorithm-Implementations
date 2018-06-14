# Time:  O(E log(V))

from collections import defaultdict
import heapq
def prim(adjList):
    source = 0
    dist = {source: 0}
    front = [(0, source, source)]
    parent = {}
    while len(parent) < len(adjList):
        _, daddy, node = heapq.heappop(front)
        if node in parent:
            continue
        parent[node] = daddy
        for child, weight in adjList[node]:
            if child not in dist or weight < dist[child]:
                dist[child] = weight
                heapq.heappush(front, (dist[child], node, child))
    return parent
