#ifndef __LINKED_LIST__
#define __LINKED_LIST__

#include <vector>

struct ListNode
{
	int val;
	ListNode* next;
	ListNode(int x) : val(x), next(NULL) {}
};

ListNode* getLinkedList(std::vector<int> array);
std::vector<int> getArray(ListNode* head);
void destroyLinkedList(ListNode* head);

#endif
