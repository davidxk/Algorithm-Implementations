def isHead(elem):
    return elem == 0

def isTail(elem):
    return elem == 2

def three_way_partition(array, is_head = isHead, is_tail = isTail):
    head, tail = 0, len(array) - 1
    i = 0
    while i <= tail:
        if is_head(array[i]):
            array[i], array[head] = array[head], array[i]
            head += 1
            i += 1
        elif is_tail(array[i]):
            array[i], array[tail] = array[tail], array[i]
            tail -= 1
        else:
            i += 1

