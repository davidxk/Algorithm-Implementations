from collections import defaultdict

# Tested
def bellman_ford(nodes, edges, source):
    dist = defaultdict(lambda: float("inf"))
    #dist = [float("inf")] * len(nodes)
    prev = [None] * len(nodes)
    dist[source] = 0
    
    for i in range(1, len(nodes)):
        for edge in edges:
            u, v, w = edge
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u

    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return None, "Negative Cycle"

    return dist, prev
