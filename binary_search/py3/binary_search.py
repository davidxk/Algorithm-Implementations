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

# target_is_gt returns true when target is in interval (center, right]
# a) target does not equal center AND
# b) target is greater than center
# target_is_gt returns false when target is in interval [left, center]
# a) target may equal center OR
# b) target may be less than center
#
# Loop ends when
# a) right = center == left OR
# b) left = center + 1 == right
# So it does not matter if you return left or you return right
# 
# Loop will end because
# a) when left = n and right = n + 1
#         center = left + (right - left) // 2 == n == left
# b) EITHER left = center + 1 == n + 1 == right OR right = center == n == left
def general_binary_search(lower, upper, target_is_gt):
    left, right = lower, upper
    while left < right:
        center = left + (right - left) // 2
        if target_is_gt(center):
            left = center + 1
        else:
            right = center
    # assert left == right
    # assert not target_is_gt(left)
    return left

# target_is_ge returns true when target is in interval [center, right]
# a) target may equal center OR
# b) target may be greather than center
# target_is_ge returns false when target is in interval [left, center)
# a) target does not equal center AND
# b) target is less than center
#
# Loop ends when
# a) right = center == left or
# b) right = center - 1 == left
# So it does not matter which one of left and right you return
# 
# Loop will end because
# a) when left = n and right = n + 1
#         center = left + (right - left + 1) // 2 == n + 1 == right
# b) EITHER left = center == n + 1 == right OR right = center - 1 == n == left
def general_binary_search2(lower, upper, target_is_ge):
    left, right = lower, upper
    while left < right:
        center = left + (right - left + 1) // 2
        if target_is_ge(center):
            left = center
        else:
            right = center - 1
    # assert left == right
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
