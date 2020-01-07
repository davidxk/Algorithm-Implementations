def insertion_sort(array, left, right):
    for i in range(left + 1, right + 1):
        x = array[i]
        j = i - 1
        while j >= left and x < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = x

def median3(array, left, right):
    center = (left + right) // 2
    a, b, c = sorted([array[left], array[center], array[right]])
    array[left], array[center], array[right] = a, c, b
    return b

def partition(array, left, right):
    pivot = median3(array, left, right)
    i = left
    for j in range(left, right):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[right] = array[right], array[i]
    return i

def q_sort(array, left, right):
    if right - left > 10:
        center = partition(array, left, right)
        q_sort(array, left, center - 1)
        q_sort(array, center + 1, right)
    else:
        insertion_sort(array, left, right)

def quick_sort_lomuto(array):
    q_sort(array, 0, len(array) - 1)
