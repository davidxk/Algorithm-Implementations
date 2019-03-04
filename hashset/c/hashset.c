#include <stdlib.h>
#include "hashset.h"


void list_append(LinkedList* list, int value)
{
	ListNode* node = (ListNode*) malloc(sizeof(ListNode));
	node->val = value;
	node->next = NULL;
	list->tail->next = node;
}

ListNode* list_find(LinkedList* list, int value)
{
	ListNode* curr = list->head;
	while(curr)
	{
		if(curr->val == value)
			return curr;
		curr = curr->next;
	}
	return NULL;
}

int hashset_myhash(HashSet* hashset, const int value)
{
	int hashVal = value;
	int tableSize = hashset->primes[hashset->primeIdx];
	hashVal %= tableSize;
	if(hashVal < tableSize)
		hashVal += tableSize;
	return hashVal;
}

void hashset_insert(HashSet* hashset, int value)
{
	LinkedList* list = hashset->table[hashset_myhash(hashset, value)];
	if(list_find(list, value))
		return;
	list_append(list, value);
	int tableSize = hashset->primes[hashset->primeIdx];
	if(hashset->_size > tableSize)
		hashset_rehash(hashset);
}

void hashset_erase(HashSet* hashset, int value)
{

}

void hashset_rehash(HashSet* hashset)
{

}
