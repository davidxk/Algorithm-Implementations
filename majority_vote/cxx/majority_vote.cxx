#include <algorithm>
#include <unordered_map>
#include <vector>

int majority_vote(const std::vector<int>& nums)
{
	int candy, count = 0;
	for(const auto& num: nums)
	{
		if(count == 0)
		{
			candy = num;
			count = 1;
		}
		else if(num == candy)
			count += 1;
		else
			count -= 1;
	}
	if(std::count(nums.begin(), nums.end(), candy) > nums.size() / 2)
		return candy;
	return -1;
}

std::vector<int> majority_vote_general(const std::vector<int>& nums, int k)
{
	if(nums.size() < k)
	{
		std::vector<int> result(nums);
		std::sort(result.begin(), result.end());
		auto it = std::unique(result.begin(), result.end());
		result.resize(std::distance(result.begin(), it));
		return result;
	}
	std::unordered_map<int, int> count;
	for(const auto& num: nums)
	{
		if(count.find(num) != count.end() or count.size() < k - 1)
			count[num]++;
		else
		{
			auto it = count.begin();
			for(; it != count.end(); it++)
				if(it->second == 0)
				{
					count.erase(it);
					count[num] = 1;
					break;
				}
			if(it == count.end())
				for(auto& item: count)
					item.second--;
		}
	}
	std::vector<int> result;
	for(const auto& item: count)
		if(std::count(nums.begin(), nums.end(), item.first) > nums.size() / k)
			result.push_back(item.first);
	return result;
}
