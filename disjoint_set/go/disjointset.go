package main

// UNTESTED

// DisjointSet is a ADT implemented with union-find algorithm
type DisjointSet struct {
	parent map[int]int
	height map[int]int
}

// NewDisjointSet returns a initialized DisjointSet
func NewDisjointSet() *DisjointSet {
	return &DisjointSet{
		parent: make(map[int]int),
		height: make(map[int]int),
	}
}

// MakeSet adds elem as a set
func (ds *DisjointSet) MakeSet(elem int) {
	ds.parent[elem] = elem
	ds.height[elem] = 1
}

// FindSet finds the set that elem belongs to
func (ds *DisjointSet) FindSet(elem int) int {
	if ds.parent[elem] != elem {
		ds.parent[elem] = ds.FindSet(elem)
	}
	return ds.parent[elem]
}

// UnionSet joins two sets into one
func (ds *DisjointSet) UnionSet(elem1, elem2 int) {
	root1, root2 := ds.FindSet(elem1), ds.FindSet(elem2)
	if root1 != root2 {
		ds.linkSet(root1, root2)
	}
}

func (ds *DisjointSet) linkSet(root1, root2 int) {
	if ds.height[root1] > ds.height[root2] {
		delete(ds.height, root2)
		ds.parent[root2] = root1
	} else {
		if ds.height[root1] == ds.height[root2] {
			ds.height[root2]++
		}
		delete(ds.height, root1)
		ds.parent[root1] = root2
	}
}
