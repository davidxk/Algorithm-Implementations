#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

void insertion_sort(vector<int>& array)
{
	for(int i = 1; i < array.size(); i++)
	{
		int x = array[i];
		int j = i - 1;
		while(j >= 0 && array[j] > x)
		{
			array[j + 1] = array[j];
			j--;
		}
		array[j + 1] = x;
	}
}
