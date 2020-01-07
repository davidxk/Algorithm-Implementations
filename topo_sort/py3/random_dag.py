import itertools
import random

def random_dag(size = 500, isWeighted = True):
    root = int(size ** 0.5)
    ranks = random.randrange(root // 2, root * 3 // 2)
    width = size // ranks
    lvlMin, lvlMax = width // 2, width * 3 // 2
    base = 0
    elders = []
    edges = []
    for rank in range(ranks):
        count = random.randrange(lvlMin, lvlMax)
        level = range(base, base + count)
        for u, v in itertools.product(elders, level):
            if random.random() < 0.1:
                if isWeighted:
                    edges.append((u, v, random.randrange(100)))
                else:
                    edges.append((u, v))
        elders += level
        base += count
    return edges
