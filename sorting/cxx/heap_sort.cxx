#include <algorithm>
#include <vector>

void perc_down(std::vector<int>& array, int i, int size)
{
	int child, x;
	for(x = array[i]; 2*i+1 < size; i = child)
	{
		child = 2 * i + 1;
		if(child + 1 < size and array[child + 1] > array[child])
			child++;
		if(array[child] > x)
			array[i] = array[child];
		else
			break;
	}
	array[i] = x;
}

void heap_sort(std::vector<int>& array)
{
	for(int i = array.size()/2; i >= 0; i--)
		perc_down(array, i, array.size());
	for(int i = array.size() - 1; i > 0; i--)
	{
		std::swap(array[0], array[i]);
		perc_down(array, 0, i);
	}
}
