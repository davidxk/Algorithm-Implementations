#include "linked_list.h"

#include <stdlib.h>

ListNode* get_list_node(int value)
{
	ListNode* node = (ListNode*) malloc(sizeof(ListNode));
	node->val = value;
	node->next = NULL;
	return node;
}

ListNode* get_linked_list(int* array, int n)
{
	if(n == 0)
		return 0;

	int i;
	ListNode* head = get_list_node(array[0]);
	ListNode* curr = head;

	for(i = 1; i < n; i++)
	{
		curr->next = get_list_node(array[i]);
		curr = curr->next;
	}
	return head;
}

int* get_array(ListNode* head)
{
	ListNode* curr = head;
	int cnt = 0;
	while(curr)
	{
		cnt++;
		curr = curr->next;
	}

	int* array = (int*) malloc(sizeof(int) * cnt);
	curr = head;
	int i;
	for(i = 0; i < cnt; i++)
	{
		array[i] = curr->val;
		curr = curr->next;
	}
	return array;
}

void destroy_linked_list(ListNode* head)
{
	while(head)
	{
		free(head);
		head = head->next;
	}
}
