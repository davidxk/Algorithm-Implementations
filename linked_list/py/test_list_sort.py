from copy import copy
from collections import Counter
from random import randrange
from time import time
from ListNode import getLinkedList
from ListNode import getArray

def check_consistency(array, head):
    cnt = Counter()
    for elem in array:
        cnt[elem] += 1
    ptr = head
    while ptr:
        cnt[ptr.val] -= 1
        ptr = ptr.next
    return sum(cnt.values()) == 0

def check_monotonic(head):
    cnt = 0
    ptr = head
    while ptr.next:
        if ptr.val > ptr.next.val or cnt > 50000:
            return False
        ptr = ptr.next
    return True

def test_list_sort(sort_algo):
    array = [randrange(5000) for i in range(5000)]
    head = getLinkedList(array)

    time0 = time()
    head = sort_algo(head)
    time1 = time()
    print sort_algo, time1 - time0

    array = getArray(head)
    return check_monotonic(head) and check_consistency(array, head)

from list_insert_sort import list_insert_sort
from list_merge_sort import list_merge_sort
from list_quick_sort import list_quick_sort
from list_quick_sort_ import list_quick_sort_

sort_algos = [list_insert_sort, list_merge_sort, list_quick_sort, list_quick_sort_]
for func in sort_algos:
    if not test_list_sort(func):
        print "WA: ", func
