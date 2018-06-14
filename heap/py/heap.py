# Heap is a binary tree where from root to every leaf is a sorted linked list
# - Percolate down is like a iteration in insertion sort
# - Heapify runs insertion sort for all root-leaf path
# - Heappush inserts at bottom right and percolates up like bubble sort
# - Heappop pops off the root, replaces it with bottom right and percolates down
# - Heappushpop returns the min between the new and the top, perc_down if needed
#
# For node i, its children are 2*i+1 and 2*i+2

# For everyone behind me, if you are shorter than me, step up
def perc_down(array, i, size):
    x = array[i]
    child = None
    while i*2+1 < size:
        child = i * 2 + 1
        # Choose which path to go down
        if child + 1 < size and array[child + 1] < array[child]:
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

def heappushpop(array, elem):
    if array[0] < elem:
        array[0], elem = elem, array[0]
        perc_down(array, 0, len(array))
    return elem

# A binary tree problem can always be solved recursively
def perc_down_recursive(array, i, size):
    child = 2 * i + 1
    if not child < size:
        return
    if child + 1 < size and array[child + 1] < array[child]:
        child += 1
    if array[i] > array[child]:
        array[i], array[child] = array[child], array[i]
        perc_down_recursive(array, child, size)
