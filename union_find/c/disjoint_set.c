#include "disjoint_set.h"
#include <stdlib.h>

void disjoint_set_init(DisjointSet* ds, int n)
{
	ds->height = (int*) malloc(sizeof(int) * n);
	ds->parent = (int*) malloc(sizeof(int) * n);
	int i;
	for(i = 0; i < n; i++)
	{
		ds->height[i] = 0;
		ds->parent[i] = i;
	}

	ds->findSet = disjoint_set_find;
	ds->unionSet = disjoint_set_union;
	ds->destroy = disjoint_set_destroy;
}

int disjoint_set_find(DisjointSet* ds, int elem)
{
	if(ds->parent[elem] != elem)
		ds->parent[elem] = disjoint_set_find(ds, ds->parent[elem]);
	return ds->parent[elem];
}

void disjoint_set_link(DisjointSet* ds, int root1, int root2)
{
	if(ds->height[root1] > ds->height[root2])
		ds->parent[root2] = root1;
	else
	{
		if(ds->height[root1] == ds->height[root2])
			ds->height[root2]++;
		ds->parent[root1] = root2;
	}
}

void disjoint_set_union(DisjointSet* ds, int elem1, int elem2)
{
	int root1 = disjoint_set_find(ds, elem1);
	int root2 = disjoint_set_find(ds, elem2);
	if(root1 != root2)
		disjoint_set_link(ds, root1, root2);
}

void disjoint_set_destroy(DisjointSet* ds)
{
	free(ds->height);
	free(ds->parent);
}
