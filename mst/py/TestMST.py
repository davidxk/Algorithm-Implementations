import random
import unittest
from collections import defaultdict
from prim import prim
from kruskal import kruskal

class TestMST(unittest.TestCase):
    def testMST(self):
        size = 50
        for _ in range(100):
            adjList = defaultdict(list)
            edges = []
            cnt = 0
            weights = range(size * (size - 1) / 2)
            random.shuffle(weights)
            for i in range(size):
                for j in range(i + 1, size):
                    adjList[i].append((j, weights[cnt]))
                    adjList[j].append((i, weights[cnt]))
                    edges.append((i, j, weights[cnt]))
                    cnt += 1
            parent = prim(adjList)
            edges = kruskal(size, edges)
            self.assertEqual(len(edges) + 1, len(parent))
            for u, v in edges:
                self.assertTrue(parent[u] == v or parent[v] == u)

if __name__ == "__main__":
    unittest.main()
