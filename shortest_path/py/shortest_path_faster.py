from collections import deque, defaultdict

def shortest_path_faster(adjList, source):
    dist = defaultdict(lambda: float("inf"))
    dist[source] = 0
    prev = {source: None}
    front = deque([source])
    queue = {source}
    while front:
        node = front.popleft()
        queue.remove(node)
        for child, weight in adjList[node]:
            if dist[node] + weight < dist[child]:
                dist[child] = dist[node] + weight
                prev[child] = node
                if child not in queue:
                    front.append(child)
                    queue.add(child)
    return dist, prev
