#include <stdlib.h>
#include <limits.h>

#define SKIPLIST_MAX_LEVEL 6

typedef struct skip_node
{
    int key;
    int value;
    struct skip_node **forward;
} SkipNode;

typedef struct skip_list
{
    int level;
    int size;
    SkipNode* header;

} SkipList;

SkipList* skiplist_init(SkipList* list)
{
    int i;
    SkipNode *header = (SkipNode*) malloc(sizeof(SkipNode));
    list->header = header;
    header->key = INT_MAX;
    header->forward = (SkipNode**) malloc(sizeof(SkipNode*)*(SKIPLIST_MAX_LEVEL+1));
    for (i = 0; i <= SKIPLIST_MAX_LEVEL; i++)
        header->forward[i] = list->header;

    list->level = 1;
    list->size = 0;

    return list;
}

SkipNode* skiplist_search(SkipList* list, int key)
{
    SkipNode* curr = list->header;
    int i;
    for(i = list->level; i >= 1; i--)
        while(curr->forward[i]->key < key)
            curr = curr->forward[i];
    if(curr->forward[1]->key == key)
        return curr->forward[1];
    return NULL;
}

int skiplist_insert(SkipList* list, int key, int value)
{
    SkipNode* update[SKIPLIST_MAX_LEVEL+1];
    SkipNode* curr = list->header;
    int i, level;
    for(i = list->level; i >= 1; i--)
	{
        while(curr->forward[i]->key < key)
            curr = curr->forward[i];
        update[i] = curr;
    }
    curr = curr->forward[1];

    if(key == curr->key)
	{
        curr->value = value;
        return 0;
    }
	else
	{
        level = rand_level();
        if(level > list->level)
		{
            for(i = list->level+1; i <= level; i++)
                update[i] = list->header;
            list->level = level;
        }

        curr = (SkipNode*) malloc(sizeof(SkipNode));
        curr->key = key;
        curr->value = value;
        curr->forward = (SkipNode **)malloc(sizeof(SkipNode*) * (level + 1));
        for(i = 1; i <= level; i++)
		{
            curr->forward[i] = update[i]->forward[i];
            update[i]->forward[i] = curr;
        }
    }
    return 0;
}
