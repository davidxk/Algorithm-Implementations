#include <vector>

class SkipNode
{
public:
	SkipNode(int k, int v, int level);
public:
	int key;
	int value;
	std::vector<SkipNode*> forward;
};

class SkipList
{
public:
	SkipList();
	SkipNode* find(int key);
	void add(int key, int value);
	void remove(int key);
	~SkipList();
protected:
	int randomLevel();
	int nodeLevel(const std::vector<SkipNode*> forward);
private:
	SkipNode* head;
	SkipNode* tail;
	float probability;
	int maxLevel;
};
