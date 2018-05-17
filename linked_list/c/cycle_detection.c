#include "linked_list.h"
#include <stddef.h>

int cycle_detection(ListNode* head)
{
	ListNode *slow = head, *fast = head;
	while(fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if(slow == fast)
			return 1;
	}
	return 0;
}

ListNode* cycle_finding(ListNode* head)
{
	ListNode *slow = head, *fast = head;
	while(fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if(slow == fast)
		{
			slow = head;
			while(slow != fast)
			{
				slow = slow->next;
				fast = fast->next;
			}
			return fast;
		}
	}
	return NULL;
}
