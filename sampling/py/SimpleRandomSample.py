import heapq
import random

# Intuition: randomly taking 3 balls out of the box at once is equivalent to
#            randomly taking 1 ball from the box without replacement 3 times
# Simple Random Sample algorithm for fixed length input
def selection_rejection(array, n, k):
    """ Fan et al., 1962 """
    sample = []
    for elem in array:
        if random.random() * n < k:
            sample.append(elem)
            k -= 1
        n -= 1
    return sample

# Simple Random Sample algorithm for stream input
def reservoir_sampling(iterator, k):
    """ Vitter, 1985 """
    sample = []
    for i in range(k):
        try:
            sample.append(next(iterator))
        except StopIteration:
            return sample

    n = k
    while True:
        n += 1
        try:
            elem = next(iterator)
            if random.random() * n < k:
                idx = random.randrange(k)
                sample[idx] = elem
        except StopIteration:
            break
    return sample
