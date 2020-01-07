import random

class RandomGraph:
    def randomGnmGraph(self, n = 100, M = 3000,
            isDirected = False,
            isWeighted = False, wRange = 11):
        if not isDirected:
            M *= 2
        if M > n * (n - 1):
            raise ValueError("Number of edges greater than sq of nodes")
        if isWeighted:
            return self.gnmGraphWeighted(n, M, isDirected, wRange)
        else:
            return self.gnmGraphUnweighted(n, M, isDirected)

    def gnmGraphUnweighted(self, n, M, isDirected):
        adjList = { node: set() for node in range(n) }
        nEdges = 0
        while nEdges < M:
            u, v = random.randrange(n), random.randrange(n)
            if u != v and v not in adjList[u]:
                adjList[u].add(v)
                if not isDirected:
                    adjList[v].add(u)
                    nEdges += 1
                nEdges += 1
        return adjList

    def gnmGraphWeighted(self, n, M, isDirected, wRange):
        adjList = { node: set() for node in range(n) }
        edges = set()
        while len(edges) < M:
            u, v = random.randrange(n), random.randrange(n)
            if u != v and (u, v) not in edges and \
                    (not isDirected or (v, u) not in edges):
                w = random.randrange(1, wRange)
                adjList[u].add((v, w))
                edges.add((u, v))
                if not isDirected:
                    adjList[v].add((u, w))
                    edges.add((v, u))
        return adjList

    def randomGnpGraph(self, n = 100, p = 0.3,
            isDirected = False,
            isWeighted = False, wRange = 10):
        adjList = { node: set() for node in range(n) }
        for u in range(n - 1):
            for v in range(i + 1, n):
                if random.random() < p:
                    adjList[u].add((v, w) if isWeighted else v)
                    if not isDirected:
                        adjList[v].add((u, w) if isWeighted else u)
        return adjList

    def toNodeEdges(self, adjList):
        nodes = list(adjList.keys())
        edges = []
        for u in adjList:
            for v, w in adjList[u]:
                edges.append((u, v, w))
        return nodes, edges

    def toWeighted(self, adjList):
        weighted = { node: set() for node in range(len(adjList)) }
        for u in adjList:
            for v in adjList[u]:
                weighted[u].add((v, 1))
        return weighted
