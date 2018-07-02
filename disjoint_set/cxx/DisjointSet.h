#include <unordered_map>

class DisjointSet
{
public:
	DisjointSet() { }
	void makeSet(int elem);
	int findSet(int elem);
	void unionSet(int elem1, int elem2);
protected:
	void linkSet(int elem1, int elem2);
	std::unordered_map<int, int> height;
	std::unordered_map<int, int> parent;
};
