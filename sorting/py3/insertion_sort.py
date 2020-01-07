# 2  3  5  7->9   9 
# x = 4    j  j+1 i
# For everyone before me, if you are taller, walk one step back
#                                            that is your index goes up by one
# For the first guy no taller than me, I will stand right behind you
# Time:  O(n^2)
# Space: O(1)

def insertion_sort(array):
    for i in range(len(array)):
        x = array[i]
        j = i - 1
        while j >= 0 and array[j] > x:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = x
