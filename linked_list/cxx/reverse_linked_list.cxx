#include "LinkedList.h"

ListNode* reverse_linked_list(ListNode* head)
{
	ListNode *prev = NULL, *curr = head, *next = NULL;
	while(curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	return prev;
}
