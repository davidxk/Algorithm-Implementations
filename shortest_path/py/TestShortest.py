import unittest
import random
from random_graph import RandomGraph
from bfs import bfs
from dijkstra import dijkstra
from bellman_ford import bellman_ford
from floyd_warshall import floyd_warshall

class TestShortest(unittest.TestCase):
    def setUp(self):
        self.randG = RandomGraph()

    def testUnweighted(self):
        for i in range(50):
            adjList = self.randG.randomGnmGraph(n=50, M=1000, isWeighted=False, isDirected=False)
            src = random.choice(adjList.keys())
            dist1, prev1 = bfs(adjList, src)
            adjList = self.randG.toWeighted(adjList)
            dist3, prev3 = dijkstra(adjList, src)
            self.assertEqual(dist1, dist3)

    @unittest.skip("for testing bfs and bidirectional")
    def testWeighted(self):
        for i in range(50):
            adjList = self.randG.randomGnmGraph(n=50, M=1000, isWeighted=True)
            nodes, edges = self.randG.toNodeEdges(adjList)
            src = random.choice(adjList.keys())
            dist1, prev1 = dijkstra(adjList, src)
            dist2, prev2 = bellman_ford(nodes, edges, src)
            self.assertEqual(dist1, dist2)

    @unittest.skip("for testing bfs and bidirectional")
    def testAllPairs(self):
        for i in range(50):
            adjList = self.randG.randomGnmGraph(n=50, M=1000, isWeighted=True)
            nodes, edges = self.randG.toNodeEdges(adjList)
            src = random.choice(adjList.keys())
            dist1, prev1 = dijkstra(adjList, src)
            dist2 = floyd_warshall(nodes, edges)
            self.assertEqual(dist1, dist2[src])

if __name__ == "__main__":
    unittest.main()
