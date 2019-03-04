from copy import copy
from random import randrange
from time import time
from ListNode import getLinkedList

def list_array_pk(array_sort, list_sort, scale = 20):
    volume = 5000 * scale
    array = [randrange(volume) for i in range(volume)]
    head = getLinkedList(array)

    time0 = time()
    array_sort(array)
    time1 = time()
    list_sort(head)
    time2 = time()

    return time1 - time0, time2 - time1

from bubble_sort import bubble_sort
from bubble_sort_3ex import bubble_sort_3ex
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from quick_sort_weiss import quick_sort_weiss
from quick_sort_hpure import quick_sort_hpure
from quick_sort_hoare import quick_sort_hoare
from quick_sort_pure import quick_sort_pure
from quick_sort_lomuto import quick_sort_lomuto

from list_insert_sort import list_insert_sort
from list_merge_sort import list_merge_sort
from list_quick_sort import list_quick_sort
from list_quick_sort_ import list_quick_sort_

array_sort, list_sort = quick_sort_hpure, list_quick_sort

cnt_win, total = 0, 50
sum_t_a, sum_t_b = 0, 0
for i in range(total):
    timeA, timeB = list_array_pk(array_sort, list_sort, randrange(1, 80))
    sum_t_a += timeA
    sum_t_b += timeB
    if timeA < timeB:
        cnt_win += 1
    print "round", i
    print array_sort, timeA
    print list_sort, timeB

print
print array_sort, "wins", cnt_win, "/", total, "of time"
print "It's running time is", sum_t_a / sum_t_b, "of the other"


