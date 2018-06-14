#include <algorithm>
#include <cstdlib>
#include <vector>

void insertion_sort(std::vector<int>& array, int left, int right);
int median3(std::vector<int>& array, int left, int right);
int partition(std::vector<int>& array, int left, int right);
void q_select(std::vector<int>& array, int left, int right, int rank);
int quick_select(std::vector<int>& array, int rank);

int quick_select(std::vector<int>& array, int rank)
{
	q_select(array, 0, array.size() - 1, rank - 1);
	return array[rank - 1];
}

void q_select(std::vector<int>& array, int left, int right, int rank)
{
	if(right - left < 10)
	{
		insertion_sort(array, left, right);
		return;
	}
	int center = partition(array, left, right);
	if(rank < center)
		return q_select(array, left, center - 1, rank);
	else if(rank > center)
		return q_select(array, center + 1, right, rank);
}

void insertion_sort(std::vector<int>& array, int left, int right)
{
	int j, x;
	for(int i = left + 1; i < right + 1; i++)
	{
		x = array[i];
		for(j = i - 1; j >= left and x < array[j]; j--)
			array[j + 1] = array[j];
		array[j + 1] = x;
	}
}

int median3(std::vector<int>& array, int left, int right)
{
	int center = (left + right) / 2;
	std::vector<int> tmp = { array[left], array[center], array[right] }; 
	insertion_sort(tmp, 0, 2);
	array[left] = tmp[0];
	array[right] = tmp[2];
	array[center] = tmp[1];
	return array[right];
}

int partition(std::vector<int>& array, int left, int right)
{
	int pivot = median3(array, left, right);
	int i = left + 1, j = right - 1;
	while(true)
	{
		while(array[i] < pivot) i++;
		while(pivot < array[j]) j--;
		if(i >= j)
		{
			std::swap(array[i], array[right]);
			return i;
		}
		std::swap(array[i++], array[j--]);
	}
}
