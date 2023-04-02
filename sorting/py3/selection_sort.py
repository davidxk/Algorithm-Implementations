# Time:  O(n^2)
# Space: O(1)

def selection_sort(array):
    for i in range(len(array)):
        minIdx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minIdx]:
                minIdx = j
        array[i], array[minIdx] = array[minIdx], array[i]
