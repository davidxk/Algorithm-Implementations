#include <cassert>
#include <climits>
#include <cstdlib>
#include <ctime>

#include "RMQSegmentTree.h"

void testQuery()
{
	const int size = 100;
	std::vector<int> array(size);
	int i, j, left, right;
	int minimum;
	for(i = 0; i < size; i++)
		array[i] = rand() % size;
	RMQSegmentTree rmq(array);
	for(i = 0; i < size; i++)
	{
		left = rand() % (size / 2);
		right = rand() % size;
		minimum = INT_MAX;
		for(j = left; j <= right; j++)
			if(array[j] < minimum)
				minimum = array[j];
		assert(rmq.query(left, right) == minimum);
	}
}

void testUpdate()
{
	const int size = 100;
	std::vector<int> array(size);
	int i, j, left, right;
	int minimum;
	for(i = 0; i < size; i++)
		array[i] = rand() % size;
	RMQSegmentTree rmq(array);

	int index = rand() % size, delta = -rand() % 50;
	array[index] += delta;
	rmq.update(index, delta);
	for(i = 0; i < size; i++)
	{
		left = rand() % (size / 2);
		right = rand() % size;
		minimum = INT_MAX;
		for(j = left; j <= right; j++)
			if(array[j] < minimum)
				minimum = array[j];
		assert(rmq.query(left, right) == minimum);
	}
}

int main()
{
	testQuery();
	testUpdate();
	return 0;
}
