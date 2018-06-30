#include "rsq_segment_tree.h"

#include <math.h>
#include <stdlib.h>

static void rsq_segment_tree_build(RSQSegmentTree* st, int i, int* array, int left, int right);
static int rsq_segment_tree_query_util(RSQSegmentTree* st, int i, int q_left, int q_right, int left, int right);

RSQSegmentTree* rsq_segment_tree_init(int* array, int n)
{
	RSQSegmentTree* st = (RSQSegmentTree*) malloc(sizeof(RSQSegmentTree));
	st->length = n;

	int x = log2(n) + 1;
	int size = pow(2, x) * 2;
	st->tree = (int*) malloc(sizeof(int) * size);

	st->query = rsq_segment_tree_query;
	st->update = rsq_segment_tree_update;
	st->destroy = rsq_segment_tree_destroy;

	rsq_segment_tree_build(st, 0, array, 0, st->length - 1);
	return st;
}

void rsq_segment_tree_build(RSQSegmentTree* st, int i, int* array, int left, int right)
{
	if(left >= right)
	{
		st->tree[i] = array[left];
		return;
	}
	int center = left + (right - left) / 2;
	rsq_segment_tree_build(st, 2 * i + 1, array, left, center);
	rsq_segment_tree_build(st, 2 * i + 2, array, center + 1, right);
	st->tree[i] = st->tree[i * 2 + 1] + st->tree[i * 2 + 2];
}

int rsq_segment_tree_query(RSQSegmentTree* st, int q_left, int q_right)
{
	return rsq_segment_tree_query_util(st, 0, q_left, q_right, 0, st->length - 1);
}

int rsq_segment_tree_query_util(RSQSegmentTree* st, int i, int q_left, int q_right, int left, int right)
{
	if(q_left <= left && right <= q_right)
		return st->tree[i];

	if(right < q_left || q_right < left)
		return 0;

	int center = left + (right - left) / 2;
	return rsq_segment_tree_query_util(st, 2 * i + 1, q_left, q_right, left, center) + 
		rsq_segment_tree_query_util(st, 2 * i + 2, q_left, q_right, center + 1, right);
}

void rsq_segment_tree_update(RSQSegmentTree* st, int index, int delta)
{
	int left = 0, right = st->length - 1, center;
	int i = 0;
	while(left < right)
	{
		center = left + (right - left) / 2;
		if(index <= center)
		{
			right = center;
			i = 2 * i + 1;
		}
		else
		{
			left = center + 1;
			i = 2 * i + 2;
		}
	}
	st->tree[i] += delta;
	while(i > 0)
	{
		i = (i - 1) / 2;
		st->tree[i] = st->tree[2 * i + 1] + st->tree[2 * i + 2];
	}
}

void rsq_segment_tree_destroy(RSQSegmentTree* st)
{
	free(st->tree);
	free(st);
}
