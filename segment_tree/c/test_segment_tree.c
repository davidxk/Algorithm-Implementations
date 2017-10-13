#include <assert.h>
#include <stdlib.h>
#include <time.h>

#include "sum_segment_tree.h"

void test_query()
{
	const int size = 100;
	int array[size];
	int i, j, left, right;
	int sum;
	for(i = 0; i < size; i++)
		array[i] = rand() % size;
	SumSegmentTree* st = sum_segment_tree_init(array, size);
	for(i = 0; i < size; i++)
	{
		left = rand() % (size / 2);
		right = rand() % size;
		sum = 0;
		for(j = left; j <= right; j++)
			sum += array[j];
		assert(st->query(st, left, right) == sum);
	}
	st->destroy(st);
}

void test_update()
{
	const int size = 100;
	int array[size];
	int i, j, left, right;
	int sum;
	for(i = 0; i < size; i++)
		array[i] = rand() % size;
	SumSegmentTree* st = sum_segment_tree_init(array, size);

	int index = rand() % size, delta = -rand() % 50;
	array[index] += delta;
	st->update(st, index, delta);
	for(i = 0; i < size; i++)
	{
		left = rand() % (size / 2);
		right = rand() % size;
		sum = 0;
		for(j = left; j <= right; j++)
			sum += array[j];
		assert(st->query(st, left, right) == sum);
	}
	st->destroy(st);
}

int main()
{
	test_query();
	test_update();
	return 0;
}
