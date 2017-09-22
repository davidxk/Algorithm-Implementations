#include "BinaryIndexedTree.h"
#include <cmath>

BinaryIndexedTree::BinaryIndexedTree(std::vector<int> array)
{
	this->tree.push_back(0);
	for(int elem: array)
		this->tree.push_back(elem);
	int j;
	for(int i = 0; i < this->tree.size(); i++)
	{
		j = i + (i & (-i));
		if(j < this->tree.size())
			this->tree[j] += this->tree[i];
	}
}

int BinaryIndexedTree::getSum(int i)
{
	i += 1;
	int sum = 0;
	while(i > 0)
	{
		sum += this->tree[i];
		i -= i & (-i);
	}
	return sum;
}

void BinaryIndexedTree::update(int i, int delta)
{
	i += 1;
	while(i <= this->tree.size())
	{
		this->tree[i] += delta;
		i += i & (-i);
	}
}

int BinaryIndexedTree::getRange(int i, int j)
{
	return getSum(j) - getSum(i - 1);
}
