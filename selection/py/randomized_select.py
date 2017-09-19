def median3(array, left, right):
    if right - left >= 2:
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

def r_select(array, left, right, rank):
    if left == right:
        return array[right]
    center = partition(array, left, right)
    pivot_rank = center - left + 1
    if rank == pivot_rank:
        return array[center]
    elif rank < pivot_rank:
        return r_select(array, left, center - 1, rank)
    else:
        return r_select(array, center + 1, right, rank - pivot_rank)

def randomized_select(array, rank):
    return r_select(array, 0, len(array) - 1, rank)
