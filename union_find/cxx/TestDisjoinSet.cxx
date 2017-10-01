#include "DisjointSet.h"

#include <cassert>

void testDisjointSet()
{
	DisjointSet ds;
	for(int i = 0; i < 100; i++)
		ds.makeSet(i);
	for(int i = 0; i < 100; i++)
		ds.unionSet(i, i % 5);
	for(int i = 0; i < 100; i++)
		for(int j = i; j < 100; j++)
			assert((ds.findSet(i) == ds.findSet(j)) == ((i % 5) == (j % 5)));
}

int main()
{
	testDisjointSet();
	return 0;
}
