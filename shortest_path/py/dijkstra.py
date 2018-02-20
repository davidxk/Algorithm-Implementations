from heapq import *

# Tested
def dijkstra(adjList, source):
    front = [(0, source)]
    dist = {source: 0}
    prev = {source: None}

    while front:
        d, node = heappop(front)
        for child, weight in adjList[node]:
            if child not in dist or d + weight < dist[child]:
                dist[child] = d + weight
                heappush(front, (dist[child], child))
                prev[child] = node

    return dist, prev

# Verified
def dijkstra_template(adjList, source):
    front = [(0, source)]
    dist = {source: 0}
    while front:
        d, node = heappop(front)
        for child, weight in adjList[node]:
            if child not in dist or d + weight < dist[child]:
                dist[child] = d + weight
                heappush(front, (dist[child], child))
    return dist

def dijkstra_decrese_key(adjList, source):
    pass

def uniform_cost_search(adjList, source, dest):
    pass
