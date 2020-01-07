import unittest
import random
from random_graph import RandomGraph
from bfs import bfs
from dijkstra import dijkstra
from bellman_ford import bellman_ford
from shortest_path_faster import shortest_path_faster
from floyd_warshall import floyd_warshall
from johnson import johnson

class TestShortest(unittest.TestCase):
    def setUp(self):
        self.randG = RandomGraph()

    def testUnweighted(self):
        for i in range(50):
            adjList = self.randG.randomGnmGraph(n=50, M=1000, isWeighted=False, isDirected=False)
            src = random.choice(list(adjList.keys()))
            dist1, prev1 = bfs(adjList, src)
            adjList = self.randG.toWeighted(adjList)
            dist3, prev3 = dijkstra(adjList, src)
            self.assertEqual(dist1, dist3)

    def testWeighted(self):
        for i in range(50):
            adjList = self.randG.randomGnmGraph(n=50, M=1000, isWeighted=True)
            nodes, edges = self.randG.toNodeEdges(adjList)
            src = random.choice(list(adjList.keys()))
            dist1, prev1 = dijkstra(adjList, src)
            dist2, prev2 = bellman_ford(nodes, edges, src)
            dist3, prev3 = shortest_path_faster(adjList, src)
            self.assertEqual(dist1, dist2)
            self.assertEqual(dist2, dist3)

    def testFloydWarshall(self):
        for i in range(50):
            adjList = self.randG.randomGnmGraph(n=50, M=1000, isWeighted=True)
            nodes, edges = self.randG.toNodeEdges(adjList)
            src = random.choice(list(adjList.keys()))
            dist1, prev1 = dijkstra(adjList, src)
            dist2, prev2 = floyd_warshall(nodes, edges)
            self.assertEqual(dist1, dist2[src])

    def testAllPairs(self):
        for i in range(50):
            adjList = self.randG.randomGnmGraph(n=50, M=1000, isWeighted=True)
            nodes, edges = self.randG.toNodeEdges(adjList)
            src = random.choice(list(adjList.keys()))
            dist1, prev1 = floyd_warshall(nodes, edges)
            dist2, prev2 = johnson(nodes, edges)
            self.assertEqual(dist1, dist2)

if __name__ == "__main__":
    print("These tests coult take up to 10 seconds to finish. ")
    unittest.main()
