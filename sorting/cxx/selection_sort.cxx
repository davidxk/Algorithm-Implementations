#include <algorithm>
#include <vector>

void selection_sort(std::vector<int>& array)
{
	int minIdx;
	for(int i = 0; i < array.size(); i++)
	{
		minIdx = i;
		for(int j = i + 1; j < array.size(); j++)
			if(array[j] < array[minIdx])
				minIdx = j;
		std::swap(array[i], array[minIdx]);
	}
}
