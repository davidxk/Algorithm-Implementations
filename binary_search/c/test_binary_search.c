#include "binary_search.h"

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void sort(int* array, int n);
void m_sort(int* array, int n, int start, int end, int* tmp);
void merge(int* array, int n, int start, int middle, int end, int* tmp);

void sort(int* array, int n)
{
	int* tmp = (int*) malloc(sizeof(int) * n);
	m_sort(array, n, 0, n, tmp);
	free(tmp);
}

void m_sort(int* array, int n, int start, int end, int* tmp)
{
	if(end - start > 1)
	{
		int middle = start + (end - start) / 2;
		m_sort(array, n, start, middle, tmp);
		m_sort(array, n, middle, end, tmp);
		merge(array, n, start, middle, end, tmp);
	}
}

void merge(int* array, int n, int start, int middle, int end, int* tmp)
{
	int i = start, j = middle, k = 0;
	while(i < middle && j < end)
		if(array[i] < array[j])
			tmp[k++] = array[i++];
		else
			tmp[k++] = array[j++];
	while(i < middle)
		tmp[k++] = array[i++];
	while(j < end)
		tmp[k++] = array[j++];
	for(i = 0; i < k; i++)
		array[start + i] = tmp[i];
}

void assertEqual(int result, int expect)
{
	if(result != expect)
		printf("Expecting %d, got %d\n", expect, result);
	assert(result == expect);
}

void test_binary_search()
{
	const int SIZE = 1000;
	int array[SIZE];
	int i, target;
	for(i = 0; i < SIZE; i++)
		array[i] = i;
	for(i = 0; i < 100; i++)
	{
		target = rand() % (SIZE * 2);
		if(target >= SIZE)
			assert(binary_search(array, SIZE, target) == -1);
		else
			assert(binary_search(array, SIZE, target) == target);
	}
}

void test_lower_bound()
{
	const int SIZE = 1000;
	int array[SIZE];
	int i, target, j, lower;
	for(i = 0; i < SIZE; i++)
		array[i] = rand();
	sort(array, SIZE);
	for(i = 0; i < 100; i++)
	{
		target = rand();
		for(j = 0; j < SIZE; j++)
			if(array[j] >= target)
			{
				lower = j - 1;
				break;
			}
		assertEqual(lower_bound(array, SIZE, target), lower);
	}
}

void test_upper_bound()
{
	const int SIZE = 1000;
	int array[SIZE];
	int i, target, j, upper;
	for(i = 0; i < SIZE; i++)
		array[i] = rand();
	sort(array, SIZE);
	for(i = 0; i < 100; i++)
	{
		target = rand();
		for(j = SIZE - 1; j >= 0; j--)
			if(array[j] <= target)
			{
				upper = j + 1;
				break;
			}
		assertEqual(upper_bound(array, SIZE, target), upper);
	}
}

int main()
{
	srand(time(0));
	test_binary_search();
	test_upper_bound();
	test_lower_bound();
	return 0;
}
