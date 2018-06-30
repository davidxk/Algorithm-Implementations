import random
import unittest
from collections import defaultdict
from random_dag import random_dag
from topo_sort import viterbi_shortest_path, dp_shortest_path
from topo_sort import topo_sort, dfs_based

class TestTopoSort(unittest.TestCase):
    def testViterbi(self):
        for _ in range(50):
            edges = random_dag(isWeighted=True)
            dist1 = viterbi_shortest_path(edges)
            dist2 = dp_shortest_path(edges)
            self.assertEqual(dist1, dist2)

    def getReachableSet(self, adjList):
        def dfs(adjList, source):
            front = [source]
            visited = {source}
            while front:
                node = front.pop()
                for child in adjList[node]:
                    if child not in visited:
                        visited.add(child)
                        front.append(child)
            return visited
        reachable = defaultdict(list)
        for node in adjList.keys():
            reachable[node] = dfs(adjList, node)
        return reachable

    def getAdjList(self, edges):
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
        return adjList

    def __test_topo__(self, algo):
        for _ in range(50):
            edges = random_dag(50, isWeighted=False)
            array = algo(edges)
            adjList = self.getAdjList(edges)
            reachable = self.getReachableSet(adjList)
            for i in range(len(array)):
                for j in range(i + 1, len(array)):
                    self.assertNotIn(array[i], reachable[array[j]])

    def testTopoSort(self):
        self.__test_topo__(topo_sort)
        self.__test_cycle__(topo_sort)

    def testDFSBased(self):
        self.__test_topo__(dfs_based)
        self.__test_cycle__(dfs_based)

    def __test_cycle__(self, algo):
        for _ in range(10):
            edges = random_dag(100, isWeighted=False)
            edges = set(edges)
            length = random.randrange(10, 100)
            pool = range(100)
            random.shuffle(pool)
            cycle = pool[:length]
            for i in range(length):
                if (cycle[i - 1], cycle[i]) not in edges:
                    edges.add((cycle[i - 1], cycle[i]))
            self.assertEqual(algo(edges), [])

if __name__ == "__main__":
    print "This could take up to 5 seconds"
    unittest.main()
