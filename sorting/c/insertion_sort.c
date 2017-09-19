#include <stdio.h>
#include <stdlib.h>

void insertion_sort(int *array, const int n)
{
	int i, j;
	for(i = 0; i < n; i++)
	{
		int x = array[i];
		j = i - 1;
		while(j >= 0 && array[j] > x)
		{
			array[j + 1] = array[j];
			j -= 1;
		}
		array[j + 1] = x;
	}
}
