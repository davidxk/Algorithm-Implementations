
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
            if self.parent[root1] == self.parent[root2]:
                self.height[root2] += 1
            self.parent[root1] = root2
            self.height.pop(root1)

    '''
    def elements(self):
        return self.parent.keys()

    from collections import defaultdict
    def partition(self):
        mapping = defaultdict(list)
        for child in parent:
            mapping[parent[child]].append(child)
        return mapping.values()

    def count(self):
        return len(self.height)
    '''

class DisjointSetLinkBySize:
    def __init__(self, elems = []):
        self.parent = { elem: elem for elem in elems }
        self.size = { elem: 1 for elem in elems }

    def make_set(self, elem):
        self.parent[elem] = elem
        self.size[elem] = 1

    def find_set(self, elem):
        if self.parent[elem] != elem:
            self.parent[elem] = self.find_set(self.parent[elem])
        return self.parent[elem]

    def union(self, elem1, elem2):
        root1, root2 = self.find_set(elem1), self.find_set(elem2)
        if root1 != root2:
            self.link(root1, root2)

    def link(self, root1, root2):
        if self.size[root1] < self.size[root2]:
            self.link(root2, root1)
        else:
            self.size[root1] += self.size[root2]
            self.size.pop(root2)
            self.parent[root2] = root1

    '''
    def elements(self):
        return self.parent.keys()

    def count(self):
        return len(self.size)

    from collections import defaultdict
    def partition(self):
        mapping = defaultdict(list)
        for child in self.parent:
            mapping[self.find_set(child)].append(child)
        return mapping.values()

    def component_size(self, elem):
        root = self.find_set(elem)
        return self.size[root]

    def max_size(self):
        return max(self.size.values()) if self.size else 0
    '''
