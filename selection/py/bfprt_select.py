# Time:  O(n) worst case

def insertion_sort(array, left, right):
    for i in range(left + 1, right + 1):
        x = array[i]
        j = i - 1
        while j >= left and array[j] > x:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = x

def median5(array, left, right):
    insertion_sort(array, left, right)
    return (left + right)/2

def median_of_medians(array, left, right):
    if right - left < 5:        # 5 - 1 < 5
        return median5(array, left, right)
    for i in range(left, right + 1, 5):
        subright = i + 4
        if subright > right:
            subright = right
        index = median5(array, i, subright)
        gid = left + (i - left) / 5
        array[index], array[gid] = array[gid], array[index]
    return m_select(array, left, left + (right - left + 1) / 5,
            (right - left) / 10 + 1)

def partition(array, left, right):
    index = median_of_medians(array, left, right)
    pivot = array[index]
    array[index], array[right] = array[right], array[index]
    i, j = left, right - 1
    while True:
        while array[i] < pivot:
            i += 1
        while left <= j and pivot < array[j]:
            j -= 1
        if i >= j:
            array[i], array[right] = array[right], array[i]
            return i
        array[i], array[j] = array[j], array[i]
        i += 1; j -= 1

def m_select(array, left, right, rank):
    if left == right:
        return left
    center = partition(array, left, right)
    pivot_rank = center - left + 1
    if rank == pivot_rank:
        return center
    elif rank < pivot_rank:
        return m_select(array, left, center - 1, rank)
    else: 
        return m_select(array, center + 1, right, rank - pivot_rank)

def bfprt_select(array, rank):
    return m_select(array, 0, len(array) - 1, rank)
