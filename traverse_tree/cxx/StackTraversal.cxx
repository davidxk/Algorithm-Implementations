#include <algorithm>
#include <stack>
#include <vector>
#include "TraversalMethods.h"
#include "TreeNode.h"

class StackTraversal: public TraversalMethods
{
public:
	std::vector<int> preorderTraversal(TreeNode* root);
	std::vector<int> inorderTraversal(TreeNode* root);
	std::vector<int> postorderTraversal(TreeNode* root);
	std::vector<int> callStackSimulation(TreeNode* root);
};

std::vector<int> StackTraversal::preorderTraversal(TreeNode* root)
{
	std::vector<int> result;
	std::stack<TreeNode*> fringe;
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

std::vector<int> StackTraversal::inorderTraversal(TreeNode* root)
{
	std::vector<int> result;
	TreeNode* curr = root;
	std::stack<TreeNode*> fringe;
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

std::vector<int> StackTraversal::postorderTraversal(TreeNode* root)
{
	std::vector<int> result;
	TreeNode* curr = root;
	std::stack<std::pair<TreeNode*, bool> > fringe;
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

// TESTED but not included in routine unit test
std::vector<int> StackTraversal::callStackSimulation(TreeNode* root)
{
	std::vector<int> result;
	std::deque<std::pair<int, TreeNode*> > stack;
	std::vector<std::function<void (TreeNode*)> > statements = {
		[&](TreeNode* root) {
			if(root == nullptr)
				stack.pop_back();
		},
		[&](TreeNode* root) {
			stack.emplace_back(0, root->left);
		},
		[&](TreeNode* root) {
			stack.emplace_back(0, root->right);
		},
		[&](TreeNode* root) {
			result.push_back(root->val);
		}
	};
	stack.emplace_back(0, root);
	while(!stack.empty())
	{
		int& eip = stack.back().first;
		if(eip == statements.size())
		{
			stack.pop_back();
			continue;
		}
		TreeNode* node = stack.back().second;
		statements[eip++](node);
	}
	return result;
}
