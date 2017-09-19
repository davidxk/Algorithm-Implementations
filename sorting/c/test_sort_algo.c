#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "insertion_sort.c"
#include "selection_sort.c"
#include "bubble_sort.c"
#include "merge_sort.c"
#include "quick_sort_hoare.c"
#include "heap_sort.c"

const int N = 5000;
int array[N];

int check_monotonic(int* array, const int n)
{
	int i;
	for(i = 0; i < n; i++)
	{
		if(array[i] < 0 || array[i] > N)
			return 0;
		if(i >= 1 && array[i-1] > array[i])
			return 0;
	}
	return 1;
}

int check_consistency(int* original, int* array, int N)
{
	int sum = 0, xor_sum = 0;
	for(int i = 0; i < N; i++)
		sum += original[i], xor_sum ^= original[i];

	for(int i = 0; i < N; i++)
		sum -= array[i], xor_sum ^= array[i];

	return sum == 0 && xor_sum == 0;
}

int check_sort_impl(void (*func)(int*, const int))
{
	for(int i = 0; i < N; i++)
		array[i] = rand() % N;
	int original[N];
	memcpy(original, array, sizeof(int) * N);
	func(array, N);
	return check_monotonic(array, N) && check_consistency(original, array, N);
}


int main()
{
	const int NFUNC = 6;
	typedef void (*sort_func)(int*, const int);
	sort_func funcs[] = { insertion_sort, selection_sort, bubble_sort, 
		merge_sort, quick_sort_hoare, heap_sort
	};
	int i;
	for(i = 0; i < NFUNC; i++)
		if( !check_sort_impl(funcs[i]) )
			printf("Error at funcs[%d]", i);
	return 0;
}

