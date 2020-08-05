#  1  0
#  l=>l
#  r
#
#  1  0
#     l
#  r<=r
#  Conclusion: 'left' always land at right of the boundary
#              'right' at left of the boundary
# Time:  O(log n)
# Space: O(1)

def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        center = (left + right) // 2
        if array[center] == target:
            return center
        elif array[center] < target:
            left = center + 1
        else:
            right = center - 1
    return -1

# isRight returns true when
# a) array[center] is not the target and
# b) target is in (center, right]
# isRight returns false when
# a) array[center] may be the target and
# b) target is in [left, center]
#
# Loop ends when
# a) right = center == left or
# b) left = center + 1 == right
# So it does not matter which one you return
def general_binary_search(array, isRight):
    left, right = 0, len(array) - 1
    while left < right:
        center = left + (right - left) // 2
        if isRight(array[center]):
            left = center + 1
        else:
            right = center
    # assert left == right
    # assert not isRight(left)
    return left

def lower(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        center = (left + right) // 2
        # When equal search in left
        if array[center] == target:
            right = center - 1
        elif array[center] < target:
            left = center + 1
        else:
            right = center - 1
    return right

def higher(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        center = (left + right) // 2
        # When equal search in right
        if array[center] == target:
            left = center + 1
        elif array[center] < target:
            left = center + 1
        else:
            right = center - 1
    return left

def equal_range(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        center = (left + right) // 2
        if array[center] < target:
            left = center + 1
        else:
            right = center - 1
    if left >= len(array) or array[left] != target:
        return (-1, -1)
    start = left
    left, right = left, len(array) - 1
    while left <= right:
        center = (left + right) // 2
        if array[center] <= target:
            left = center + 1
        else:
            right = center - 1
    end = right
    return (start, end)
