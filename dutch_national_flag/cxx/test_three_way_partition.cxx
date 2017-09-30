#include "three_way_partition.h"

#include <cassert>
#include <cstdlib>
#include <ctime>
#include <vector>

void test_three_way_partition()
{
	const int size = 1000;
	std::vector<int> array(size);
	int cnt[3] = { 0, 0, 0 };
	int num = 0;
	for(int i = 0; i < size; i++)
	{
		num = rand() % 3;
		array[i] = num;
		cnt[num] += 1;
	}
	three_way_partition(array);
	for(int i = 0; i < size; i++)
	{
		assert(i == 0 or array[i - 1] <= array[i]);
		cnt[array[i]]--;
	}
	assert(array[0] == array[1] and array[1] == array[2] and array[2] == 0);
}

int main()
{
	srand(time(NULL));
	test_three_way_partition();
	return 0;
}
