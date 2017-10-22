#include "LinkedList.h"

ListNode* find_middle(ListNode* head)
{
	if(head == NULL)
		return head;

	ListNode *slow = head, *fast = head;
	while(fast->next and fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	return slow;
}
