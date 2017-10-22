#ifndef _LINKED_LIST_H_
#define _LINKED_LIST_H_

typedef struct list_node {
	int val;
	struct list_node *next;
} ListNode;

ListNode* get_list_node(int value);
ListNode* get_linked_list(int* array, int n);
int* get_array(ListNode* head);
void destroy_linked_list(ListNode* head);

#endif
