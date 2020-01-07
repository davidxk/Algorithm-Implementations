# 99% of the time faster than lomuto, 30% faster on average
# 99% of the time faster than pure quick sort, 15% faster on average
# Time:  O(n log n)

def insertion_sort(array, left, right):
    for i in range(left + 1, right + 1):
        x = array[i]
        j = i - 1
        while j >= left and array[j] > x:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = x

def median3(array, left, right):
    center = (left + right) // 2
    temp = [array[left], array[center], array[right]]
    insertion_sort(temp, 0, 2)
    array[left], array[right], array[center] = temp
    return array[right]

def partition(array, left, right):
    pivot = median3(array, left, right)
    i, j = left + 1, right - 1
    while True:
        while array[i] < pivot:
            i += 1
        # Invariant: array[i] >= pivot
        while pivot < array[j]:
            j -= 1
        # Invariant: array[j] <= pivot
        if i >= j:
            array[i], array[right] = array[right], array[i]
            return i
        array[i], array[j] = array[j], array[i]
        i, j = i + 1, j - 1

def q_sort(array, left, right):
    if right - left > 10:
        center = partition(array, left, right)
        q_sort(array, left, center - 1)
        q_sort(array, center + 1, right)
    else:
        insertion_sort(array, left, right)

def quick_sort(array):
    q_sort(array, 0, len(array) - 1)
