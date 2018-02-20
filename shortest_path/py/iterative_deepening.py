def iterative_deepening(adjList, source, target, max_depth = 10000):
    for limit in range(1, max_depth + 1):
        result = depth_limited(adjList, source, target, limit)
        if result:
            return result

def depth_limited(adjList, source, target, limit):
    stack = [(source, 0)]
    dist = {source: 0}
    prev = {source: None}
    while stack:
        node, level = stack.pop()
        if node is target:
            return dist, prev
        if level >= limit:
            continue
        for child in adjList[node]:
            stack.append((child, level + 1))
            dist[child] = level + 1
            prev[child] = node
    return None

# Verified
def depth_limited_recursive(adjList, source, target, limit):
    def helper(source, target, limit, path, result):
        if source is target:
            result.append(list(path))
            return result
        elif limit <= 0 or source in visited:
            return result
        visited.add(source)

        for child in adjList[source]:
            path.append(child)
            if helper(child, target, limit - 1, path, result):
                return result
            path.pop()
        return result
    visited = set()
    return helper(source, target, limit, [source], [])
