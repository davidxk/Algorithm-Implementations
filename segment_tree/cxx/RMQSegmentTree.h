#include <vector>

class RMQSegmentTree
{
public:
	RMQSegmentTree(const std::vector<int>& array);
	void build(int index, const std::vector<int>& array, int left, int right);
	int query(int qLeft, int qRight);
	void update(int index, int delta);
protected:
	int queryUtil(int index, int qLeft, int qRight, int left, int right);
	void updateUtil(int index, int delta, int i, int left, int right);
private:
	std::vector<int> tree;
	int length;
};
