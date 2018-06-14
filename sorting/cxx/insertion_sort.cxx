#include <cstdlib>
#include <iostream>
#include <vector>

void insertion_sort(std::vector<int>& array)
{
	int j;
	for(int i = 0; i < array.size(); i++)
	{
		int x = array[i];
		for(j = i - 1; j >= 0; j--)
			if(array[j] > x)
				array[j + 1] = array[j];
			else
				break;
		array[j + 1] = x;
	}
}
