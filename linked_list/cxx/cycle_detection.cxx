#include "LinkedList.h"

bool cycle_detection(ListNode* head)
{
	ListNode *slow = head, *fast = head;
	while(fast and fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if(slow == fast)
			return true;
	}
	return false;
}

ListNode* cycle_finding(ListNode* head)
{
	ListNode *slow = head, *fast = head;
	while(fast and fast->next)
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
