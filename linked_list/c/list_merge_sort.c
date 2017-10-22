#include "list_merge_sort.h"
#include "linked_list.h"
#include <stdlib.h>

static ListNode* find_middle(ListNode* head);

ListNode* list_merge_sort(ListNode* head)
{
	if(head == 0)
		return head;
	return list_m_sort(head);
}

ListNode* find_middle(ListNode* head)
{
	ListNode *slow = head, *fast = head;
	while(fast->next && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	return slow;
}

ListNode* list_m_sort(ListNode* head)
{
	if(head->next == 0)
		return head;
	ListNode* slow = find_middle(head);
	ListNode* midd = slow->next;
	slow->next = 0;

	head = list_m_sort(head);
	midd = list_m_sort(midd);

	return list_merge(head, midd);
}

ListNode* list_merge(ListNode* l1, ListNode* l2)
{
	ListNode* dummy = (ListNode*) malloc(sizeof(ListNode));
	ListNode* curr = dummy;
	while(l1 && l2)
	{
		if(l1->val < l2->val)
		{
			curr->next = l1;
			l1 = l1->next;
		}
		else
		{
			curr->next = l2;
			l2 = l2->next;
		}
		curr = curr->next;
	}
	curr->next = l1 ? l1 : l2;
	curr = dummy->next;
	free(dummy);
	return curr;
}
