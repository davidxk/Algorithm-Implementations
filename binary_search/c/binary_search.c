int binary_search(int* array, int n, int target)
{
	int left = 0, right = n - 1, center;
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

int lower(int* array, int n, int target)
{
	int left = 0, right = n - 1, center;
	while(left <= right)
	{
		center = left + (right - left) / 2;
		if(array[center] == target)
			right = center - 1;
		else if(array[center] < target)
			left = center + 1;
		else
			right = center - 1;
	}
	return left - 1;
}

int higher(int* array, int n, int target)
{
	int left = 0, right = n - 1, center;
	while(left <= right)
	{
		center = left + (right - left) / 2;
		if(array[center] == target)
			left = center + 1;
		else if(array[center] < target)
			left = center + 1;
		else
			right = center - 1;
	}
	return left;
}
