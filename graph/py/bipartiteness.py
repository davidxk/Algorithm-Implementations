# Time:  O(V + E)
# Space: O(b^d)
# Has to test every connected component
def is_bipartite(adjList):
    layer = {}
    for node in range(len(adjList)):
        if node not in layer:
            if not self.bfs_alternate_test(adjList, node, layer):
                return False
    return True

def bfs_alternate_test(self, adjList, source, layer):
    front = [source]
    layer[source] = 0
    while front:
        children = []
        for node in front:
            for child in adjList[node]:
                if child in layer and layer[child] == layer[node]:
                    return False
                elif child not in layer:
                    children.append(child)
                    layer[child] = not layer[node]
        front = children
    return True
