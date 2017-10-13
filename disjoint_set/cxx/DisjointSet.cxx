#include "DisjointSet.h"

void DisjointSet::makeSet(int elem)
{
	height.emplace(elem, 0);
	parent.emplace(elem, elem);
}

int DisjointSet::findSet(int elem)
{
	if(parent[elem] != elem)
		parent[elem] = findSet(parent[elem]);
	return parent[elem];
}

void DisjointSet::unionSet(int elem1, int elem2)
{
	int root1 = findSet(elem1), root2 = findSet(elem2);
	if(root1 != root2)
		linkSet(root1, root2);
}

void DisjointSet::linkSet(int root1, int root2)
{
	if(height[root1] > height[root2])
	{
		height.erase(root2);
		parent[root2] = root1;
	}
	else
	{
		if(height[root1] == height[root2])
			height[root2] += 1;
		height.erase(root1);
		parent[root2] = root1;
	}
}
