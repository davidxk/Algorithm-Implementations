#include <vector>

void merge_sort(std::vector<int>& array);
void m_sort(std::vector<int>& array, std::vector<int>& temp, int start, int stop);
void merge(std::vector<int>& array, std::vector<int>& temp, int start, int middle, int stop);

void merge_sort(std::vector<int>& array)
{
	std::vector<int> temp(array.size());
	m_sort(array, temp, 0, array.size());
}

void m_sort(std::vector<int>& array, std::vector<int>& temp, int start, int stop)
{
	if(stop - start > 1)
	{
		int middle = start + (stop - start) / 2;
		m_sort(array, temp, start, middle);
		m_sort(array, temp, middle, stop);
		merge(array, temp, start, middle, stop);
	}
}

void merge(std::vector<int>& array, std::vector<int>& temp, int start, int middle, int stop)
{
	int i = start, j = middle, k = 0;
	while(i < middle && j < stop)
	{
		if(array[i] < array[j])
			temp[ k++ ] = array[ i++ ];
		else
			temp[ k++ ] = array[ j++ ];
	}

	while(i < middle)
		temp[ k++ ] = array[ i++ ];

	while(j < stop)
		temp[ k++ ] = array[ j++ ];

	for(int k = 0; k < stop - start; k++)
		array[start + k] = temp[k];
}
