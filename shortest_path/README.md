# Shortest path problem
* The **single-source shortest path problem**, in which we have to find shortest paths from a source vertex v to all other vertices in the graph.
* The **all-pairs shortest path problem,** in which we have to find shortest paths between every pair of vertices v, v' in the graph.

| Algorithm | type | Graph type | Weighted | Graph representation | Time complexity |
|-----------|------|------------|----------|----------------------|-----------------|
| DFS | Single-source shortest paths | tree | weighted | tree | $O(V + E)$ |
| Viterbi | Single-source shortest paths | graph | weighted dag | adjacency list | $O(V + E)$ |
| BFS | Single-source shortest paths | graph | unweighted | adjacency list | $O(V + E)$ |
| Dijkstra's | Single-source shortest paths | graph | weighted+ | adjacency list | $O(E \log V)$ $O(E + V \log V)$ |
| Bellman-Ford | Single-source shortest paths | graph | weighted | set of $V$ & $E$ | $O(VE)$ |
| SPFA | Single-source shortest paths | graph | weighted | adjacency list | $O(E)$ |
| Floyd-Warshall | All-pairs shortest paths | graph | weighted | set of $V$ & $E$ | $O(V^3)$ |
| Johnson's | All-pairs shortest paths | graph | weighted | adjacency list | $O(V^2\log V + VE)$ |

Note that

> * BFS is Dijkstra in unweighted graph

# Is DAG
* Topological sort
* DFS based algorithm

# Uninformed Search
Elements of a search problem:

* States
* Initial state
* Actions
* Transition model
* Goal test
* Path cost

A solution to a problem is an action sequence (a plan) that leads from the initial state to a goal state. Solution quality is measured by the path *cost function*, and an OPTIMAL SOLUTION has the lowest path cost among all solutions.

* Completeness: Is the algorithm guaranteed to find a solution when there is one?
* Optimality: Does the strategy find the optimal solution, as defined above?


| Algorithm | Time Complexity | Space Complexity | Complete | Optimal |
|---------------------|--------------|--------------|-----|-----|
| BFS                 | $O(b^d)$     | $O(b^d)$     | Yes | Yes |
| Uniform Cost search | $O(b^{C/u})$ | $O(b^{C^*/u})$ | Yes | Yes |
| Backward search     | $O(\bar b^d)$| $O(\bar b^d)$| Yes | Yes |
| Bidirectional       | $O(b^{d/2})$ | $O(b^{d/2})$ | Yes | Yes |
| Depth Limited       | $O(b^l)$     | $O(bl)$      | No  | No  |
| Iterative Deepening | $O(b^d)$     | $O(bd)$      | Yes | Yes |

* $b$: branching factor
* $\bar b$: branching factor backwards
* $l$: depth limit
* $d$: depth of the shallowest solution
* $C^*$: cost of the optimal solution
* $u$: minimum action cost

Note that

> * Backward search is faster when the branching factor backwards is smaller
> * Bidirectional is a faster version of BFS when backward expansion is possible
> * Depth Limited takes advantage of the knowledge of $d$'s upper bound $l$
> * Iterative Deepening is a complete search algorithm that is space efficient
> * Dijkstra's variant for uninformed search is called uniform cost search where it stops at the goal state instead of going through the entire search tree

# Informed Search
