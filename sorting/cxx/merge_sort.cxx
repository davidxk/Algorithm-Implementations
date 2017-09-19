#include <vector>
using namespace std;

void merge_sort(vector<int>& array);
void m_sort(vector<int>& array, int start, int end);
void merge(vector<int>& array, int start, int middle, int end);

void merge_sort(vector<int>& array)
{
	m_sort(array, 0, array.size());
}

void m_sort(vector<int>& array, int start, int end)
{
	if(end - start > 1)
	{
		int middle = (start + end) / 2;
		m_sort(array, start, middle);
		m_sort(array, middle, end);
		merge(array, start, middle, end);
	}
}

void merge(vector<int>& array, int start, int middle, int end)
{
	static vector<int> tmp(array.size());
	int i = start, j = middle, k = 0;
	while(i < middle && j < end)
	{
		if(array[i] < array[j])
			tmp[ k++ ] = array[ i++ ];
		else
			tmp[ k++ ] = array[ j++ ];
	}

	while(i < middle)
		tmp[ k++ ] = array[ i++ ];

	while(j < end)
		tmp[ k++ ] = array[ j++ ];

	for(int i = 0; i < k; i++)
		array[start + i] = tmp[i];
}
