#include "three_way_partition.h"

#include <algorithm>
#include <vector>

bool default_is_head(int elem)
{
	return elem == 0;
}

bool default_is_tail(int elem)
{
	return elem == 2;
}

void three_way_partition(std::vector<int>& array, bool (*is_head)(int),
		bool (*is_tail)(int))
{
	int head = 0, tail = array.size() - 1;
	int i = 0;
	while(i <= tail)
	{
		if(is_head(array[i]))
			std::swap(array[i++], array[head++]);
		else if(is_tail(array[i]))
			std::swap(array[i], array[tail--]);
		else
			i++;
	}
}
