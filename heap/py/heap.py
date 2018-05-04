# Heap is a binary tree where from root to every leaf is a sorted linked list
# - Percolate down is like a iteration in insertion sort
# - Heapify runs percolate down for all layers above the leaf, bottom up
# - Heappush inserts at bottom right and percolates up like bubble sort
# - Heappop pops off the root, replaces it with bottom right and percolates down
#
# For node i, its children are 2*i+1 and 2*i+2

def perc_down(array, i, size):
    x = array[i]
    child = None
    while i*2+1 < size:
        child = i * 2 + 1

        if child != size - 1 and array[child] > array[child + 1]:
            child += 1

        if array[child] < x:
            array[i] = array[child]
            i = child
        else:
            break

    array[i] = x

def heapify(array):
    for i in range(len(array) / 2, -1, -1):
        perc_down(array, i, len(array))

def heappush(array, elem):
    array.append(elem)
    i = len(array) - 1
    while i > 0:
        parent = (i - 1) / 2
        if array[i] < array[parent]:
            array[i], array[parent] = array[parent], array[i]
            i = parent
        else:
            break

def heappop(array):
    array[0], array[-1] = array[-1], array[0]
    perc_down(array, 0, len(array) - 1)
    return array.pop()
