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
	TreeNode* curr = root;
	while(curr or not fringe.empty())
	{
		while(curr)
		{
			fringe.push(curr);
			result.push_back(curr->val);
			curr = curr->left;
		}
		curr = fringe.top();
		fringe.pop();
		curr = curr->right;
	}
	return result;
}

vector<int> StackTraversal::inorderTraversal(TreeNode* root)
{
	vector<int> result;
	TreeNode* curr = root;
	stack<TreeNode*> fringe;
	while(curr or not fringe.empty())
	{
		while(curr)
		{
			fringe.push(curr);
			curr = curr->left;
		}
		curr = fringe.top();
		fringe.pop();
		result.push_back(curr->val);
		curr = curr->right;
	}
	return result;
}

vector<int> StackTraversal::postorderTraversal(TreeNode* root)
{
	vector<int> result;
	TreeNode* curr = root;
	stack<pair<TreeNode*, bool> > fringe;
	while(curr or not fringe.empty())
	{
		while(curr)
		{
			fringe.push({curr, false});
			curr = curr->left;
		}
		if(fringe.top().second == false)
		{
			fringe.top().second = true;
			curr = fringe.top().first->right;
		}
		else
		{
			result.push_back(fringe.top().first->val);
			fringe.pop();
		}
	}
	return result;
}
