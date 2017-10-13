#include "RMQSegmentTree.h"

#include <algorithm>
#include <climits>
#include <cmath>

RMQSegmentTree::RMQSegmentTree(const std::vector<int>& array)
{
	this->length = array.size();
	int x = (int) log2(array.size()) + 1;
	int size = pow(2, x) * 2;
	tree = std::vector<int>(size);
	build(0, array, 0, this->length - 1);
}

// Structured like a merge sort
void RMQSegmentTree::build(int index, const std::vector<int>& array, int left, int right)
{
	if(left >= right)
	{
		tree[index] = array[left];
		return;
	}
	int center = left + (right - left) / 2;
	build(index * 2 + 1, array, left, center);
	build(index * 2 + 2, array, center + 1, right);
	tree[index] = std::min(tree[index * 2 + 1], tree[index * 2 + 2]);
}

int RMQSegmentTree::query(int qLeft, int qRight)
{
	return queryUtil(0, qLeft, qRight, 0, this->length - 1);
}

// Structured like a quick select
int RMQSegmentTree::queryUtil(int index, int qLeft, int qRight, int left, int right)
{
	if(qLeft <= left and right <= qRight)
		return tree[index];

	if(right < qLeft or qRight < left)
		return INT_MAX;

	int center = left + (right - left) / 2;
	return std::min(queryUtil(2 * index + 1, qLeft, qRight, left, center),
			queryUtil(2 * index + 2, qLeft, qRight, center + 1, right));
}

void RMQSegmentTree::update(int index, int delta)
{
	updateUtil(index, delta, 0, 0, this->length - 1);
}

void RMQSegmentTree::updateUtil(int index, int delta, int i, int left, int right)
{
	if(left >= right)
	{
		tree[i] += delta;
		return;
	}
	int center = left + (right - left) / 2;
	if(index <= center)
		updateUtil(index, delta, 2 * i + 1, left, center);
	else
		updateUtil(index, delta, 2 * i + 2, center + 1, right);
	tree[i] = std::min(tree[2 * i + 1], tree[2 * i + 2]);
}
