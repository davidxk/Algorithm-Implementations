import random

def selection_rejection(array, n, k):
    """ Fan et al., 1962 """
    sample = []
    for elem in array:
        if random.random() * n < k:
            sample.append(elem)
            k -= 1
        n -= 1
    return sample

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
