from copy import copy
from random import randrange
from time import time

def sort_impl_pk(funcA, funcB, scale = 20):
    volume = 5000 * scale
    array = [randrange(volume) for i in range(volume)]
    yarra = copy(array)

    time0 = time()
    funcA(array)
    time1 = time()
    funcB(yarra)
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

funcA, funcB = quick_sort_hoare, quick_sort_weiss

cnt_win, total = 0, 50
sum_t_a, sum_t_b = 0, 0
for i in range(total):
    timeA, timeB = sort_impl_pk(funcA, funcB, randrange(80))
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
