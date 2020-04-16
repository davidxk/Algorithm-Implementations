# Time:  O(V + E)
# Space: O(b^d)
# Has to test every connected component
def is_bipartite(adjList):
    color = {}
    for node in range(len(adjList)):
        if node not in color:
            if not dfs_alternate_test(adjList, node, color):
                return False
    return True

def dfs_alternate_test(adjList, source, color):
    front = [source]
    color[source] = 0
    while front:
        node = front.pop()
        for child in adjList[node]:
            if child in color and color[child] == color[node]:
                return False
            elif child not in color:
                front.append(child)
                color[child] = not color[node]
    return True
