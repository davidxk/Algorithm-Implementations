#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "insertion_sort.c"
#include "selection_sort.c"
#include "bubble_sort.c"
#include "merge_sort.c"
#include "quick_sort.c"
#include "heap_sort.c"

int compare(const void * a, const void * b) { return (*(int*)a - *(int*)b); } 

int check_sort_impl(void (*func)(int*, const int))
{
	const int times = 100;
	int array[2000], original[2000];
	for(int j = 0; j < times; j++)
	{
		int size = rand() % 1000 + 1000;
		for(int i = 0; i < size; i++)
			array[i] = rand() % size;
		memcpy(original, array, sizeof(int) * size);
		func(array, size);
		qsort(original, size, sizeof(int), compare);
		for(int i = 0; i < size; i++)
			if(array[i] != original[i])
				return 0;
	}
	return 1;
}

int main()
{
	const int NFUNC = 6;
	typedef void (*sort_func)(int*, const int);
	sort_func funcs[] = { insertion_sort, selection_sort, bubble_sort, 
		merge_sort, quick_sort, heap_sort
	};
	int i;
	for(i = 0; i < NFUNC; i++)
		if( !check_sort_impl(funcs[i]) )
			printf("Error at funcs[%d]", i);
	return 0;
}
