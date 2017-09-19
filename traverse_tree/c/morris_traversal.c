#include "TreeNode.h"
#include "myvector.h"
#include <stdlib.h>

int* preorderTraversal(struct TreeNode* root, int* returnSize)
{
	struct myvector result;
	struct TreeNode *cur, *node;
	while(cur)
	{
		if(cur->left == NULL)
		{
			result.push_back(&result, cur->val);
			cur = cur->right;
		}
		else
		{
			node = cur->left;
			while(node->right && node->right != cur)
				node = node->right;

			if(node->right == NULL)
			{
				result.push_back(&result, cur->val);
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
	*returnSize = result.size(&result);
	return result.data;
}


