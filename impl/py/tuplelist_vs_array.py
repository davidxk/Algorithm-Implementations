from time import time

def get_tuple_list(array):
    tail = (array[-1], None)
    ptr = tail
    for i in range(len(array) - 2, -1, -1):
        ptr = (array[i], ptr)
    return ptr

def array_traverse(array):
    xor = 0
    for i in range(len(array)):
        xor ^= array[i]

def tuple_list_traverse(head):
    ptr = head
    xor = 0
    while ptr:
        xor ^= ptr[0]
        ptr = ptr[1]

def list_vs_array(scale = 20):
    volumn = 5000 * scale
    array = [i % 1000 for i in range(volumn)]
    timeM0 = time()
    head = get_tuple_list(array)
    timeM1 = time()
    print "malloc ", timeM1 - timeM0

    time0 = time()
    array_traverse(array)
    time1 = time()

    time2 = time()
    tuple_list_traverse(head)
    time3 = time()

    timeA, timeB = time1 - time0, time3 - time2
    print "array: ", timeA
    print "tuple: ", timeB
    print "%.2f" % (timeA / timeB)

list_vs_array(1000)
