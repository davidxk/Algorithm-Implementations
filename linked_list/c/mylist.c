#include "mylist.h"
#include <stddef.h>
#include <stdbool.h>
#include <stdlib.h>

int  mylistSize(mylist* list)
{
	if( list == NULL )
		return -1;
	return list->count;
}

int  mylistEmpty(mylist* list)
{
	if( list == NULL )
		return -1;
	return list->head == list->tail;
}

/* .. O = O - $
 * .. O = O == O -- $ */
int  mylistPushBack(mylist* list, void* obj)
{
	if( list == NULL ) return false;

    /* Create new node */
	ListNode* node = (ListNode*) malloc(sizeof(ListNode));
	node->obj = obj;
    list->count++;

	list->tail->next = node;
	node->prev = list->tail;
	node->next = NULL;
	list->tail = node;

	return true;
}

/* O = O ..
 * ^
 * O == O = O ..
 * ^ */
int  mylistPushFront(mylist* list, void* obj)
{
	if( list == NULL ) return false;

    /* Create new node */
	ListNode* node = (ListNode*) malloc(sizeof(ListNode));
	node->obj = obj;
    list->count++;

	node->next = list->head->next;
	node->next->prev = node;
	list->head->next = node;
	node->prev = list->head;

	return true;
}

void mylistErase(mylist* list, ListNode* elem)
{
	if(elem == list->tail)
		list->tail = elem->prev;
	ListNode* nextNode = elem->next;
	ListNode* prevNode = elem->prev;
	if(nextNode != NULL)
		nextNode->prev = prevNode;
	prevNode->next = nextNode;
    free( elem );
    list->count--;
}

void mylistClear(mylist* list)
{
	ListNode* elem = mylistFront(list);
	while( elem != NULL )
	{
		ListNode* tmp = elem;
		elem = mylistNext(list, elem);
		free( tmp );
	}
    mylistInit(list);
}

int  mylistInsert(mylist* list, void* obj, ListNode* elem)
{
    if(elem == NULL)
        return mylistPushBack(list, obj);

	ListNode* nextNode = elem;
	ListNode* prevNode = elem->prev;

    /* Create new node */
	ListNode* node = (ListNode*) malloc(sizeof(ListNode));
	if( node == NULL ) return false;
	node->obj = obj;
	if( list == NULL ) return false;
    list->count++;

	prevNode->next = node;
	node->prev = prevNode;
	nextNode->prev = node;
	node->next = nextNode;

	return true;
}


ListNode *mylistFront(mylist* list)
{
	if( mylistEmpty(list) )
		return NULL;
	if( list == NULL )
		return NULL;
	return list->head->next;
}

ListNode *mylistBack(mylist* list)
{
	if( mylistEmpty(list) )
		return NULL;
	if( list == NULL )
		return NULL;
	return list->tail;
}

ListNode *mylistNext(mylist* list, ListNode* elem)
{
	if( elem == mylistBack(list) )
		return NULL;
	if( elem == NULL )
		return NULL;
	return elem->next;
}

ListNode *mylistPrev(mylist* list, ListNode* elem)
{
	if( elem == mylistFront(list) )
		return NULL;
	if( elem == NULL )
		return NULL;
	return elem->prev;
}


ListNode *mylistFind(mylist* list, void* obj)
{
	ListNode *elem = NULL;

	for(elem = mylistFront(list);
			elem != NULL;
			elem = mylistNext(list, elem))
		if( obj == elem->obj )
			return elem;
	return NULL;
}

int mylistInit(mylist* list)
{
	if(list == NULL) return false;

    list->count = 0;
    list->dummy.obj = NULL;
    list->dummy.next = NULL;
    list->dummy.prev = NULL;
	list->head = &list->dummy;
	list->tail = &list->dummy;
	return true;
}

void mylistDestroy(mylist* list)
{
	mylistClear(list);
}
