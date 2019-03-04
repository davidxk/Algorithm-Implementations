#include "SkipList.h"

#include <limits>

SkipNode::SkipNode(int k, int v, int level): key(k), value(v)
{
	for(int i = 0; i < level; i++)
		forward.push_back(NULL);
}

SkipList::SkipList(): probability(0.5), maxLevel(16)
{
	int headKey = std::numeric_limits<int>::min();
	head = new SkipNode(headKey, 0, maxLevel);

	int tailKey = std::numeric_limits<int>::max();
    tail = new SkipNode(tailKey, 0, maxLevel);

	for(int i = 0; i < head->forward.size(); i++)
		head->forward[i] = tail;
}

SkipNode* SkipList::find(int key)
{
	SkipNode* curr = head;
	int currentMaximum = nodeLevel(head->forward);
}
