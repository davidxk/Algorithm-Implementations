#include "stddef.h"

typedef struct list_node
{
	int val;
	struct list_node* next;
} ListNode;

typedef struct linked_list
{
	ListNode *head, *tail;
} LinkedList;

typedef struct hashset
{
	LinkedList** table;
	int primes[26] = {
		53, 97, 193, 389, 769, 1543, 3079, 6151, 12289, 24593, 49157, 98317,
		196613, 393241, 786433, 1572869, 3145739, 6291469, 12582917, 25165843,
		50331653, 100663319, 201326611, 402653189, 805306457, 1610612741
	};
	int primeIdx = 0;
	int _size = 0;
} HashSet;
