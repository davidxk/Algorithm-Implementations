#include <stdio.h>
#include <stdlib.h>

void selection_sort(int* a, const int n)
{
	int i, j, minIdx;
	int tmp;
	for(i = 0; i < n; i++)
	{
		minIdx = i;
		for(j = i + 1; j < n; j ++)
			if(a[j] < a[minIdx])
				minIdx = j;

		tmp = a[i];
		a[i] = a[minIdx];
		a[minIdx] = tmp;
	}
}
