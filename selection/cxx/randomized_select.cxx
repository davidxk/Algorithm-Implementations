#include <algorithm>
#include <cstdlib>
#include <vector>
using namespace std;

int random_pivot(vector<int>& array, int left, int right);
int partition(vector<int>& array, int left, int right);
int r_select(vector<int>& array, int left, int right, int rank);
int randomized_select(vector<int>& array, int rank);

int randomized_select(vector<int>& array, int rank)
{
	return r_select(array, 0, array.size() - 1, rank);
}

int r_select(vector<int>& array, int left, int right, int rank)
{
	if(left == right)
		return array[left];
	int center = partition(array, left, right);
	int pivot_rank = center - left + 1;
	if(rank == pivot_rank)
		return array[center];
	else if(rank < pivot_rank)
		return r_select(array, left, center - 1, rank);
	else
		return r_select(array, center + 1, right, rank - pivot_rank);
}

int random_pivot(vector<int>& array, int left, int right)
{
	int index = rand() % (right - left + 1) + left;
	swap(array[index], array[right]);
	return array[right];
}

int partition(vector<int>& array, int left, int right)
{
	int pivot = random_pivot(array, left, right);
	int i = left, j = right - 1;
	while(true)
	{
		while(array[i] < pivot) i++;
		while(pivot < array[j]) j--;
		if(i >= j)
		{
			swap(array[i], array[right]);
			return i;
		}
		swap(array[i++], array[j--]);
	}
}
