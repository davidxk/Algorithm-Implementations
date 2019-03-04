# Hoare partition scheme, Mark Allen Weiss book
def insertion_sort(array, left, right):
    for i in range(left, right + 1):
        x = array[i]
        j = i - 1
        while j >= left and array[j] > x:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = x

def median3(array, left, right):
    center = (left + right) / 2
    a, b, c = array[left], array[center], array[right]
    array[left], array[center], array[right] = sorted([a, b, c])
    array[center], array[right] = array[right], array[center]
    return array[right]

def q_sort(array, left, right):
    if left + 10 <= right:
        pivot = median3(array, left, right)
        i, j = left + 1, right - 1
        while True:
            while array[i] < pivot:
                i += 1
            while pivot < array[j]:
                j -= 1

            if i >= j:
                break
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
        array[i], array[right] = array[right], array[i]
        q_sort(array, left, i - 1)
        q_sort(array, i + 1, right)
    else:
        insertion_sort(array, left, right)

def quick_sort_weiss(array):
    q_sort(array, 0, len(array) - 1)

'''
from random import randrange
while True:
    array = [randrange(20) for i in range(20)]
    print "Test: ", array
    quick_sort(array)
    print "Gets: ", array
'''
