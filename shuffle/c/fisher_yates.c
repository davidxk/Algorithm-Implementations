#include <stdlib.h>

void swap(int* left, int* right)
{
	int tmp = *left;
	*left = *right;
	*right = tmp;
}

void fisher_yates(int* array, int n)
{
	int i, j;
	for(i = n - 1; i > 1; i--)
	{
		j = rand() % (i + 1);
		swap(&array[i], &array[j]);
	}
}

void fisher_yates_front(int* array, int n)
{
	int i, j;
	for(i = 0; i < n; i++)
	{
		j = i + rand() % (n - i);
		swap(&array[i], &array[j]);
	}
}
