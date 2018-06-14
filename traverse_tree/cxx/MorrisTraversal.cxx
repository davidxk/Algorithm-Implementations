#include <vector>
#include "TraversalMethods.h"
#include "TreeNode.h"

class MorrisTraversal: public TraversalMethods
{
public:
	std::vector<int> preorderTraversal(TreeNode* root);
	std::vector<int> inorderTraversal(TreeNode* root);
	std::vector<int> postorderTraversal(TreeNode* root);
private:
	void traceBack(TreeNode* from, TreeNode* to, std::vector<int>& result);
};

std::vector<int> MorrisTraversal::preorderTraversal(TreeNode* root)
{
	std::vector<int> result;
	TreeNode *cur = root, *node = NULL;
	while(cur)
	{
		if(cur->left == NULL)
		{
			result.push_back(cur->val);
			cur = cur->right;
		}
		else
		{
			node = cur->left;
			while(node->right != NULL && node->right != cur)
				node = node->right;

			if(node->right == NULL)
			{
				result.push_back(cur->val);
				node->right = cur;
				cur = cur->left;
			}
			else
			{
				node->right = NULL;
				cur = cur->right;
			}
		}
	}

	return result;
}

std::vector<int> MorrisTraversal::inorderTraversal(TreeNode* root)
{
	std::vector<int> result;
	TreeNode *cur = root, *node = NULL;
	while(cur)
	{
		if(cur->left == NULL)
		{
			result.push_back(cur->val);
			cur = cur->right;
		}
		else
		{
			node = cur->left;
			while(node->right != NULL && node->right != cur)
				node = node->right;

			if(node->right == NULL)
			{
				node->right = cur;
				cur = cur->left;
			}
			else
			{
				node->right = NULL;
				result.push_back(cur->val);
				cur = cur->right;
			}
		}
	}
	return result;
}

std::vector<int> MorrisTraversal::postorderTraversal(TreeNode* root)
{
	TreeNode* dummy = new TreeNode(0);
	dummy->left = root;
	
	std::vector<int> result;
	TreeNode *cur = dummy, *node = NULL;
	while(cur)
	{
		if(cur->left == NULL)
		{
			cur = cur->right;
		}
		else
		{
			node = cur->left;
			while(node->right != NULL && node->right != cur)
				node = node->right;
			if(node->right == NULL)
			{
				node->right = cur;
				cur = cur->left;
			}
			else
			{
				traceBack(cur->left, node, result);
				node->right = NULL;
				cur = cur->right;
			}
		}
	}
	delete dummy;
	return result;
}

void MorrisTraversal::traceBack(TreeNode* from, TreeNode* to, std::vector<int>& result)
{
	TreeNode* cur = from;
	std::vector<int> reverse;
	while(cur != to)
	{
		reverse.push_back(cur->val);
		cur = cur->right;
	}
	reverse.push_back(to->val);
	for(std::vector<int>::reverse_iterator it = reverse.rbegin();
			it != reverse.rend(); it++)
		result.push_back(*it);
}
