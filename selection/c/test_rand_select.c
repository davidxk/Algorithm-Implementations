#include <stdio.h>
#include <stdlib.h>
#include "quick_select.c"

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

int check_rand_select(int* array, int n, int rank, int retval)
{
	heap_sort(array, n);
	return array[rank - 1] == retval;
}

int test_rand_select()
{
	const int n = 5000;
	int array[n];
	int i, j, rank, retval;
	for(i = 0; i < 1000; i++)
	{
		for(j = 0; j < n; j++)
			array[j] = rand() % (n * 2);
		rank = rand() % n + 1;
		retval = quick_select(array, n, rank);
		if(!check_rand_select(array, n, rank, retval))
			return 0;
	}
	return 1;
}

int main()
{
	if(!test_rand_select())
		printf("WA: rand_select\n");
}
