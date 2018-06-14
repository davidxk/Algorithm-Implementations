# Time:  O(E + V log(E))
import heapq

def kruskal(n, edges):
    dset = DisjointSet(range(n))
    edges = map(lambda (u, v, w): (w, u, v), edges)
    heapq.heapify(edges)
    result = []
    while len(dset) > 1:
        w, u, v = heapq.heappop(edges)
        if dset.find_set(u) != dset.find_set(v):
            result.append((u, v))
            dset.union(u, v)
    return result

class DisjointSet:
    def __init__(self, elems = []):
        self.parent = { elem: elem for elem in elems }
        self.height = { elem: 1 for elem in elems }

    def make_set(self, elem):
        self.parent[elem] = elem
        self.height[elem] = 1

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
            # When same height, link root1 to root2
            if self.height[root1] == self.height[root2]:
                self.height[root2] += 1
            self.parent[root1] = root2
            self.height.pop(root1)

    def __len__(self):
        return len(self.height)
