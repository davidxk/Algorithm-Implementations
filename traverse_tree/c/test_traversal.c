#include <stdio.h>
#include <stdlib.h>
#include "morris_traversal.c"
#include "TreeNode.h"

void shuffle(int* array, int size)
{
	int i, j, tmp;
	for(i = 0; i < size; i++)
	{
		j = rand() % size;

		tmp = array[i];
		array[i] = array[j];
		array[j] = tmp;
	}
}

struct TreeNode* generate_random_tree(int size)
{
	int* pool = (int*) malloc(sizeof(int) * size);
	int i;
	for(i = 0; i < size; i++)
		pool[i] = i;
	i = 0;
	struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
	root->val = pool[i++];
	// I need a deque<struct TreeNode*>
	for(i = 0; i < size; i++)
	{

	}
	free(pool);
	return root;
}

int test_traversal_methods(int* (*func)(struct TreeNode*, int*), int size)
{
	struct TreeNode* root = generate_random_tree(size);
	root = 0;
	return 1;
}

int main()
{
	typedef int* (*traversal)(struct TreeNode*, int*);
	traversal funcs[] = { morris_preorder };
	int i;
	for(i = 0; i < 1; i++)
		if(!test_traversal_methods(funcs[i], 0))
			printf("WA: func at funcs[%d]", i);
}
