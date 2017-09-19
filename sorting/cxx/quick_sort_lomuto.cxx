#include <algorithm>
#include <vector>
using namespace std;

void quick_sort_lomuto(vector<int>& array);

# define LUMOTO_BEGIN namespace lomuto{
# define LUMOTO_END };

LUMOTO_BEGIN

void q_sort(vector<int>& array, int left, int right);
int partition(vector<int>& array, int left, int right);
int median3(vector<int>& array, int left, int right);
void insertion_sort(vector<int>& array, int left, int right);


void insertion_sort(vector<int>& array, int left, int right)
{
	for(int i = left + 1; i < right + 1; i++)
	{
		int x = array[i];
		int j = i - 1;
		while(j >= left && array[j] > x)
		{
			array[j + 1] = array[j];
			j--;
		}
		array[j + 1] = x;
	}
}

void q_sort(vector<int>& array, int left, int right)
{
	if(right - left > 10)
	{
		int center = partition(array, left, right);
		q_sort(array, left, center - 1);
		q_sort(array, center + 1, right);
	}
	else
		insertion_sort(array, left, right);
}

int median3(vector<int>& array, int left, int right)
{
	int center = (left + right) / 2;
	const int three[] = { array[left], array[center], array[right] };
	vector<int> tmp(three, three + 3);
	insertion_sort(tmp, 0, 2);
	array[left] = tmp[0];
	array[center] = tmp[2];
	array[right] = tmp[1];
	return array[right];
}

int partition(vector<int>& array, int left, int right)
{
	int pivot = median3(array, left, right);
	int i = left;
	for(int j = left; j < right; j++)
		if(array[j] < pivot)
		{
			swap(array[i], array[j]);
			i++;
		}

	swap(array[i], array[right]);
	return i;
}

LUMOTO_END

void quick_sort_lomuto(vector<int>& array)
{
	lomuto::q_sort(array, 0, array.size() - 1);
}
