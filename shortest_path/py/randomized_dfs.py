import random
from maze_util import print_maze

# Instead of visiting each child in order, visit them in random order
# Maze generated with this method has very long paths
# Keep the complete call stack so that we can track the parent of each child
def randomized_dfs(rows, cols):
    start = (0, 0)
    stack = [start]
    visited = set()
    result = []
    dircs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while stack:
        # Do not pop root off or it will be hard to add edges
        node = stack[-1]
        visited.add(node)
        choices = []
        # Randomly choose unexplored direction
        for dirc in dircs:
            child = (node[0] + dirc[0], node[1] + dirc[1])
            isValid = (0 <= child[0] < rows and 0 <= child[1] < cols)
            if child not in visited and isValid:
                choices.append(child)
        if not choices:
            stack.pop()
            continue
        child = random.choice(choices)
        stack.append(child)
        result.append((node, child))
    return result

if __name__ == '__main__':
    rows, cols = 10, 39
    ways = randomized_dfs(rows, cols)
    maze = print_maze(ways, rows, cols)
    for line in maze:
        print line
