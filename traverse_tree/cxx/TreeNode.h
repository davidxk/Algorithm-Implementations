#ifndef __TREE_NODE__
#define __TREE_NODE__

#include <iostream>

struct TreeNode
{
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

#endif
