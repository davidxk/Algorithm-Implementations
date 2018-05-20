# Time:  O(n log n)
# Space: O(n)

def merge_sort(array):
    temp = [None] * len(array)
    m_sort(array, 0, len(array), temp)

def m_sort(array, start, stop, temp):
    if stop - start > 1:
        middle = (start + stop) / 2
        m_sort(array, start, middle, temp)
        m_sort(array, middle, stop, temp)
        merge(array, start, middle, stop, temp)

def merge(array, start, middle, stop, temp):
    i, j, k = start, middle, 0
    while i < middle and j < stop:
        if array[i] < array[j]:
            temp[k] = array[i]
            i += 1
        else:
            temp[k] = array[j]
            j += 1
        k += 1

    while i < middle:
        temp[k] = array[i]
        i += 1
        k += 1

    while j < stop:
        temp[k] = array[j]
        j += 1
        k += 1

    for i in range(k):
        array[start + i] = temp[i]

"""
# In 'left-right-pointer' convention
def merge_sort(array):
    temp = [None] * len(array)
    m_sort(array, 0, len(array) - 1, temp)

def m_sort(array, left, right, temp):
    if left < right:
        center = (left + right) / 2
        m_sort(array, left, center, temp)
        m_sort(array, center + 1, right, temp)
        merge(array, left, center, right, temp)

def merge(array, left, center, right, temp):
    i, j, k = left, center + 1, 0
    while i <= center and j <= right:
        if array[i] < array[j]:
            temp[k] = array[i]
            i += 1
        else:
            temp[k] = array[j]
            j += 1
        k += 1

    while i <= center:
        temp[k] = array[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = array[j]
        j += 1
        k += 1
    
    for i in range(k):
        array[left + i] = temp[i]
"""
