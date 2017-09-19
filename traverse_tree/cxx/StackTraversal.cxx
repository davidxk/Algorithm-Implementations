#include <algorithm>
#include <stack>
#include <vector>
#include "TraversalMethods.h"
#include "TreeNode.h"
using namespace std;

class StackTraversal: public TraversalMethods
{
public:
	vector<int> preorderTraversal(TreeNode* root);
	vector<int> inorderTraversal(TreeNode* root);
	vector<int> postorderTraversal(TreeNode* root);
};

vector<int> StackTraversal::preorderTraversal(TreeNode* root)
{
	vector<int> result;
	stack<TreeNode*> fringe;
	TreeNode* cur = root;
	while(cur or not fringe.empty())
	{
		while(cur)
		{
			fringe.push(cur);
			result.push_back(cur->val);
			cur = cur->left;
		}
		cur = fringe.top();
		fringe.pop();
		cur = cur->right;
	}
	return result;
}

vector<int> StackTraversal::inorderTraversal(TreeNode* root)
{
	vector<int> result;
	TreeNode* cur = root;
	stack<TreeNode*> fringe;
	while(cur or not fringe.empty())
	{
		while(cur)
		{
			fringe.push(cur);
			cur = cur->left;
		}
		cur = fringe.top();
		fringe.pop();
		result.push_back(cur->val);
		cur = cur->right;
	}
	return result;
}

vector<int> StackTraversal::postorderTraversal(TreeNode* root)
{
	vector<int> result;
	TreeNode* cur = root;
	stack<TreeNode*> fringe;
	while(cur or not fringe.empty())
	{
		while(cur)
		{
			fringe.push(cur);
			result.push_back(cur->val);
			cur = cur->right;
		}
		cur = fringe.top();
		fringe.pop();
		cur = cur->left;
	}
	for(int i = 0; i < result.size()/2; i++)
		swap(result[i], result[result.size() - 1 - i]);
	return result;
}
