from maze_util import print_maze
from maze_util import UnionFind
from maze_util import RandomizedSet

# Instead of picking edges using the greedy strategy, pick randomly
# Trees generated with this method can be truely random
def randomized_kruskal(rows, cols):
    # Represent all cells in union find
    uf = UnionFind()
    for i in range(rows):
        for j in range(cols):
            uf.make_set((i, j))
    # Add all edges in random set
    dircs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    edges = RandomizedSet()
    for i in range(rows):
        for j in range(cols):
            for dirc in dircs:
                if 0 <= i + dirc[0] < rows and 0 <= j + dirc[1] < cols:
                    edges.add(((i, j), (i + dirc[0], j + dirc[1])))
    # Randomly pick valid edges
    result = []
    while len(uf.size) > 1:
        cell, neighbour = edges.pop_random()
        if uf.find_set(cell) != uf.find_set(neighbour):
            result.append((cell, neighbour))
            uf.union(cell, neighbour)
    return result

if __name__ == '__main__':
    rows, cols = 10, 39
    ways = randomized_kruskal(rows, cols)
    maze = print_maze(ways, rows, cols)
    for line in maze:
        print line
