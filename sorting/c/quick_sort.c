#include "swap.h"

void quick_sort(int* array, const int n);
void q_sort(int* array, int left, int right);
int partition(int* array, int left, int right);
int median3(int *array, int left, int right);
void _insertion_sort(int* array, int left, int right);

void _insertion_sort(int* array, int left, int right)
{
	int i, j, x;
	for(i = left + 1; i < right + 1; i++)
	{
		x = array[i];
		for(j = i - 1; j >= left; j--)
			if(array[j] > x)
				array[j + 1] = array[j];
			else
				break;
		array[j + 1] = x;
	}
}

void quick_sort(int* array, const int n)
{
	q_sort(array, 0, n - 1);
}

void q_sort(int* array, int left, int right)
{
	if(right - left > 10)
	{
		int center = partition(array, left, right);
		q_sort(array, left, center - 1);
		q_sort(array, center + 1, right);
	}
	else
		_insertion_sort(array, left, right);
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
		swap(&array[ i++ ], &array[ j-- ]);
	}
}
