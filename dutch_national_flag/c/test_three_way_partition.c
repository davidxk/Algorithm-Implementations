#include "three_way_partition.h"

#include <assert.h>
#include <stdlib.h>
#include <time.h>

void test_three_way_partition()
{
	const int size = 1000;
	int array[size];
	int cnt[3] = { 0, 0, 0 };
	int num = 0;
	for(int i = 0; i < size; i++)
	{
		num = rand() % 3;
		array[i] = num;
		cnt[num] += 1;
	}
	three_way_partition(array, size, default_is_head, default_is_tail);
	for(int i = 0; i < size; i++)
	{
		assert(i == 0 || array[i - 1] <= array[i]);
		cnt[array[i]]--;
	}
	assert(array[0] == array[1] && array[1] == array[2] && array[2] == 0);
}

int main()
{
	srand(time(0));
	test_three_way_partition();
	return 0;
}
