from maze_util import print_maze
from maze_util import RandomizedSet

# Instead of picking the min weight edge in the frontier, pick randomly
# Tree generated with this method tends to be very balanced
def randomized_prim(rows, cols):
    visited = set([(0, 0)])
    edges = RandomizedSet([((0, 0), (0, 1)), ((0, 0), (1, 0))])
    dircs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    result = []
    while len(visited) < rows * cols:
        cell, neighbour = edges.pop_random()
        if (cell in visited) == (neighbour in visited):
            continue
        result.append((cell, neighbour))
        visited.add(neighbour)
        for dirc in dircs:
            nn = (neighbour[0] + dirc[0], neighbour[1] + dirc[1])
            if 0 <= nn[0] < rows and 0 <= nn[1] < cols and nn not in visited:
                edges.add((neighbour, nn))
    return result

if __name__ == '__main__':
    rows, cols = 10, 39
    ways = randomized_prim(rows, cols)
    maze = print_maze(ways, rows, cols)
    for line in maze:
        print line
