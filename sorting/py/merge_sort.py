def merge_sort(array):
    tmp = [None for i in range(len(array))]
    m_sort(array, tmp, 0, len(array))

def m_sort(array, tmp, left, right):
    if right - left > 1:
        center = (left + right) / 2
        m_sort(array, tmp, left, center)
        m_sort(array, tmp, center, right)
        merge(array, tmp, left, center, right)

def merge(array, tmp, left, center, right):
    i, j, k = left, center, 0
    while i < center and j < right:
        if array[i] < array[j]:
            tmp[k] = array[i]
            i += 1
        else:
            tmp[k] = array[j]
            j += 1
        k += 1

    while i < center:
        tmp[k] = array[i]
        i += 1
        k += 1

    while j < right:
        tmp[k] = array[j]
        j += 1
        k += 1
    
    for i in range(k):
        array[left + i] = tmp[i]
