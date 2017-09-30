#include "binary_search.h"

#include <iostream>
#include <cassert>

void test_binary_search()
{
	const int SIZE = 1000;
	std::vector<int> array(SIZE);
	int i, target;
	for(i = 0; i < SIZE; i++)
		array[i] = i;
	for(i = 0; i < 100; i++)
	{
		target = rand() % (SIZE * 2);
		if(target >= SIZE)
			assert(binary_search(array, target) == -1);
		else
			assert(binary_search(array, target) == target);
	}
}

void test_upper_bound()
{
	const int SIZE = 1000;
	std::vector<int> array(SIZE);
	int target, lower;
	for(int i = 0; i < SIZE; i++)
		array[i] = rand();
	sort(array.begin(), array.end());
	for(int i = 0; i < 100; i++)
	{
		target = rand();
		for(int j = 0; j < SIZE; j++)
			if(array[j] >= target)
			{
				lower = j - 1;
				break;
			}
		assert(lower_bound(array, target) == lower);
	}
}

void test_lower_bound()
{
	const int SIZE = 1000;
	std::vector<int> array(SIZE);
	int target, upper;
	for(int i = 0; i < SIZE; i++)
		array[i] = rand();
	sort(array.begin(), array.end());
	for(int i = 0; i < 100; i++)
	{
		target = rand();
		for(int j = SIZE - 1; j >= 0; j--)
			if(array[j] <= target)
			{
				upper = j + 1;
				break;
			}
		assert(upper_bound(array, target) == upper);
	}
}

int main()
{
	test_binary_search();
	test_upper_bound();
	test_lower_bound();
	return 0;
}
