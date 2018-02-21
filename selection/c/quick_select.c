// Rank == count( * <= the element ) in sorted array

#include <stdlib.h>

void swap(int *a, int *b)
{
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

int random_pivot(int* array, int n, int left, int right)
{
	int index = rand() % (right - left + 1) + left;
	swap(&array[index], &array[right]);
	return array[right];
}

int partition(int* array, int n, int left, int right)
{
	int pivot = random_pivot(array, n, left, right);
	int i = left, j = right - 1;
	while(1)
	{
		while(array[i] < pivot) i++;
		while(pivot < array[j]) j--;
		if(i >= j)
		{
			swap(&array[i], &array[right]);
			return i;
		}
		swap(&array[i], &array[j]);
		i++, j--;
	}
}

int q_select(int* array, int n, int left, int right, int rank)
{
	if(left == right)
		return array[left];
	int center = partition(array, n, left, right);
	int pivot_rank = center - left + 1;
	if(rank == pivot_rank)
		return array[center];
	else if(rank < pivot_rank)
		return q_select(array, n, left, center - 1, rank);
	else
		return q_select(array, n, center + 1, right, rank - pivot_rank);
}

int quick_select(int* array, const int n, int rank)
{
	return q_select(array, n, 0, n - 1, rank);
}
