#include <algorithm>
#include <vector>
using namespace std;

void bubble_sort(vector<int>& array)
{
	bool swapped = false;
	do
	{
		swapped = false;
		for(int i = 1; i < array.size(); i++)
			if(array[i - 1] > array[i])
			{
				swap(array[i - 1], array[i]);
				swapped = true;
			}
	} while(swapped);
}
