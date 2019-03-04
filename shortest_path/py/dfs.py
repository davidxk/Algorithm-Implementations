
def dfs(adjList, source):
    stack = [source]
    parent = {source: None}
    while stack:
        node = stack.pop()
        for child in adjList[source]:
            if child not in parent:
                stack.append(child)
                parent[child] = node
    return parent
