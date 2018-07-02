#include "BinarySearchTree.h"
#include <cassert>
#include <climits>
#include <stack>

int BinarySearchTree::begin()
{
	assert(root != NULL && "taking value from empty BST");
	TreeNode* curr = root;
	while(curr->left)
		curr = curr->left;
	return curr->val;
}

int BinarySearchTree::end()
{
	assert(root != NULL && "taking value from empty BST");
	TreeNode* curr = root;
	while(curr->right)
		curr = curr->right;
	return curr->val;
}

bool BinarySearchTree::insert(int value)
{
	if(root == NULL)
	{
		root = new TreeNode(value);
		return true;
	}
	TreeNode *prev = NULL, *curr = root;
	while(curr)
	{
		prev = curr;
		if(value == curr->val)
			return false;
		else if(value < curr->val)
			curr = curr->left;
		else
			curr = curr->right;
	}
	if(value < prev->val)
		prev->left = new TreeNode(value);
	else
		prev->right = new TreeNode(value);
	return true;
}

bool BinarySearchTree::erase(int value)
{
	TreeNode *prev = NULL, *curr = root;
	while(curr and value != curr->val)
	{
		prev = curr;
		if(value < curr->val)
			curr = curr->left;
		else
			curr = curr->right;
	}
	if(curr == NULL) return false;
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

	if(prev == NULL)
		root = curr;
	else if(value < prev->val)
		prev->left = curr;
	else
		prev->right = curr;
	return true;
}

bool BinarySearchTree::find(int value)
{
	TreeNode* curr = root;
	while(curr)
	{
		if(value == curr->val)
			return true;
		else if(value < curr->val)
			curr = curr->left;
		else
			curr = curr->right;
	}
	return false;
}

int BinarySearchTree::lower_bound(int value)
{
	assert(root != NULL && "taking value from empty BST");
	TreeNode* curr = root;
	int lower = INT_MIN;
	while(curr)
	{
		if(value == curr->val)
			return value;
		else if(value < curr->val)
		{
			lower = curr->val;
			curr = curr->left;
		}
		else
			curr = curr->right;
	}
	return lower;
}

int BinarySearchTree::upper_bound(int value)
{
	assert(root != NULL && "taking value from empty BST");
	TreeNode* curr = root;
	int upper = INT_MAX;
	while(curr)
	{
		if(value == curr->val)
			curr = curr->right;
		else if(value < curr->val)
		{
			upper = curr->val;
			curr = curr->left;
		}
		else
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
