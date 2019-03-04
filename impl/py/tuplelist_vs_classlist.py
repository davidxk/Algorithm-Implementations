from ListNode import getLinkedList
from time import time

def get_tuple_list(array):
    tail = (array[-1], None)
    ptr = tail
    for i in range(len(array) - 2, -1, -1):
        ptr = (array[i], ptr)
    return ptr

def get_list_list(array):
    tail = [array[-1], None]
    ptr = tail
    for i in range(len(array) - 2, -1, -1):
        ptr = [array[i], ptr]
    return ptr

def tuple_list_traverse(head):
    ptr = head
    xor = 0
    while ptr:
        xor ^= ptr[0]
        ptr = ptr[1]

def tuple_list_print(head):
    ptr = head
    while ptr:
        print ptr[0]
        ptr = ptr[1]

def test_same_list(headA, headB):
    while headA and headB:
        assert headA[0] == headB.val
        headA = headA[1]
        headB = headB.next

def tuplelist_vs_classlist():
	array = range(100)
	timeA, timeB, timeC = 0, 0, 0
	for i in range(10000):
		time0 = time()
		headA = get_tuple_list(array)
		time1 = time()
		headB = get_list_list(array)
		time2 = time()
		headC = getLinkedList(array)
		time3 = time()

		timeA += time1 - time0
		timeB += time2 - time1
		timeC += time3 - time2

	test_same_list(headA, headC)
	test_same_list(headB, headC)

	print "tuple list: ", timeA
	print "list  list: ", timeB
	print "class list: ", timeC
	print "A/C: %.2f" % (timeA / timeC)
	print "B/C: %.2f" % (timeB / timeC)

tuplelist_vs_classlist()
