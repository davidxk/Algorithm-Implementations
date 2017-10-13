## Equivalence Relation
An equivalence relation is a relation \\(\text{R}\\) that satisfies three properties:

| Property | Mathematically |
|----------|----------------|
Reflexive  | For \\(\forall a \in S\\), \\(a \text{ R } a\\).
Symmetric  | \\(a \text{ R } b \Longleftrightarrow b \text{ R } a\\).
Transitive | \\(a \text{ R } b \text{ and } b \text{ R } c \Longrightarrow a \text{ R } c\\).

## Partition of A Set
A family of sets \\(P\\) is a *partition* of \\(X\\) iff all of the following conditions hold:

| Property | Mathematically |
|----------|----------------|
\\(P\\) does not contain the empty set | \\(\varnothing \not\in P\\)
Union of all sets in \\(P\\) is \\(X\\) | \\(\bigcup _ {A \in P} A = X\\)
All pairs of sets in \\(P\\) are disjoint | \\(\forall A, B \in P, A \neq B \Longrightarrow A \cap B = \varnothing)\\)

* An equivalence relation \\(\sim\\) on a set \\(X\\) partitions \\(X\\).
* Conversely, corresponding to any partition of \\(X\\), there exists an equivalence relation \\(\sim\\) on \\(X\\).

## LeetCode
Disjoint Set is typically used to solve "Connected Components in Undirected Graph" problem. Nodes in connected components naturally form a family of disjoint sets. With Union Find data structure, we can find if two nodes are in the same component or join two components when an edge between them is found in inverse Ackermann function time. 

Connected Component related problems are usually solvable via DFS or BFS, which could be easier to implement when implementation of Disjoint Set is not present. However, Disjoint Set does have an advantage over DFS and BFS in dealing with streaming input, where Disjoint Set can make it possible to save the equivalence relations obtained as the input goes along. 
