#include <vector>

void comb_helper(std::vector<int> nums, int k, int start, std::vector<int>& buf, std::vector<std::vector<int> >& result)
{
	if(buf.size() == k)
	{
		result.push_back(buf);
		return;
	}
	for(int i = start; i < nums.size() - (k - buf.size()) + 1; i++)
	{
		buf.push_back(nums[i]);
		comb_helper(nums, k, i + 1, buf, result);
		buf.pop_back();
	}
}

std::vector<std::vector<int> > combinations(std::vector<int> nums, int k)
{
	std::vector<std::vector<int> > result;
	std::vector<int> buf;
	comb_helper(nums, k, 0, buf, result);
	return result;
}

void comb_with_dup_helper(std::vector<int> nums, int k, int start, std::vector<int>& buf, std::vector<std::vector<int> >& result)
{
	if(buf.size() == k)
	{
		result.push_back(buf);
		return;
	}
	for(int i = start; i < nums.size() - (k - buf.size()) + 1; i++)
		if(i == 0 or nums[i] != nums[i - 1])
		{
			buf.push_back(nums[i]);
			comb_with_dup_helper(nums, k, i + 1, buf, result);
			buf.pop_back();
		}
}

std::vector<std::vector<int> > combinations_with_dup(std::vector<int> nums, int k)
{
	std::vector<std::vector<int> > result;
	std::vector<int> buf;
	comb_with_dup_helper(nums, k, 0, buf, result);
	return result;
}
