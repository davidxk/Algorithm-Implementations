import random

# 1 2 3 4 5 6 7
# ^ ^ ^ ^ ^ ^ ^
# ^ ^ ^ ^ ^ ^
# ^ ^ ^ ^ ^
# Every time decrease the range of swapping by 1 from the back
# Time:  O(n)
# Space: O(1)
def fisher_yates(array):
    for i in range(len(array) - 1, -1, -1):
        j = random.randrange(i + 1)
        array[i], array[j] = array[j], array[i]

# 1 2 3 4 5 6 7
# ^ ^ ^ ^ ^ ^ ^
#   ^ ^ ^ ^ ^ ^
#     ^ ^ ^ ^ ^
# ... or do so from the front. Makes no difference
def fisher_yates_front(array):
    for i in range(len(array)):
        j = random.randrange(i, len(array))
        array[i], array[j] = array[j], array[i]
