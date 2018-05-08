def merge_sort(array):
    tmp = [None] * len(array)
    m_sort(array, 0, len(array), tmp)

def m_sort(array, left, right, tmp):
    if right - left > 1:
        center = (left + right) / 2
        m_sort(array, left, center, tmp)
        m_sort(array, center, right, tmp)
        merge(array, left, center, right, tmp)

def merge(array, left, center, right, tmp):
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
