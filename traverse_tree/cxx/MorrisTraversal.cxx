#include <vector>
#include "TraversalMethods.h"
#include "TreeNode.h"
using namespace std;

class MorrisTraversal: public TraversalMethods
{
public:
	vector<int> preorderTraversal(TreeNode* root);
	vector<int> inorderTraversal(TreeNode* root);
	vector<int> postorderTraversal(TreeNode* root);
private:
	void traceBack(TreeNode* from, TreeNode* to, vector<int>& result);
};

vector<int> MorrisTraversal::preorderTraversal(TreeNode* root)
{
	vector<int> result;
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

vector<int> MorrisTraversal::inorderTraversal(TreeNode* root)
{
	vector<int> result;
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

vector<int> MorrisTraversal::postorderTraversal(TreeNode* root)
{
	TreeNode* dummy = new TreeNode(0);
	dummy->left = root;
	
	vector<int> result;
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

void MorrisTraversal::traceBack(TreeNode* from, TreeNode* to, vector<int>& result)
{
	TreeNode* cur = from;
	vector<int> reverse;
	while(cur != to)
	{
		reverse.push_back(cur->val);
		cur = cur->right;
	}
	reverse.push_back(to->val);
	for(vector<int>::reverse_iterator it = reverse.rbegin();
			it != reverse.rend(); it++)
		result.push_back(*it);
}
