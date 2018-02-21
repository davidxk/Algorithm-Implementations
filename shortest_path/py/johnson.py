# Intuition: Make each edge positive while preserve s-t path length ordering
# Observation: w + Pu - Pv -> L + Ps - Pt does not change path length ordering
# Claim: Use shortest path distance as P will make weights positive

from bellman_ford import bellman_ford
from dijkstra import dijkstra

def johnson(nodes, edges):
    sentinel = -1
    for node in nodes:
        edges.append((sentinel, node, 0))
    nodes.append(sentinel)

    weights, prev = bellman_ford(nodes, edges, sentinel)
    if weights is None:
        return None, "Negative Cycle"
    nodes.pop()
    del edges[-len(nodes):]
    
    adjList = { node: [] for node in nodes }
    for u, v, w in edges:
        adjList[u].append((v, w + weights[u] - weights[v]))
    dist, prev = {}, {}
    for src in nodes:
        dist[src], prev[src] = dijkstra(adjList, src)
        for dest in dist[src]:
            dist[src][dest] -= (weights[src] - weights[dest])
    return dist, prev
