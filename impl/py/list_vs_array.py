# Array is always faster than linked list because of memory cache locality

from ListNode import getLinkedList
from time import time

def array_traverse(array):
    xor = 0
    for i in range(len(array)):
        xor ^= array[i]

def list_traverse(head):
    ptr = head
    xor = 0
    while ptr:
        xor ^= ptr.val
        ptr = ptr.next

def list_vs_array(scale = 20):
    volumn = 5000 * scale
    array = [i % 1000 for i in range(volumn)]
    timeM0 = time()
    head = getLinkedList(array)
    timeM1 = time()
    print "malloc ", timeM1 - timeM0

    time0 = time()
    array_traverse(array)
    time1 = time()

    time2 = time()
    list_traverse(head)
    time3 = time()

    timeA, timeB = time1 - time0, time3 - time2
    print "array: ", timeA
    print "list : ", timeB
    print "%.2f" % (timeA / timeB)

list_vs_array(1000)
