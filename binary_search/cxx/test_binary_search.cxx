#include "binary_search.cxx"

#include <algorithm>
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

void test_lower_bound()
{
	const int SIZE = 1000;
	std::vector<int> array(SIZE);
	int target, index;
	for(int i = 0; i < SIZE; i++)
		array[i] = rand();
	std::sort(array.begin(), array.end());
	for(int i = 0; i < 100; i++)
	{
		target = rand();
		index = lower_bound(array, target);
		assert(array[index] == 
				*std::lower_bound(array.begin(), array.end(), target));
	}
	for(int i = 0; i < 100; i++)
	{
		target = array[rand() % SIZE];
		index = lower_bound(array, target);
		assert(array[index] == 
				*std::lower_bound(array.begin(), array.end(), target));
	}
}

void test_upper_bound()
{
	const int SIZE = 1000;
	std::vector<int> array(SIZE);
	int target, index;
	for(int i = 0; i < SIZE; i++)
		array[i] = rand();
	std::sort(array.begin(), array.end());
	for(int i = 0; i < 100; i++)
	{
		target = rand();
		index = upper_bound(array, target);
		assert(array[index] == 
				*std::upper_bound(array.begin(), array.end(), target));
	}
	for(int i = 0; i < 100; i++)
	{
		target = array[rand() % SIZE];
		index = upper_bound(array, target);
		assert(array[index] == 
				*std::upper_bound(array.begin(), array.end(), target));
	}
}

int main()
{
	test_binary_search();
	test_lower_bound();
	test_upper_bound();
	return 0;
}
