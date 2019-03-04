#include "DisjointSet.h"

DisjointSet::DisjointSet(int nElems)
{
	height.resize(nElems, 1);
	parent.resize(nElems);
	for(int node = 0; node < parent.size(); node++)
		parent[node] = node;
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
		height[root2] = 0;
		parent[root2] = root1;
	}
	else
	{
		if(height[root1] == height[root2])
			height[root2]++;
		height[root1] = 0;
		parent[root1] = root2;
	}
}
