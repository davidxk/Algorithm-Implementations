# Finds the kth largest element in the array by partially sorting the array
# At the end, all k smallest elements are placed at array[:k + 1]
# All elements greater than the kth largest element are placed at array[k + 1:]
# Time:  O(n)

def insertion_sort(array, left, right):
    for i in range(left + 1, right + 1):
        x = array[i]
        j = i - 1
        while j >= left and array[j] > x:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = x

def median3(array, left, right):
    center = (left + right) / 2
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
    elif center < rank:
        q_select(array, center + 1, right, rank)

def quick_select(array, rank):
    q_select(array, 0, len(array) - 1, rank - 1)
    return array[rank - 1]

# Binary search on an array can usually be implemented non-recursively
def q_select_loop(array, left, right, rank):
    while right - left > 10:
        center = partition(array, left, right)
        if center == rank:
            return
        elif center < rank:
            left = center + 1
        else:
            right = center - 1
    insertion_sort(array, left, right)
