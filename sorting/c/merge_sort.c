#include <stdlib.h>

void merge_sort(int* array, const int n);
void m_sort(int* array, int* temp, int start, int stop);
void merge(int* array, int* temp, int start, int middle, int stop);

void merge_sort(int* array, const int n)
{
	int* temp = malloc(sizeof(int) * n);
	m_sort(array, temp, 0, n);
	free( temp );
}

void m_sort(int* array, int* temp, int start, int stop)
{
	if(stop - start > 1)
	{
		int middle = start + (stop - start) / 2;
		m_sort(array, temp, start, middle);
		m_sort(array, temp, middle, stop);
		merge(array, temp, start, middle, stop);
	}
}

void merge(int* array, int* temp, int start, int middle, int stop)
{
	int i = start, j = middle, k = 0;
	while(i < middle && j < stop)
		if(array[i] < array[j])
			temp[ k++ ] = array[ i++ ];
		else
			temp[ k++ ] = array[ j++ ];

	while(i < middle)
		temp[ k++ ] = array[ i++ ];

	while(j < stop)
		temp[ k++ ] = array[ j++ ];

	for(i = 0; i < k; i++)
		array[start + i] = temp[i];
}
