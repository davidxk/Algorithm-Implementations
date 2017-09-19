int partition(int* array, int left, int right);
int r_select(int* array, int left, int right, int rank);
int randomized_select(int* array, const int n, int rank);

int randomized_select(int* array, int n, int rank)
{
	return r_select(array, 0, n - 1, rank);
}

int r_select(int* array, int left, int right, int rank)
{
	if(left == right)
		return array[right];
	int center = partition(array, left, right);
	int pivot_rank = center - left + 1;
	if(rank == pivot_rank)
		return array[center];
	else if(rank < pivot_rank)
		return r_select(array, left, center - 1, rank);
	else
		return r_select(array, center + 1, right, rank - pivot_rank);
}

void swap(int* a, int* b)
{
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

int partition(int* array, int left, int right)
{
	int pivot = array[right];
	int i = left;
	for(int j = left; j < right; j++)
		if(array[j] < pivot)
		{
			swap(&array[i], &array[j]);
			i++;
		}
	swap(&array[i], &array[right]);
	return i;
}
