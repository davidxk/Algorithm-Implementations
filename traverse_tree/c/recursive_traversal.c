#include "TreeNode.h"
#include "myvector.h"
#include <stdlib.h>

static void preorder(struct TreeNode* root, struct myvector* result)
{
	if(root)
	{
		result->push_back(result, root->val);
		preorder(root->left, result);
		preorder(root->right, result);
	}
}

int* preorderTraversal(struct TreeNode* root, int* returnSize)
{
	struct myvector result;
	preorder(root, &result);
	*returnSize = result.size(&result);
	return result.data;
}

static void inorder(struct TreeNode* root, struct myvector* result)
{
	if(root != NULL)
	{
		inorder(root->left, result++);
		result->push_back(result, root->val);
		inorder(root->right, result++);
	}
}

int* inorderTraversal(struct TreeNode* root, int* returnSize)
{
	struct myvector result;
	inorder(root, &result);
	*returnSize = result.size(&result);
	return result.data;
}

static void postorder(struct TreeNode* root, struct myvector* result)
{
	if(root)
	{
		postorder(root->left, result);
		postorder(root->right, result);
		result->push_back(result, root->val);
	}
}

int* postorderTravesal(struct TreeNode* root, int* returnSize)
{
	struct myvector result;
	postorder(root, &result);
	*returnSize = result.size(&result);
	return result.data;
}
