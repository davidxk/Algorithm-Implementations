
// Implementation of a double linked list
typedef struct tagListNode {
    void *obj;
    struct tagListNode *next;
    struct tagListNode *prev;
} ListNode;

typedef struct tagMyList {
    int count;
    ListNode dummy;
	ListNode *head, *tail;

    void (*init)(struct tagMyList *);
    int  (*size)(struct tagMyList *);
    int  (*empty)(struct tagMyList *);

    int  (*push_back)(struct tagMyList *, void*);
    int  (*push_front)(struct tagMyList *, void*);
    void (*erase)(struct tagMyList *, ListNode*);
    void (*clear)(struct tagMyList *);
    int  (*insert)(struct tagMyList *, void*, ListNode*);

    ListNode *(*front)(struct tagMyList *);
    ListNode *(*back)(struct tagMyList *);
    ListNode *(*next)(struct tagMyList *, ListNode *);
    ListNode *(*prev)(struct tagMyList *, ListNode *);

    ListNode *(*find)(struct tagMyList *, void *);
} mylist;

extern int  mylistSize(mylist*);
extern int  mylistEmpty(mylist*);

extern int  mylistPushBack(mylist*, void*);
extern int  mylistPushFront(mylist*, void*);
extern void mylistErase(mylist*, ListNode*);
extern void mylistClear(mylist*);
extern int  mylistInsert(mylist*, void*, ListNode*);

extern ListNode *mylistFront(mylist*);
extern ListNode *mylistBack(mylist*);
extern ListNode *mylistNext(mylist*, ListNode*);
extern ListNode *mylistPrev(mylist*, ListNode*);

extern ListNode *mylistFind(mylist*, void*);

extern int mylistInit(mylist*);
extern void mylistDestroy(mylist*);
