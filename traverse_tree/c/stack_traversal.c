#include "TreeNode.h"
#include "../../vector/myvector.h"

int* preorderTraversal(struct TreeNode* root, int* returnSize)
{
	struct myvector result;
	struct myvector stack;
	struct TreeNode* cur;
	while(cur && !stack.empty(&stack))
	{
		while(cur)
		{
			stack.push_back(&stack, (int)cur);
			result.push_back(&result, cur->val);
			cur = cur->left;
		}
		cur = (struct TreeNode*) stack.back(&stack);
		stack.pop_back(&stack);
		cur = cur->right;
	}

	*returnSize = result.size(&result);
	return result.data;
}
