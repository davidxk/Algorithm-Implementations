#include <cassert>
#include <cstdlib>
#include <ctime>
#include <vector>

#include "find_middle.h"
#include "reverse_linked_list.h"
#include "LinkedList.h"
#include "list_merge_sort.h"

void test_find_middle(int size)
{
	std::vector<int> array(size);
	for(int i = 0; i < size; i++)
		array[i] = i;
	ListNode* head = getLinkedList(array);
	ListNode* middle = find_middle(head);
	assert(middle->val == (size - 1) / 2);
	destroyLinkedList(head);
}

void test_reverse_linked_list()
{
	const int size = 100;
	std::vector<int> array(size);
	for(int i = 0; i < size; i++)
		array[i] = i;
	ListNode* head = reverse_linked_list(getLinkedList(array));
	ListNode* curr = head;
	for(int i = size - 1; i >= 0; i--)
	{
		assert(array[i] == curr->val);
		curr = curr->next;
	}
	destroyLinkedList(head);
}

void test_list_sort_impl(ListNode* (*sort)(ListNode*))
{
	const int size = 100;
	std::vector<int> array(size);
	for(int i = 0; i < size; i++)
		array[i] = rand();
	ListNode* head = getLinkedList(array);
	head = sort(head);
	ListNode* curr = head;
	std::sort(array.begin(), array.end());
	for(int i = 0; i < size; i++)
	{
		assert(array[i] == curr->val);
		curr = curr->next;
	}
	destroyLinkedList(head);
}

int main()
{
	srand(time(NULL));
	test_find_middle(100);
	test_find_middle(99);
	test_find_middle(1);
	test_reverse_linked_list();
	test_list_sort_impl(list_merge_sort);
	return 0;
}
