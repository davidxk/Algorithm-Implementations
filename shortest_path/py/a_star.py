from heapq import heapq

def trivial_heuristic(state):
    """
    Admissible: Optimistic, heuristic is an underestimate of the cost to goal
                A* is optimal when h(n) is admissible
    Consistent: Heuristic cost between every two nodes in an underestimate
                Consistency is required only for graph search

    In general, most natural admissbile heuristics tend to be consistent,
    especially if from relaxed problems
    """
    return 0

def a_star_search(adjList, source, dest, heuristic):
    """
    f(n) = g(n) + h(n)
    Estimated cost of cheapest solution throught node n
    """
    front = [(0, source)]
    parent = {}
    visited = set()
    dist = { source: 0 }
    while front:
        d, node = heapq.heappop(front)
        visited.add(node)
        if node == dest:
            return parent
        for child, weight in adjList[node]:
            if child not in visited:
                newdist = dist[node] + weight
                if child in dist and dist[child] < newdist:
                    continue
                dist[child] = newdist
                heapq.heappush(front,
                        (dist[child] + heuristic(child, dest), child))
                parent[child] = node
    return None
