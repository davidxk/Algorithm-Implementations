import unittest
import random
from connected_component import cnt_connected_component, cnt_connected_component_dj

class TestConnectedComponent(unittest.TestCase):
    def randomGnmGraph(self, n, M):
        adjList = { node: set() for node in range(n) }
        if M > n * (n - 1) / 2:
            raise ValueError("Impossible number of edges")
        cntEdge = 0
        while cntEdge < M:
            u, v = random.randrange(n), random.randrange(n)
            if v not in adjList[u] and u != v:
                adjList[u].add(v)
                adjList[v].add(u)
                cntEdge += 1
        return adjList

    def testConnectedComponent(self):
        for _ in range(100):
            adjList = self.randomGnmGraph(50, 70)
            cnt1 = cnt_connected_component(adjList)
            cnt2 = cnt_connected_component_dj(adjList)
            self.assertEqual(cnt1, cnt2)

if __name__ == "__main__":
    unittest.main()
