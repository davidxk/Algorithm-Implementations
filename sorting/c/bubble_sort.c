#include <stdio.h>
#include <stdlib.h>

void bubble_sort(int* array, const int n)
{
	int i, swapped;
	do
	{
		swapped = 0;
		for(i = 0; i < n - 1; i++)
			if(array[i] > array[i + 1])
			{
				int tmp = array[i];
				array[i] = array[i + 1];
				array[i + 1] = tmp;

				swapped = 1;
			}
	} while( swapped );
}
