#include "TreeNode.h"
#include <stdlib.h>

static int cnt = 0;
static void preorder(struct TreeNode* root, int* result)
{
	if(root)
	{
		result[cnt++] = root->val;
		preorder(root->left, result);
		preorder(root->right, result);
	}
}

int* recursive_preorder(struct TreeNode* root, int* returnSize)
{
	int* result = (int*) malloc(sizeof(int) * (*returnSize));
	cnt = 0;
	preorder(root, result);
	return result;
}

static void inorder(struct TreeNode* root, int* result)
{
	if(root != NULL)
	{
		inorder(root->left, result++);
		result[cnt++] = root->val;
		inorder(root->right, result++);
	}
}

int* recursive_inorder(struct TreeNode* root, int* returnSize)
{
	int* result = (int*) malloc(sizeof(int) * (*returnSize));
	cnt = 0;
	inorder(root, result);
	return result;
}

static void postorder(struct TreeNode* root, int* result)
{
	if(root)
	{
		postorder(root->left, result);
		postorder(root->right, result);
		result[cnt++] = root->val;
	}
}

int* postorderTravesal(struct TreeNode* root, int* returnSize)
{
	int* result = (int*) malloc(sizeof(int) * (*returnSize));
	cnt = 0;
	postorder(root, result);
	return result;
}
