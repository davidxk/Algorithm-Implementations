#include "linked_list.h"

ListNode* find_middle(ListNode* head)
{
	ListNode *slow = head, *fast = head;
	while(fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	return slow;
}
