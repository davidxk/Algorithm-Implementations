#include <deque>
#include <vector>
#include <unordered_map>

// TESTED on LeetCode

// permutations([1 2 3 4]): four possibilities
// [1 (***)]
// [2 (***)]
// [3 (***)]
// [4 (***)]
//
// Permutations
std::vector<std::vector<int> > permutations(std::vector<int>&);

// Permutations recursion helper function
void permsHelper(int start, std::vector<int>&, std::vector<std::vector<int> >&);

std::vector<std::vector<int> > permutations(std::vector<int>& nums)
{
	std::vector<std::vector<int> > result;
	permsHelper(0, nums, result);
	return result;
}

void permsHelper(int start, std::vector<int>& nums, std::vector<std::vector<int> >& result)
{
	if(start == nums.size())
		result.emplace_back(nums);
	for(int i = start; i < nums.size(); i++)
	{
		std::swap(nums[i], nums[start]);
		permsHelper(start + 1, nums, result);
		std::swap(nums[i], nums[start]);
	}
}

// permsWithDup([1 1 2 3]):
// [1 | 1 2 3]
// 	 [1 1 | 2 3]
// 	   [1 1 2 | 3]
// 	     [1 1 2 3]
// [2 | 1 1 3]
// [3 | 1 1 2]
//
// Permutations with duplicates
std::vector<std::vector<int> > permsWithDup(std::vector<int>&);

// Permutations with duplicates recursion helper function
void permsDupHelper(int, std::vector<int>, std::vector<std::vector<int> >&);

std::vector<std::vector<int> > permsWithDup(std::vector<int>& nums)
{
	std::vector<std::vector<int> > result;
	std::sort(nums.begin(), nums.end());
	permsDupHelper(0, nums, result);
	return result;
}

void permsDupHelper(int start, std::vector<int> nums, std::vector<std::vector<int> >& result)
{
	if(start == nums.size())
		result.emplace_back(nums);
	for(int i = start; i < nums.size(); i++)
		if(i == start || nums[i] != nums[start])
		{
			std::swap(nums[i], nums[start]);
			permsDupHelper(start + 1, nums, result);
		}
}

// permsWithDupHashmap([1 1 2 3]):
// 1 -> 1 2 3
// 2 -> 1 1 3
// 3 -> 1 1 2
//
// Permutations with duplicates using hash map
std::vector<std::vector<int> > permsWithDupHashmap(std::vector<int>&);

// Permutations with duplicates using hash map recursion helper function
void permsWithDupHashmapHelper(std::vector<int>&, std::deque<int>& buf, std::unordered_map<int, int>&, std::vector<std::vector<int> >&);

std::vector<std::vector<int> > permsWithDupHashmap(std::vector<int>& nums)
{
	std::vector<std::vector<int> > result;
	std::unordered_map<int, int> count;
	for(const int& num: nums)
		count[num]++;
	std::deque<int> buf;
	permsWithDupHashmapHelper(nums, buf, count, result);
	return result;
}

void permsWithDupHashmapHelper(std::vector<int>& nums, std::deque<int>& buf, std::unordered_map<int, int>& count, std::vector<std::vector<int> >& result)
{
	if(buf.size() == nums.size())
		result.emplace_back(buf.begin(), buf.end());
	for(const std::pair<int, int>& it: count)
		if(it.second > 0)
		{
			int num = it.first;
			buf.push_back(num);
			count[num]--;
			permsWithDupHashmapHelper(nums, buf, count, result);
			count[num]++;
			buf.pop_back();
		}
}
