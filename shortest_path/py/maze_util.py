from random import *

def coord_to_imagepos(coord):
    return map(lambda x: 2 * x + 1, coord)

def print_maze(ways, rows, cols):
    maze = [["#"] * (2 * cols + 1) for i in range(2 * rows + 1)]
    for way in ways:
        coordA, coordB = way
        posA, posB = coord_to_imagepos(coordA), coord_to_imagepos(coordB)
        posWay = (coordA[0] + coordB[0] + 1, coordA[1] + coordB[1] + 1)
        for pos in (posA, posB, posWay):
            row, col = pos
            maze[row][col] = ' '
    for i, line in enumerate(maze):
        maze[i] = str().join(line)
    return maze

class UnionFind:
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

class RandomizedSet:
    def __init__(self, array = []):
        self.array = array

    def add(self, elem):
        self.array.append(elem)

    def pop_random(self):
        index = randrange(len(self.array))
        self.array[index], self.array[-1] = self.array[-1], self.array[index]
        return self.array.pop()
