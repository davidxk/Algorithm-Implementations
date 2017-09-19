#include <stdio.h>
#include <stdlib.h>

void selection_sort(int* a, const int n)
{
	int i, j;
	for(i = 0; i < n; i++)
		for(j = i + 1; j < n; j ++)
			if(a[i] > a[j])
			{
				int tmp = a[i];
				a[i] = a[j];
				a[j] = tmp;
			}
}
