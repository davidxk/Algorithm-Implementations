#include "RecursiveTraversal.cxx"
#include "MorrisTraversal.cxx"
#include "StackTraversal.cxx"
#include "TraversalMethods.h"
#include "TreeNode.h"
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <queue>
#include <random>
#include <vector>

int pick_and_take(std::vector<int>& pool)
{
	int rand_pick = rand() % pool.size();
	int result = pool[rand_pick];
	std::swap(pool[rand_pick], pool.back());
	pool.pop_back();
	return result;
}

TreeNode* generate_random_tree(int size)
{
	std::vector<int> pool;
	for(int i = 0; i < size; i++)
		pool.push_back(i);
	unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
	std::shuffle(pool.begin(), pool.end(), std::default_random_engine(seed));

	TreeNode* root = new TreeNode(pick_and_take(pool));
	std::queue<TreeNode*> fringe;
	fringe.push(root);
	for(int i = 1; i < size - 1; i++)
	{
		TreeNode* node = fringe.front();
		fringe.pop();
		if((float)rand() / RAND_MAX < 0.7f)
		{
			node->left = new TreeNode(pick_and_take(pool));
			fringe.push(node->left);
			i++;
		}
		if((float)rand() / RAND_MAX < 0.7f or fringe.empty())
		{
			node->right = new TreeNode(pick_and_take(pool));
			fringe.push(node->right);
			i++;
		}
	}
	return root;
}

bool test_traversal_methods(TraversalMethods* impl, int size = 100)
{
	TreeNode* root = generate_random_tree(size);
	std::string tag[] = {"preorder", "inorder", "postorder"};
	RecursiveTraversal rcur;

	std::vector<int> ans[3];
	ans[0] = rcur.preorderTraversal(root);
	ans[1] = rcur.inorderTraversal(root);
	ans[2] = rcur.postorderTraversal(root);

	std::vector<int> ret[3];
	ret[0] = impl->preorderTraversal(root);
	ret[1] = impl->inorderTraversal(root);
	ret[2] = impl->postorderTraversal(root);

	for(int i = 0; i < 3; i++)
	{
		if(ans[i].size() != ret[i].size())
			return false;
		for(int j = 0; j < ans[i].size(); j++)
			if(ret[i][j] != ans[i][j])
			{
				std::cout<<tag[i]<<" error! "<<std::endl;
				return false;
			}
	}
        
	return true;
}

int main()
{
	std::vector<TraversalMethods*> impls;
	impls.push_back(new StackTraversal());
	impls.push_back(new MorrisTraversal());
	for(int i = 0; i < impls.size(); i++)
		if(not test_traversal_methods(impls[i]))
			std::cout<<"WA: impl "<<i<<std::endl;
	return 0;
}
