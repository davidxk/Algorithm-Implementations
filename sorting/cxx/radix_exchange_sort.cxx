#include <algorithm>
#include <climits>
#include <vector>

void radix_exchange_sort(std::vector<int>& array);

# define RADIX_EXCHANGE_BEGIN namespace radix_exchange {
# define RADIX_EXCHANGE_END };

RADIX_EXCHANGE_BEGIN

void r_sort(std::vector<int>& array, int left, int right, int bitNo);
int partition(std::vector<int>& array, int left, int right, int mask);


void r_sort(std::vector<int>& array, int left, int right, int bitNo)
{
	if(right > left and bitNo >= 0)
	{
		int center = partition(array, left, right, 1 << bitNo);
		r_sort(array, left, center - 1, bitNo - 1);
		r_sort(array, center, right, bitNo - 1);
	}
}

int partition(std::vector<int>& array, int left, int right, int mask)
{
	int i = left, j = right;
	while(true)
	{
		while((array[i] & mask) == 0 && i < j) i++;
		while((array[j] & mask) != 0 && i < j) j--;
		if(i >= j)
		{
			if((array[i] & mask) == 0)
				i++;
			return i;
		}
		std::swap(array[i++], array[j--]);
	}
}

RADIX_EXCHANGE_END

void radix_exchange_sort(std::vector<int>& array)
{
	int signMask = 1 << (sizeof(int) * CHAR_BIT  - 1);
	for(int& num: array)
		num ^= signMask;

	radix_exchange::r_sort(array, 0, array.size() - 1, sizeof(int) * CHAR_BIT - 1);

	for(int& num: array)
		num ^= signMask;
}
