import random

def fisher_yates(array):
    for i in range(len(array) - 1, -1, -1):
        j = random.randrange(i + 1)
        array[i], array[j] = array[j], array[i]

def fisher_yates_front(array):
    for i in range(len(array)):
        j = random.randrange(i, len(array))
        array[i], array[j] = array[j], array[i]
