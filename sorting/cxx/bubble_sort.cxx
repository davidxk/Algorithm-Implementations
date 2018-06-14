#include <algorithm>
#include <vector>

void bubble_sort(std::vector<int>& array)
{
	bool swapped = false;
	do
	{
		swapped = false;
		for(int i = 1; i < array.size(); i++)
			if(array[i - 1] > array[i])
			{
				std::swap(array[i - 1], array[i]);
				swapped = true;
			}
	} while(swapped);
}
