from collections import deque
from random import randrange
from time import time

def push_pop(stack, times):
    for i in range(times):
        if randrange(2) & 1:
            stack.append(1)
        else:
            stack.pop()

def deque_vs_list(scale = 500):
    base = 1000
    times = base * scale

    list_stack = range(times)
    deque_stack = deque(range(times))

    time0 = time()
    push_pop(deque_stack, times)
    time1 = time()

    time2 = time()
    push_pop(list_stack, times)
    time3 = time()

    timeA, timeB = time1 - time0, time3 - time2
    print "deque: ", timeA
    print "list : ", timeB
    print "%.2f" % (timeA / timeB)
    return timeA, timeB

cnt = 0
for i in range(50):
    timeA, timeB = deque_vs_list(randrange(500))
    if timeA < timeB:
        cnt += 1
print "deque faster than list", cnt * 2, "% of times"
print "(deque should be slightly faster)"
