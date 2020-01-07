# Dijkstra three way partition
# Time : O(n)
# Space: O(1)
#
# 0 0 0 1 1 0 2 0 1 2 2
#       ^   i     $    
# Invariant: array[:head] all 0, array[head: i] all 1, array[tail + 1:] all 2

def isHead(elem):
    return elem == 0

def isTail(elem):
    return elem == 2

def three_way_partition(array, is_head = isHead, is_tail = isTail):
    """ Dijkstra, 1976 """
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

# Compared to lumoto quick sort two way partition
# def three_way_partition(array):                 def two_way_partition(array):
#     head, tail = 0, len(array) - 1                  head = 0
#     i = 0                                           i = 0
#     while i <= tail:                                while i <= len(array) - 1:
#         if array[i] == 0:                               if array[i] == 0:
#             array[i], array[head] = array[head], array[i]   array[head], array[i] = array[i], array[head]
#             head += 1                                       head += 1
#             i += 1
#         elif array[i] == 2:
#             array[i], array[tail] = array[tail], array[i]
#             tail -= 1
#         else:
#             i += 1
