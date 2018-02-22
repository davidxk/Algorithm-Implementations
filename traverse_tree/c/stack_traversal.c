#include <stdlib.h>
#include "TreeNode.h"
#include "../../vector/myvector.h"

int* stack_preorder(struct TreeNode* root, int* returnSize)
{
	int* result = (int*) malloc(sizeof(int) * (*returnSize));
	int cnt = 0;

	struct myvector stack;
	struct TreeNode* curr = root;
	while(curr && !stack.empty(&stack))
	{
		while(curr)
		{
			stack.push_back(&stack, curr);
			result[cnt++] = curr->val;
			curr = curr->left;
		}
		curr = (struct TreeNode*) stack.back(&stack);
		stack.pop_back(&stack);
		curr = curr->right;
	}
	return result;
}

int* stack_inorder(struct TreeNode* root, int* returnSize)
{
	int* result = (int*) malloc(sizeof(int) * (*returnSize));
	int cnt = 0;

	struct myvector stack;
	struct TreeNode* curr = root;
	while(curr || !stack.empty(&stack))
	{
		while(curr)
		{
			stack.push_back(&stack, curr);
			curr = curr->left;
		}
		curr = stack.back(&stack);
		stack.pop_back(&stack);
		result[cnt++] = curr->val;
		curr = curr->right;
	}
	return result;
}

int* stack_postorder(struct TreeNode* root, int* returnSize)
{
	struct pair { struct TreeNode* node; int visited; };
	int* result = (int*) malloc(sizeof(int) * (*returnSize));
	int cnt = 0;

	struct myvector stack;
	struct TreeNode* curr = root;
	struct pair* top;
	while(curr || !stack.empty(&stack))
	{
		while(curr)
		{
			struct pair* item = (struct pair*) malloc(sizeof(struct pair));
			item->node = curr;
			item->visited = 0;
			stack.push_back(&stack, item);
			curr = curr->left;
		}
		top = stack.back(&stack);
		if(top->visited == 0)
		{
			top->visited = 1;
			curr = top->node->right;
		}
		else
		{
			result[cnt++] = top->node->val;
			stack.pop_back(&stack);
			free(top);
		}
	}
	return result;
}
