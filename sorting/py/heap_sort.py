# Time:  O(n log n)
# Space: O(1)

def perc_down(array, i, size):
    x = array[i]
    child = None
    while i*2+1 < size:
        child = i * 2 + 1
        # Heap sort uses a max heap
        if child + 1 < size and array[child + 1] > array[child]:
            child += 1
        # Larger elements goes up
        if array[child] > x:
            array[i] = array[child]
            i = child
        else:
            break

    array[i] = x

def heap_sort(array):
    # Heapify
    for i in range(len(array) / 2, -1, -1):
        perc_down(array, i, len(array))
    # Pop from the top and place at the back
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        perc_down(array, 0, i)
