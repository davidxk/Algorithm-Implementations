#include "swap.h"

void heap_sort(int* array, const int n);
void perc_down(int* array, int i, int size);

void perc_down(int* array, int i, int size)
{
	int x, child;
	for(x = array[i]; 2*i+1 < size; i = child)
	{
		child = 2*i+1;
		if(child + 1 < size && array[child + 1] > array[child])
			child++;
		if(array[child] > x)
			array[i] = array[child];
		else
			break;
	}
	array[i] = x;
}

void heap_sort(int* array, const int n)
{
	int i;
	for(i = n/2; i >= 0; i--)
		perc_down(array, i, n);

	for(i = n - 1; i > 0; i--)
	{
		swap(&array[0], &array[i]);
		perc_down(array, 0, i);
	}
}
