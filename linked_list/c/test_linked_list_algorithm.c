#include "linked_list.h"
#include <assert.h>
#include <stdlib.h>
#include <time.h>
#include "find_middle.h"
#include "reverse_linked_list.h"
#include "cycle_detection.h"
#include "list_merge_sort.h"

void test_find_middle(int size)
{
	int* array = (int*) malloc(sizeof(int) * size);
	int i;
	for(i = 0; i < size; i++)
		array[i] = i;
	ListNode* head = get_linked_list(array, size);
	ListNode* middle = find_middle(head);
	assert(middle->val == size / 2);
	free(array);
	destroy_linked_list(head);
}

void test_reverse_linked_list()
{
	const int size = 100;
	int* array = (int*) malloc(sizeof(int) * size);
	int i;
	for(i = 0; i < size; i++)
		array[i] = i;
	ListNode* head = reverse_linked_list(get_linked_list(array, size));
	ListNode* curr = head;
	for(i = size - 1; i >= 0; i--)
	{
		assert(array[i] == curr->val);
		curr = curr->next;
	}
	free(array);
	destroy_linked_list(head);
}

void test_cycle_detection()
{
	const int size = 100;
	ListNode* nodes[size];
	ListNode* head = (ListNode*) malloc(sizeof(ListNode));
	head->val = 0;
	head->next = NULL;
	ListNode *prev = head, *curr = NULL;
	nodes[0] = head;
	for(int i = 1; i < size; i++)
	{
		curr = (ListNode*)malloc(sizeof(ListNode));
		curr->val = i;
		curr->next = NULL;
		nodes[i] = curr;
		prev->next = curr;
		prev = curr;
	}
	if(rand() > RAND_MAX / 2)
	{
		int index = rand() % size;
		curr->next = nodes[index];
		assert(cycle_detection(head));
		assert(cycle_finding(head) == nodes[index]);
		curr->next = NULL;
	}
	else
	{
		assert(!cycle_detection(head));
		assert(cycle_finding(head) == NULL);
	}
	destroy_linked_list(head);
}

void insertion_sort(int* array, int n)
{
	int i, j, x;
	for(i = 0; i < n; i++)
	{
		j = i - 1;
		x = array[i];
		while(j >= 0 && array[j] > x)
		{
			array[j + 1] = array[j];
			j--;
		}
		array[j + 1] = x;
	}
}

void test_list_sort_impl(ListNode* (*sort)(ListNode*))
{
	const int size = 100;
	int* array = (int*) malloc(sizeof(int) * size);
	int i;
	for(i = 0; i < size; i++)
		array[i] = rand();
	ListNode* head = get_linked_list(array, size);
	head = sort(head);
	ListNode* curr = head;
	insertion_sort(array, size);
	for(i = 0; i < size; i++)
	{
		assert(array[i] == curr->val);
		curr = curr->next;
	}
	free(array);
	destroy_linked_list(head);
}

int main()
{
	srand(time(0));
	test_find_middle(100);
	test_find_middle(99);
	test_find_middle(1);
	test_reverse_linked_list();
	test_cycle_detection();
	test_list_sort_impl(list_merge_sort);
	return 0;
}
