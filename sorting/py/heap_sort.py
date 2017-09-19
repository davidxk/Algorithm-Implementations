def perc_down(array, i, size):
    x = array[i]
    child = None
    while i*2+1 < size:
        child = i * 2 + 1

        if child != size - 1 and array[child] < array[child + 1]:
            child += 1

        if array[child] > x:
            array[i] = array[child]
            i = child
        else:
            break

    array[i] = x

def heap_sort(array):
    for i in range(len(array) / 2, -1, -1):
        perc_down(array, i, len(array))

    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        perc_down(array, 0, i)
