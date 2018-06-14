#include <algorithm>
#include <cassert>
#include <cstdlib>
#include <vector>
#include "majority_vote.cxx"

void test_majority_vote()
{
	const int SIZE = 500;
	for(int count = 0; count < SIZE; count++)
	{
		std::vector<int> nums(SIZE, 0);
		for(int i = count; i < nums.size(); i++)
			nums[i] = 1 + rand() % 2;
		std::vector<int> uniq(SIZE);
		std::sort(nums.begin(), nums.end());
		auto it = std::unique_copy(nums.begin(), nums.end(), uniq.begin());
		uniq.resize(std::distance(uniq.begin(), it));
		int expect = -1;
		for(const int& num: uniq)
			if(std::count(nums.begin(), nums.end(), num) > nums.size() / 2)
				expect = num;
		std::random_shuffle(nums.begin(), nums.end());
		assert(majority_vote(nums) == expect && "test majority vote");
	}
}

void test_majority_vote_general()
{
	const int SIZE = 500;
	for(int count = 0; count < SIZE; count++)
	{
		std::vector<int> nums(SIZE, 0);
		int k = 2 + rand() % 8;
		int range = 1 + rand() % 10;
		for(int i = count; i < nums.size(); i++)
			nums[i] = rand() % range;
		std::vector<int> uniq(SIZE);
		std::sort(nums.begin(), nums.end());
		auto it = std::unique_copy(nums.begin(), nums.end(), uniq.begin());
		uniq.resize(std::distance(uniq.begin(), it));
		std::vector<int> expect;
		for(const int& num: uniq)
			if(std::count(nums.begin(), nums.end(), num) > nums.size() / k)
				expect.push_back(num);
		std::random_shuffle(nums.begin(), nums.end());
		std::vector<int> result = majority_vote_general(nums, k);
		assert(std::is_permutation(result.begin(), result.end(), 
					expect.begin()) && "test majority of 1/k votes");
	}
}

void test_majority_vote_edge_case()
{
	const int SIZE = 500;
	for(int count = 0; count < SIZE; count++)
	{
		std::vector<int> nums(SIZE, 0);
		int k = 1 + rand() % SIZE;
		int range = 1 + rand() % 10;
		for(int i = count; i < nums.size(); i++)
			nums[i] = rand() % range;
		std::vector<int> uniq(SIZE);
		std::sort(nums.begin(), nums.end());
		auto it = std::unique_copy(nums.begin(), nums.end(), uniq.begin());
		uniq.resize(std::distance(uniq.begin(), it));
		std::vector<int> expect;
		for(const int& num: uniq)
			if(std::count(nums.begin(), nums.end(), num) > nums.size() / k)
				expect.push_back(num);
		std::random_shuffle(nums.begin(), nums.end());
		std::vector<int> result = majority_vote_general(nums, k);
		assert(std::is_permutation(result.begin(), result.end(), 
					expect.begin()) && "test majority of 1/k votes");
	}
}

int main()
{
	test_majority_vote();
	test_majority_vote_general();
	return 0;
}
