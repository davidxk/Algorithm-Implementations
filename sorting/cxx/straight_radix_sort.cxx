#include <algorithm>
#include <climits>
#include <vector>

void straight_radix_sort(std::vector<int>& array);
void counting_sort(std::vector<int>& array, int mask);

void straight_radix_sort(std::vector<int>& array)
{
	int signMask = 1 << (sizeof(int) * CHAR_BIT  - 1);
	for(int& num: array)
		num ^= signMask;

	for(int i = 0; i < sizeof(int) * CHAR_BIT; i++)
		counting_sort(array, i);

	for(int& num: array)
		num ^= signMask;
}

void counting_sort(std::vector<int>& array, int bitNo)
{
	const int bits = 2;
	std::vector<int> count(2, 0);
	for(const int& num: array)
		count[num >> bitNo & 1]++;
	for(int i = 1; i < bits; i++)
		count[i] += count[i - 1];

	std::vector<int> temp(array.size());
	for(int i = array.size() - 1; i >= 0; i--)
	{
		temp[count[array[i] >> bitNo & 1] - 1] = array[i];
		count[array[i] >> bitNo & 1] -= 1;
	}
	std::copy(temp.begin(), temp.end(), array.begin());
}
