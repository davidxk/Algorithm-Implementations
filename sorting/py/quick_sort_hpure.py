def median3(array, left, right):
    if right - left < 2:
        return array[right]
    center = (left + right) / 2
    a, b, c = sorted([array[left], array[center], array[right]])
    array[left], array[center], array[right] = a, c, b
    return array[right]

def partition(array, left, right):
    pivot = median3(array, left, right)
    i, j = left, right - 1
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


def q_sort(array, left, right):
    if right > left:
        center = partition(array, left, right)
        q_sort(array, left, center - 1)
        q_sort(array, center + 1, right)

def quick_sort_hpure(array):
    q_sort(array, 0, len(array) - 1)
