from collections import defaultdict

# Tested
def floyd_warshall(nodes, edges):
    dist = {node: defaultdict(lambda: float("inf")) for node in nodes}
    #dist = [[float("inf")] * len(nodes) for i in range(len(nodes))]
    then = [[None] * len(nodes) for i in range(len(nodes))]
    for v in nodes:
        dist[v][v] = 0
    for edge in edges:
        u, v, w = edge
        dist[u][v] = w
        then[u][v] = v
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    then[i][j] = then[i][k]
    return dist, then
