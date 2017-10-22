#include "LinkedList.h"

ListNode* getLinkedList(std::vector<int> array)
{
	if(array.empty())
		return NULL;

	ListNode* head = new ListNode(array[0]);
	ListNode* curr = head;
	for(int i = 1; i < array.size(); i++)
	{
		curr->next = new ListNode(array[i]);
		curr = curr->next;
	}
	return head;
}

std::vector<int> getArray(ListNode* head)
{
	std::vector<int> array;
	ListNode* curr = head;
	while(curr)
	{
		array.push_back(curr->val);
		curr = curr->next;
	}
	return array;
}

void destroyLinkedList(ListNode* head)
{
	while(head != NULL)
	{
		delete head;
		head = head->next;
	}
}
