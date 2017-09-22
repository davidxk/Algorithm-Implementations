
typedef struct binary_indexed_tree
{
	int* tree;
	int treesz;
	int (*get_sum)(struct binary_indexed_tree*, int);
	void (*update)(struct binary_indexed_tree*, int, int);
	int (*get_range)(struct binary_indexed_tree*, int, int);
	void (*destroy)(struct binary_indexed_tree*);
} BinaryIndexedTree;

BinaryIndexedTree* bit_init(int* array, int n);
int bit_get_sum(BinaryIndexedTree* bit, int i);
void bit_update(BinaryIndexedTree* bit, int i, int delta);
int bit_get_range(BinaryIndexedTree* bit, int i, int j);
void bit_destroy(BinaryIndexedTree* bit);
