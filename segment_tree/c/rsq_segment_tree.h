typedef struct rsq_segment_tree
{
	int* tree;
	int length;
	int (*query)(struct rsq_segment_tree*, int, int);
	void (*update)(struct rsq_segment_tree*, int, int);
	void (*destroy)(struct rsq_segment_tree*);
} RSQSegmentTree;

RSQSegmentTree* rsq_segment_tree_init(int* array, int n);
int rsq_segment_tree_query(RSQSegmentTree* st, int q_left, int q_right);
void rsq_segment_tree_update(RSQSegmentTree* st, int index, int delta);
void rsq_segment_tree_destroy(RSQSegmentTree* st);
