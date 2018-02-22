#include "TreeNode.h"
#include "../../vector/myvector.h"
#include <stdlib.h>

int* morris_preorder(struct TreeNode* root, int* returnSize)
{
	int* result = (int*) malloc(sizeof(int) * (*returnSize));
	int cnt = 0;
	struct TreeNode *curr = root, *node;
	while(curr)
	{
		if(curr->left == NULL)
		{
			result[cnt++] = curr->val;
			curr = curr->right;
		}
		else
		{
			node = curr->left;
			while(node->right && node->right != curr)
				node = node->right;

			if(node->right == NULL)
			{
				result[cnt++] = curr->val;
				node->right = curr;
				curr = curr->left;
			}
			else
			{
				node->right = NULL;
				curr = curr->right;
			}
		}
	}
	return result;
}


