#include <vector>

class DisjointSet
{
public:
	DisjointSet(int nElems);
	int findSet(int elem);
	void unionSet(int elem1, int elem2);
protected:
	void linkSet(int root1, int root2);
	std::vector<int> height;
	std::vector<int> parent;
};
