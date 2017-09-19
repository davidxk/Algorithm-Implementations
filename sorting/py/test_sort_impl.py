from copy import copy
from collections import Counter
from random import randrange
from time import time

def check_consistency(original, array):
    cnt = Counter()
    for elem in original:
        cnt[elem] += 1
    for elem in array:
        cnt[elem] -= 1
    return sum(cnt.values()) == 0

def check_monotonic(array):
    for i in range(1, len(array)):
        if array[i - 1] > array[i]:
            return False
    return True

def check_sort_impl(sort_algo):
    array = [randrange(5000) for i in range(5000)]
    original = copy(array)
    time0 = time()
    sort_algo(array)
    time1 = time()
    print sort_algo, time1 - time0
    return check_monotonic(array) and check_consistency(original, array)

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from quick_sort_hoare import quick_sort_hoare
from quick_sort_lomuto import quick_sort_lomuto
from heap_sort import heap_sort

if __name__ == '__main__':
    sort_algos = [quick_sort_hoare, quick_sort_lomuto, heap_sort, merge_sort, insertion_sort, selection_sort, bubble_sort]
    for func in sort_algos:
        if not check_sort_impl(func):
            print "WA: ", func
