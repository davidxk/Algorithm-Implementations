#include <stdio.h>
#include <stdlib.h>

void insertion_sort(int *array, const int n)
{
	int i, j;
	int x;
	for(i = 1; i < n; i++)
	{
		x = array[i];
		for(j = i - 1; j >= 0; j--)
			if(array[j] > x)
				array[j + 1] = array[j];
			else
				break;
		array[j + 1] = x;
	}
}
