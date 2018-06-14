#include "TraversalMethods.h"
#include "TreeNode.h"
#include <vector>

class RecursiveTraversal: public TraversalMethods
{
public:
	std::vector<int> preorderTraversal(TreeNode* root);
	std::vector<int> inorderTraversal(TreeNode* root);
	std::vector<int> postorderTraversal(TreeNode* root);
private:
	void preorder_helper(TreeNode* root, std::vector<int>& result);
	void inorder_helper(TreeNode* root, std::vector<int>& result);
	void postorder_helper(TreeNode* root, std::vector<int>& result);
};

std::vector<int> RecursiveTraversal::preorderTraversal(TreeNode* root)
{
	std::vector<int> result;
	preorder_helper(root, result);
	return result;
}

void RecursiveTraversal::preorder_helper(TreeNode* root, std::vector<int>& result)
{
	if(root != NULL)
	{
		result.push_back(root->val);
		preorder_helper(root->left, result);
		preorder_helper(root->right, result);
	}
}

std::vector<int> RecursiveTraversal::inorderTraversal(TreeNode* root)
{
	std::vector<int> result;
	inorder_helper(root, result);
	return result;
}

void RecursiveTraversal::inorder_helper(TreeNode* root, std::vector<int>& result)
{
	if(root != NULL)
	{
		inorder_helper(root->left, result);
		result.push_back(root->val);
		inorder_helper(root->right, result);
	}
}

std::vector<int> RecursiveTraversal::postorderTraversal(TreeNode* root)
{
	std::vector<int> result;
	postorder_helper(root, result);
	return result;
}

void RecursiveTraversal::postorder_helper(TreeNode* root, std::vector<int>& result)
{
	if(root != NULL)
	{
		postorder_helper(root->left, result);
		postorder_helper(root->right, result);
		result.push_back(root->val);
	}
}
