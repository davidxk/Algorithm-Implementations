#include <algorithm>
#include <cstdlib>
#include <vector>

std::vector<int> draw_by_draw(std::vector<int>& array, int k)
{
	int index;
	for(int i = 0; i < k; i++)
	{
		index = rand() % (array.size() - i);
		std::swap(array[index], array[array.size() - 1 - i]);
	}
	return std::vector<int>(array.begin() + array.size() - k, array.end());
}

std::vector<int> selection_rejection(const std::vector<int>& array, int k)
{
	std::vector<int> sample(k, 0);
	int cnt = 0, n = array.size();
	for(const auto& elem: array)
	{
		if((float)rand() / RAND_MAX < (float)k / n)
		{
			sample[cnt++] = elem;
			k--;
		}
		n--;
	}
	return sample;
}

std::vector<int> reservoir_sampling(const std::vector<int>& array, int k)
{
	std::vector<int> sample(k, 0);
	auto it = array.begin();
	for(int i = 0; i < k; i++)
	{
		sample[i] = *it++;
		if(it == array.end())
			return sample;
	}
	int n = k;
	int idx;
	while(it != array.end())
	{
		n += 1;
		if((float)rand() / RAND_MAX < (float)k / n)
		{
			idx = rand() % k;
			sample[idx] = *it;
		}
		it++;
	}
	return sample;
}
