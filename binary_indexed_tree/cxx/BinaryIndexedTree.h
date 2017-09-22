#include <vector>

class BinaryIndexedTree
{
public:
	BinaryIndexedTree(std::vector<int> array);
	int getSum(int i);
	void update(int i, int delta);
	int getRange(int i, int j);
private:
	std::vector<int> tree;
};
