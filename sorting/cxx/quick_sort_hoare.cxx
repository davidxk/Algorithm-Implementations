#include <algorithm>
#include <vector>

void quick_sort_hoare(std::vector<int>& array);

# define HOARE_BEGIN namespace hoare {
# define HOARE_END };

HOARE_BEGIN

void q_sort(std::vector<int>& array, int left, int right);
int partition(std::vector<int>& array, int left, int right);
int median3(std::vector<int>& array, int left, int right);
void insertion_sort(std::vector<int>& array, int left, int right);


void insertion_sort(std::vector<int>& array, int left, int right)
{
	int j;
	for(int i = left + 1; i < right + 1; i++)
	{
		int x = array[i];
		for(j = i - 1; j >= left; j--)
			if(array[j] > x)
				array[j + 1] = array[j];
			else
				break;
		array[j + 1] = x;
	}
}

void q_sort(std::vector<int>& array, int left, int right)
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

int median3(std::vector<int>& array, int left, int right)
{
	int center = (left + right) / 2;
	const int three[] = { array[left], array[center], array[right] };
	std::vector<int> tmp(three, three + 3);
	insertion_sort(tmp, 0, 2);
	array[left] = tmp[0];
	array[center] = tmp[2];
	array[right] = tmp[1];
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

HOARE_END


void quick_sort_hoare(std::vector<int>& array)
{
	hoare::q_sort(array, 0, array.size() - 1);
}
