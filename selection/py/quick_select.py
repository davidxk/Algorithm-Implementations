def insertion_sort(array, left, right):
    for i in range(left + 1, right + 1):
        x = array[i]
        j = i - 1
        while j >= left and x < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = x

def median3(array, left, right):
    center = (left + right) / 2
    a, b, c = sorted([array[left], array[center], array[right]])
    array[left], array[center], array[right] = a, c, b
    return array[right]

def partition(array, left, right):
    pivot = median3(array, left, right)
    i, j = left + 1, right - 1
    while True:
        while array[i] < pivot:
            i += 1
        while pivot < array[j]:
            j -= 1
        if i >= j:
            array[i], array[right] = array[right], array[i]
            return i
        array[i], array[j] = array[j], array[i]
        i, j = i + 1, j - 1

def q_select(array, left, right, rank):
    if right - left < 10:
        insertion_sort(array, left, right)
        return
    center = partition(array, left, right)
    if rank < center:
        q_select(array, left, center - 1, rank)
    elif rank > center:
        q_select(array, center + 1, right, rank)

def quick_select(array, rank):
    q_select(array, 0, len(array) - 1, rank - 1)
    return array[rank - 1]
