#include "RecursiveTraversal.cxx"
#include "MorrisTraversal.cxx"
#include "StackTraversal.cxx"
#include "TraversalMethods.h"
#include "TreeNode.h"
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int pick_and_take(vector<int>& pool)
{
	int rand_pick = rand() % pool.size();
	int result = pool[rand_pick];
	swap(pool[rand_pick], pool.back());
	pool.pop_back();
	return result;
}

TreeNode* generate_random_tree(int size)
{
	vector<int> pool;
	for(int i = 0; i < size; i++)
		pool.push_back(i);
	random_shuffle(pool.begin(), pool.end());

	TreeNode* root = new TreeNode(pick_and_take(pool));
	queue<TreeNode*> fringe;
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
	string tag[] = {"preorder", "inorder", "postorder"};
	RecursiveTraversal rcur;

	vector<int> ans[3];
	ans[0] = rcur.preorderTraversal(root);
	ans[1] = rcur.inorderTraversal(root);
	ans[2] = rcur.postorderTraversal(root);

	vector<int> ret[3];
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
				cout<<tag[i]<<" error! "<<endl;
				return false;
			}
	}
        
	return true;
}

int main()
{
	vector<TraversalMethods*> impls;
	impls.push_back(new StackTraversal());
	impls.push_back(new MorrisTraversal());
	for(int i = 0; i < impls.size(); i++)
		if(not test_traversal_methods(impls[i]))
			cout<<"WA: impl "<<i<<endl;
	return 0;
}
