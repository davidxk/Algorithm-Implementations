#include <stdlib.h>

void merge_sort(int* array, const int n);
void m_sort(int* array, int* tmp, int start, int end);
void merge(int* array, int* tmp, int start, int middle, int end);

void merge_sort(int* array, const int n)
{
	int* tmp = malloc(sizeof(int) * n);
	m_sort(array, tmp, 0, n);
	free( tmp );
}

void m_sort(int* array, int* tmp, int start, int end)
{
	if(end - start > 1)
	{
		int middle = (start + end) / 2;
		m_sort(array, tmp, start, middle);
		m_sort(array, tmp, middle, end);
		merge(array, tmp, start, middle, end);
	}
}

void merge(int* array, int* tmp, int start, int middle, int end)
{
	int i = start, j = middle, k = 0;
	while(i < middle && j < end)
		if(array[i] < array[j])
			tmp[ k++ ] = array[ i++ ];
		else
			tmp[ k++ ] = array[ j++ ];

	while(i < middle)
		tmp[ k++ ] = array[ i++ ];

	while(j < end)
		tmp[ k++ ] = array[ j++ ];

	for(i = 0; i < k; i++)
		array[start + i] = tmp[i];
}
