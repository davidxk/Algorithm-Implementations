#include <algorithm>
#include <vector>

#define BFPRT_START namespace bfprt{
#define BFPRT_END }

BFPRT_START
void insertion_sort(std::vector<int>& array, int left, int right)
{
	int x, j;
	for(int i = left + 1; i < right + 1; i++)
	{
		x = array[i];
		j = i - 1;
		while(j >= left and array[j] > x)
		{
			array[j] = array[j + 1];
			j--;
		}
		array[j + 1] = x;
	}
}

int median5(std::vector<int>& array, int left, int right)
{
	insertion_sort(array, left, right);
	return (right + left) / 2;
}

int m_select(std::vector<int>& array, int left, int right, int rank);

int median_of_medians(std::vector<int>& array, int left, int right)
{
	if(right - left < 5)
		return median5(array, left, right);
	int subright, index, gid;
	for(int i = left; i <= right; i += 5)
	{
		subright = i + 4;
		if(subright > right)
			subright = right;
		index = median5(array, i, subright);
		gid = left + (i - left) / 5;
		std::swap(array[gid], array[index]);
	}
	return m_select(array, left, left + (right - left + 1) / 5,
			(right - left) / 10 + 1);
}

int partition(std::vector<int>& array, int left, int right)
{
	int index = median_of_medians(array, left, right);
	int pivot = array[index];
	std::swap(array[index], array[right]);
	int i = left, j = right - 1;
	while(true)
	{
		while(array[i] < pivot) i++;
		while(left <= j and pivot < array[j]) j--;
		if(i >= j)
		{
			std::swap(array[i], array[right]);
			return i;
		}
		std::swap(array[i++], array[j--]);
	}
}

int m_select(std::vector<int>& array, int left, int right, int rank)
{
	if(left == right)
		return left;
	int center = partition(array, left, right);
	int pivot_rank = center - left + 1;
	if(rank == pivot_rank)
		return center;
	else if(rank < pivot_rank)
		return m_select(array, left, center - 1, rank);
	else
		return m_select(array, center + 1, right, rank - pivot_rank);
}
BFPRT_END

int bfprt_select(std::vector<int>& array, int rank)
{
	int index = bfprt::m_select(array, 0, array.size() - 1, rank);
	return array[index];
}
