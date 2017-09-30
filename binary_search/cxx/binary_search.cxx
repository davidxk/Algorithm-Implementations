#include <vector>

int binary_search(std::vector<int> array, int target)
{
	int left = 0, right = array.size() - 1, center;
	while(left <= right)
	{
		center = left + (right - left) / 2;
		if(array[center] == target)
			return center;
		else if(array[center] < target)
			left = center + 1;
		else
			right = center - 1;
	}
	return -1;
}

int upper_bound(std::vector<int> array, int target)
{
	int left = 0, right = array.size() - 1, center;
	while(left <= right)
	{
		center = left + (right - left) / 2;
		if(array[center] <= target)
			left = center + 1;
		else
			right = center - 1;
	}
	return left;
}

int lower_bound(std::vector<int> array, int target)
{
	int left = 0, right = array.size() - 1, center;
	while(left <= right)
	{
		center = left + (right - left) / 2;
		if(array[center] < target)
			left = center + 1;
		else
			right = center - 1;
	}
	return right;
}
