import unittest
import random
from random_graph import RandomGraph
from bfs import bfs
from bidirectional import bidirectional
from iterative_deepening import iterative_deepening

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.randG = RandomGraph()

    def testBidirectional(self):
        for i in range(50):
            adjList = self.randG.randomGnmGraph(n=50, M=1000, isWeighted=False, isDirected=False)
            src = random.choice(list(adjList.keys()))
            dest = random.choice(list(adjList.keys()))
            dist1, prev1 = bfs(adjList, src)
            dist2, prev2 = bidirectional(adjList, src, dest)
            self.assertEqual(dist1[dest], dist2)

    def testIterativeDeepening(self):
        for i in range(50):
            adjList = self.randG.randomGnmGraph(n=50, M=1000, isWeighted=False, isDirected=False)
            src = random.choice(list(adjList.keys()))
            dest = random.choice(list(adjList.keys()))
            dist1, prev1 = bfs(adjList, src)
            dist2, prev2 = iterative_deepening(adjList, src, dest)
            self.assertEqual(dist1[dest], dist2[dest])

if __name__ == "__main__":
    unittest.main()
