#ifndef __TRAVERSAL_METHODS__
#define __TRAVERSAL_METHODS__

#include "TreeNode.h"
#include <vector>

class TraversalMethods
{
public:
	virtual std::vector<int> preorderTraversal(TreeNode* root) = 0;
	virtual std::vector<int> inorderTraversal(TreeNode* root) = 0;
	virtual std::vector<int> postorderTraversal(TreeNode* root) = 0;
};

#endif
