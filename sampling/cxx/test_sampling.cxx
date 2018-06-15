#include "simple_random_sample.cxx"
#include <cassert>
#include <cstdlib>
#include <vector>

typedef std::vector<int> (*SamplingFunc)(const std::vector<int>&, int);

void test_srs(SamplingFunc func)
{
	const int SIZE = 10;
	std::vector<int> array(SIZE, 0);
	for(int i = 0; i < array.size(); i++)
		array[i] = i;
	std::vector<int> count(SIZE, 0);
	const int TIMES = 1000;
	for(int i = 0; i < TIMES; i++)
	{
		std::vector<int> sample = func(array, SIZE / 2);
		for(const auto& num: sample)
			count[num] += 1;
	}
	for(int i = 0; i < SIZE; i++)
	{
		assert(0.4 * TIMES < count[i]);
		assert(count[i] < 0.6 * TIMES);
	}
}

int main()
{
	test_srs(selection_rejection);
	test_srs(reservoir_sampling);
	return 0 ;
}
