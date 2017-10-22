#include "linked_list.h"

ListNode* reverse_linked_list(ListNode* head)
{
	ListNode *prev = 0, *curr = head, *next = 0;
	while(curr)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	return prev;
}
