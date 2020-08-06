#include <algorithm>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <set>
#include <vector>
#include "BinarySearchTree.h"

class TestableBST: public BinarySearchTree
{
	friend void checkBST(const TestableBST& bst);
};

static void helper(TreeNode* root)
{
	if(root->left)
	{
		assert(root->val > root->left->val);
		helper(root->left);
	}
	if(root->right)
	{
		assert(root->val < root->right->val);
		helper(root->right);
	}
}

void checkBST(const TestableBST& bst)
{
	TreeNode* root = bst.root;
	if(not root) return;
	helper(root);
}

void setUp(int SIZE, int RANGE, TestableBST& bst, std::set<int>& numSet)
{
	int num;
	for(int i = 0; i < SIZE; i++)
	{
		num = rand() % RANGE;
		numSet.insert(num);
		bst.insert(num);
	}
}

void test_insert_find(int SIZE, int RANGE)
{
	TestableBST bst;
	std::set<int> numSet;
	setUp(SIZE, RANGE, bst, numSet);
	checkBST(bst);
	for(int num = 0; num < RANGE; num++)
		assert((numSet.find(num) != numSet.end()) == bst.find(num));
}

void test_erase(int SIZE, int RANGE)
{
	TestableBST bst;
	std::set<int> numSet;
	setUp(SIZE, RANGE, bst, numSet);
	for(const int& num: numSet)
	{
		assert(bst.erase(num));
		assert(not bst.find(num));
		checkBST(bst);
	}
	assert(bst.empty());
}

void test_upper_lower_bound(int SIZE, int RANGE)
{
	TestableBST bst;
	std::set<int> numSet;
	setUp(SIZE, RANGE, bst, numSet);
	for(int num = 0; num < RANGE; num++)
	{
		auto upperIter = numSet.upper_bound(num);
		auto lowerIter = numSet.lower_bound(num);
		if(lowerIter == numSet.end())
			assert(bst.lower_bound(num) == INT_MIN);
		else
			assert(bst.lower_bound(num) == *lowerIter);

		if(upperIter == numSet.end())
			assert(bst.upper_bound(num) == INT_MAX);
		else
			assert(bst.upper_bound(num) == *upperIter);
	}
}

void test_front_back(int SIZE, int RANGE)
{
	TestableBST bst;
	std::set<int> numSet;
	setUp(SIZE, RANGE, bst, numSet);
	assert(bst.front() == *std::min_element(numSet.begin(), numSet.end()));
	assert(bst.back() == *std::max_element(numSet.begin(), numSet.end()));
}

int main()
{
	const int SIZE = 1000;
	const int RANGE = SIZE * 2;
	test_insert_find(SIZE, RANGE);
	test_erase(SIZE, RANGE);
	test_front_back(SIZE, RANGE);
	test_upper_lower_bound(SIZE, RANGE);
	return 0;
}
