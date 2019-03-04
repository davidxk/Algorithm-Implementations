#include <algorithm>
#include <vector>

void perm_helper(std::vector<int>& nums, int start, std::vector<std::vector<int> >& result)
{
	if(start == nums.size())
	{
		result.push_back(nums);
		return;
	}
	for(int i = start; i < nums.size(); i++)
	{
		std::swap(nums[start], nums[i]);
		perm_helper(nums, start + 1, result);
		std::swap(nums[start], nums[i]);
	}
}

std::vector<std::vector<int> > permutations(std::vector<int> nums)
{
	std::vector<std::vector<int> > result;
	perm_helper(nums, 0, result);
	return result;
}

void perm_with_dup_helper(std::vector<int> nums, int start, std::vector<std::vector<int> >& result)
{
	if(start == nums.size())
	{
		result.push_back(nums);
		return;
	}
	for(int i = start; i < nums.size(); i++)
	{
		std::swap(nums[start], nums[i]);
		perm_with_dup_helper(nums, start + 1, result);
	}
}

std::vector<std::vector<int> > permutations_with_dup(std::vector<int> nums)
{
	std::vector<std::vector<int> > result;
	perm_with_dup_helper(nums, 0, result);
	return result;
}
