#include "linked_list.h"

ListNode* find_middle(ListNode* head)
{
	if(head == 0)
		return head;

	ListNode *slow = head, *fast = head;
	while(fast->next && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	return slow;
}
