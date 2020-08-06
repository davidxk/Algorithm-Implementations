struct TreeNode
{
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// All methods that returns an iterator in std returns the corresponding value
class BinarySearchTree
{
public:
	BinarySearchTree(): root(nullptr) { }
	~BinarySearchTree();
	int front();
	int back();
	bool empty() { return root == nullptr; }
	bool insert(int value);
	bool erase(int value);
	bool find(int value);
	int lower_bound(int value);
	int upper_bound(int value);
protected:
	TreeNode* root;
};
