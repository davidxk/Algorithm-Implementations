#include "BinarySearchTree.h"
#include <cassert>
#include <climits>
#include <stack>

int BinarySearchTree::front()
{
	assert(root != nullptr && "taking value from empty BST");
	TreeNode* curr = root;
	while(curr->left)
		curr = curr->left;
	return curr->val;
}

int BinarySearchTree::back()
{
	assert(root != nullptr && "taking value from empty BST");
	TreeNode* curr = root;
	while(curr->right)
		curr = curr->right;
	return curr->val;
}

bool BinarySearchTree::insert(int value)
{
	if(root == nullptr)
	{
		root = new TreeNode(value);
		return true;
	}
	TreeNode *prev = nullptr, *curr = root;
	while(curr)
	{
		prev = curr;
		if(value < curr->val)
			curr = curr->left;
		else if(value > curr->val)
			curr = curr->right;
		else
			return false;
	}
	if(value < prev->val)
		prev->left = new TreeNode(value);
	else
		prev->right = new TreeNode(value);
	return true;
}

bool BinarySearchTree::erase(int value)
{
	TreeNode *prev = nullptr, *curr = root;
	while(curr and value != curr->val)
	{
		prev = curr;
		if(value < curr->val)
			curr = curr->left;
		else
			curr = curr->right;
	}
	if(curr == nullptr) return false;
	if(curr->left and curr->right)
	{
		TreeNode* succ = curr->right;
		while(succ->left)
			succ = succ->left;
		succ->left = curr->left;
		curr = curr->right;
	}
	else
		curr = curr->left ? curr->left : curr->right;

	if(value < prev->val)
		prev->left = curr;
	else if(value > prev->val)
		prev->right = curr;
	else
		root = curr;
	return true;
}

bool BinarySearchTree::find(int value)
{
	TreeNode* curr = root;
	while(curr)
	{
		if(value < curr->val)
			curr = curr->left;
		else if(value > curr->val)
			curr = curr->right;
		else
			return true;
	}
	return false;
}

int BinarySearchTree::lower_bound(int value)
{
	assert(root != nullptr && "taking value from empty BST");
	TreeNode* curr = root;
	int lower = INT_MIN;
	while(curr)
	{
		if(value > curr->val)
			curr = curr->right;
		else if(value < curr->val)
		{
			lower = curr->val;
			curr = curr->left;
		}
		else
			return value;
	}
	return lower;
}

int BinarySearchTree::upper_bound(int value)
{
	assert(root != nullptr && "taking value from empty BST");
	TreeNode* curr = root;
	int upper = INT_MAX;
	while(curr)
	{
		if(value > curr->val)
			curr = curr->right;
		else if(value < curr->val)
		{
			upper = curr->val;
			curr = curr->left;
		}
		else
			// Note upper_bound and lower_bound are not defined symmetrically
			curr = curr->right;
	}
	return upper;
}

BinarySearchTree::~BinarySearchTree()
{
	if(this->empty())
		return;
	std::stack<TreeNode*> front;
	front.push(root);
	TreeNode* node;
	while(not front.empty())
	{
		node = front.top();
		front.pop();
		if(node->left)
			front.push(node->left);
		if(node->right)
			front.push(node->right);
		delete node;
	}
}
