import unittest;
from DisjointSet import DisjointSet
from DisjointSet import DisjointSetLinkBySize

class TestDisjointSet(unittest.TestCase):
    def testUnionFind(self):
        ds = DisjointSet(range(100))
        for i in range(100):
            ds.union(i, i % 5)
        for i in range(100):
            for j in range(i, 100):
                self.assertEqual(ds.find_set(i) == ds.find_set(j), i%5 ==j%5)

    def testDisjointSetLinkBySize(self):
        ds = DisjointSetLinkBySize(range(100))
        for i in range(100):
            ds.union(i, i % 5)
        for i in range(100):
            for j in range(i, 100):
                self.assertEqual(ds.find_set(i) == ds.find_set(j), i%5 ==j%5)

if __name__ == '__main__':
    unittest.main()
