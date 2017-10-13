typedef struct disjoint_set
{
	int* height;
	int* parent;

	int (*findSet)(struct disjoint_set*, int);
	void (*unionSet)(struct disjoint_set*, int, int);
	void (*destroy)(struct disjoint_set*);
} DisjointSet;

void disjoint_set_init(DisjointSet* ds, int n);
int disjoint_set_find(DisjointSet* ds, int elem);
void disjoint_set_union(DisjointSet* ds, int elem1, int elem2);
void disjoint_set_destroy(DisjointSet* ds);
