typedef struct sum_segment_tree
{
	int* tree;
	int length;
	int (*query)(struct sum_segment_tree*, int, int);
	void (*update)(struct sum_segment_tree*, int, int);
	void (*destroy)(struct sum_segment_tree*);
} SumSegmentTree;

SumSegmentTree* sum_segment_tree_init(int* array, int n);
int sum_segment_tree_query(SumSegmentTree* st, int q_left, int q_right);
void sum_segment_tree_update(SumSegmentTree* st, int index, int delta);
void sum_segment_tree_destroy(SumSegmentTree* st);

static void sum_segment_tree_build(SumSegmentTree* st, int i, int* array, int left, int right);
static int sum_segment_tree_query_util(SumSegmentTree* st, int i, int q_left, int q_right, int left, int right);
