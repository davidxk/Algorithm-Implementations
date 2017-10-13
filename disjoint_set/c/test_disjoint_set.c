#include "disjoint_set.h"

#include <assert.h>

void testDisjointSet()
{
	DisjointSet ds;
	disjoint_set_init(&ds, 100);
	int i;
	for(int i = 0; i < 100; i++)
		ds.unionSet(&ds, i, i % 5);
	for(int i = 0; i < 100; i++)
		for(int j = i; j < 100; j++)
			assert((ds.findSet(&ds, i) == ds.findSet(&ds, j)) == ((i % 5) == (j % 5)));
	ds.destroy(&ds);
}

int main()
{
	testDisjointSet();
	return 0;
}
