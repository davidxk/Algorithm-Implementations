// Rank == count( _ <= the element ) in sorted array

#include <stdlib.h>

void swap(int *a, int *b)
{
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

void _insertion_sort(int *array, int left, int right)
{
	int i, j, x;
	for(i = left + 1; i < right + 1; i++)
	{
		x = array[i];
		for(j = i - 1; j >= left && x < array[j]; j--)
			array[j + 1] = array[j];
		array[j + 1] = x;
	}
}

int median3(int* array, int left, int right)
{
	int center = (left + right) / 2;
	int tmp[] = { array[left], array[center], array[right] };
	_insertion_sort(tmp, 0, 2);
	array[left] = tmp[0];
	array[center] = tmp[2];
	array[right] = tmp[1];
	return array[right];
}

int partition(int* array, int left, int right)
{
	int pivot = median3(array, left, right);
	int i = left + 1, j = right - 1;
	while(1)
	{
		while(array[i] < pivot) i++;
		while(pivot < array[j]) j--;
		if(i >= j)
		{
			swap(&array[i], &array[right]);
			return i;
		}
		swap(&array[i++], &array[j--]);
	}
}

void q_select(int* array, int left, int right, int rank)
{
	if(right - left < 10)
	{
		_insertion_sort(array, left, right);
		return;
	}
	int center = partition(array, left, right);
	if(rank < center)
		q_select(array, left, center - 1, rank);
	else if(rank > center)
		q_select(array, center + 1, right, rank);
}

int quick_select(int* array, const int n, int rank)
{
	q_select(array, 0, n - 1, rank - 1);
	return array[rank - 1];
}
