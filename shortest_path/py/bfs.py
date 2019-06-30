from collections import deque

# Tested
def bfs(adjList, source):
    front = deque([source])
    dist = {source: 0}
    prev = {source: None}
    while front:
        node = front.popleft()
        for child in adjList[node]:
            if child not in dist:
                front.append(child)
                dist[child] = dist[node] + 1
                prev[child] = node
    return dist, prev

def bfs_template_1(adjList, source):
    front = deque([source])
    visited = {source}
    while front:
        node = front.popleft()
        # Do something here
        for child in adjList[node]:
            if child not in visited:
                front.append(child)
                visited.add(child)
    return None

# Verified
def bfs_template_2(adjList, source):
    front = [source]
    visited = {source}
    while front:
        children = []
        for node in front:
            # Do something here
            for child in adjList[node]:
                if child not in visited:
                    children.append(child)
                    visited.add(child)
        front = children
    return None
