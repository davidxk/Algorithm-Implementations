from copy import copy
from random import randrange
from time import time
from ListNode import getLinkedList

def sort_impl_pk(funcA, funcB, scale = 20):
    volume = 5000 * scale
    array = [randrange(volume) for i in range(volume)]
    head = getLinkedList(array)
    daeh = getLinkedList(array)

    time0 = time()
    funcA(head)
    time1 = time()
    funcB(daeh)
    time2 = time()

    return time1 - time0, time2 - time1

from list_insert_sort import list_insert_sort
from list_merge_sort import list_merge_sort
from list_quick_sort import list_quick_sort
from list_quick_sort_ import list_quick_sort_

funcA, funcB = list_quick_sort, list_merge_sort

cnt_win, total = 0, 50
sum_t_a, sum_t_b = 0, 0
for i in range(total):
    timeA, timeB = sort_impl_pk(funcA, funcB, randrange(1, 10))
    sum_t_a += timeA
    sum_t_b += timeB
    if timeA < timeB:
        cnt_win += 1
    print "round", i
    print funcA, timeA
    print funcB, timeB

print
print funcA, "wins", cnt_win, "/", total, "of time"
print "It's running time is", sum_t_a / sum_t_b, "of the other"
