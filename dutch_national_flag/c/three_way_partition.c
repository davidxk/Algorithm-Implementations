#include "three_way_partition.h"
#include "swap.h"

int default_is_head(int elem)
{
	return elem == 0;
}

int default_is_tail(int elem)
{
	return elem == 2;
}

void three_way_partition(int* array, int n, int (*is_head)(int), 
		int (*is_tail)(int))
{
	int head = 0, tail = n - 1;
	int i = 0;
	while(i <= tail)
	{
		if(is_head(array[i]))
			swap(&array[i++], &array[head++]);
		else if(is_tail(array[i]))
			swap(&array[i], &array[tail--]);
		else
			i++;
	}
}
