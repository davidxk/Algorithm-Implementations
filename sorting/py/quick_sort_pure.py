def median3(array, left, right):
    if right - left < 2:
        return array[right]
    center = (left + right) / 2
    a, b, c = sorted([array[left], array[center], array[right]])
    array[left], array[center], array[right] = a, c, b
    return array[right]

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
    if left < right:
        center = partition(array, left, right)
        q_sort(array, left, center - 1)
        q_sort(array, center + 1, right)

def quick_sort_pure(array):
    q_sort(array, 0, len(array) - 1)
