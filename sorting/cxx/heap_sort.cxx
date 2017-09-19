#include <algorithm>
#include <vector>
using namespace std;

void perc_down(vector<int>& array, int i, int size)
{
	int child, x;
	for(x = array[i]; 2*i+1 < array.size(); i = child)
	{
		child = 2 * i + 1;
		if(child + 1 < array.size() and array[child + 1] > array[child])
			child++;
		if(array[child] > x)
			array[i] = array[child];
		else
			break;
	}
}

void heap_sort(vector<int>& array)
{
	for(int i = array.size()/2; i >=0; i--)
		perc_down(array, i, array.size());
	for(int i = array.size() - 1; i > 0; i--)
	{
		swap(array[0], array[i]);
		perc_down(array, 0, i);
	}
}
