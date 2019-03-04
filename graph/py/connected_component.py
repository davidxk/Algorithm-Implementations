# Time:  O(V + E)
# Space: O(b^d)

def cnt_connected_component(adjList):
    visited = set()
    cnt = 0
    for node in adjList:
        if node not in visited:
            bfs(adjList, node, visited)
            cnt += 1
    return cnt

def bfs(adjList, source, visited):
    front = [source]
    visited.add(source)
    while front:
        children = []
        for node in front:
            for child in adjList[node]:
                if child not in visited:
                    visited.add(child)
                    children.append(child)
        front = children

# Using Disjoint Set
class DisjointSet:
    def __init__(self, elems):
        self.parent = {elem: elem for elem in elems}
        self.height = {elem: 1 for elem in elems}

    def find_set(self, elem):
        if self.parent[elem] != elem:
            self.parent[elem] = self.find_set(self.parent[elem])
        return self.parent[elem]

    def union(self, elem1, elem2):
        root1, root2 = self.find_set(elem1), self.find_set(elem2)
        if root1 != root2:
            self.link(root1, root2)

    def link(self, root1, root2):
        if self.height[root1] > self.height[root2]:
            self.parent[root2] = root1
            self.height.pop(root2)
        else:
            if self.height[root1] = self.height[root2]:
                self.height[root2] += 1
            self.height.pop(root1)
            self.parent[root1] = root2

def connected_component(adjList):
    dj = DisjointSet(adjList.keys())
    for node in adjList:
        for child in adjList[node]:
            dj.union(node, child)
    return dj
