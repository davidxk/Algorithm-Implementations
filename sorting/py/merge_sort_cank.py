def merge_sort(array):
    m_sort(array, 0, len(array))

def m_sort(array, left, right):
    if(right - left > 1):
        center = (left + right) / 2
        m_sort(array, left, center)
        m_sort(array, center, right)
        merge(array, left, center, right)

def merge(array, left, center, right):
    i, j = 0, 0
    leftLen = center - left
    rightLen = right - center
    copy = []
    while i < leftLen and j < rightLen:
        if array[left + i] < array[center + j]:
            copy.append( array[left + i] )
            i += 1
        else:
            copy.append( array[center + j] )
            j += 1

    while i < leftLen:
        copy.append( array[left + i] )
        i += 1

    while j < rightLen:
        copy.append( array[center + j] )
        j += 1

    for k in range(len(copy)):
        array[left + k] = copy[k]
