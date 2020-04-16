import random
import unittest
from bipartiteness import is_bipartite

class RandomGraph:
    def randomGnmGraph(self, n, M, isBipartite):
        adjList = { node: set() for node in range(n) }
        left = set(range(0, random.randrange(1, n)))
        if isBipartite and M > len(left) * (n - len(left)):
            raise ValueError("M > max edges in bipartite graph")
        cntEdge = 0
        while cntEdge < M:
            u, v = random.randrange(n), random.randrange(n)
            if v not in adjList[u] and u != v:
                if isBipartite and (u in left) == (v in left):
                    continue
                adjList[u].add(v)
                adjList[v].add(u)
                cntEdge += 1
        return adjList

class TestBipartiteness(unittest.TestCase):
    def testIsBipartite(self):
        gnm = RandomGraph()
        for _ in range(100):
            adjList = gnm.randomGnmGraph(50, 49, True)
            self.assertEqual(is_bipartite(adjList), True)

        for _ in range(100):
            adjList = gnm.randomGnmGraph(50, 1000, False)
            self.assertEqual(is_bipartite(adjList), False)

if __name__ == "__main__":
    unittest.main()
