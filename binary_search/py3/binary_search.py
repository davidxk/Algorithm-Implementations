# In the first setup, we look for a target value in an array.
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

# In the second setup, we look for target value for variable x in domain
# [lo, hi], with the knowledge of some direction function f which tells us
# to move left or right on the interval.
#
# Time:  O(log(hi-lo)) ≈ O(1)
# Space: O(1)
#
#                    f->
# <---------[lo--------------------hi]-------------------->
#                   target?
#
# Three key elements to look for in a binary search problem
# - variable x
# - domain [lo, hi]
# - direction function f
#
#
# target_is_gt returns true when target is in interval (mid, hi]
# a) target does not equal mid AND
# b) target is greater than mid
# target_is_gt returns false when target is in interval [lo, mid]
# a) target may equal mid OR
# b) target may be less than mid
#
# Loop ends when
# a) hi = mid == lo OR
# b) lo = mid + 1 == hi
# So it does not matter if you return lo or you return hi
# 
# Loop will end because
# a) when lo = n and hi = n + 1
#         mid = lo + (hi - lo) // 2 == n == lo
# b) EITHER lo = mid + 1 == n + 1 == hi OR hi = mid == n == lo
def general_binary_search(lower, upper, target_is_gt):
    lo, hi = lower, upper
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if target_is_gt(mid):
            lo = mid + 1
        else:
            hi = mid
    # assert lo == hi
    # assert not target_is_gt(lo)
    return lo

# target_is_ge returns true when target is in interval [mid, hi]
# a) target may equal mid OR
# b) target may be greather than mid
# target_is_ge returns false when target is in interval [lo, mid)
# a) target does not equal mid AND
# b) target is less than mid
#
# Loop ends when
# a) hi = mid == lo or
# b) hi = mid - 1 == lo
# So it does not matter which one of lo and hi you return
# 
# Loop will end because
# a) when lo = n and hi = n + 1
#         mid = lo + (hi - lo + 1) // 2 == n + 1 == hi
# b) EITHER lo = mid == n + 1 == hi OR hi = mid - 1 == n == lo
def general_binary_search2(lower, upper, target_is_ge):
    lo, hi = lower, upper
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2
        if target_is_ge(mid):
            lo = mid
        else:
            hi = mid - 1
    # assert lo == hi
    return lo

# Sometimes it is possible to know if a value is the target
def general_binary_search3(lower, upper, target_is_gt, target_is_lt):
    lo, hi = lower, upper
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if target_is_gt(mid):
            lo = mid + 1
        elif target_is_lt(mid):
            hi = mid - 1
        else:
            return mid
    # assert lo == hi
    # assert not target_is_gt(lo)
    return -1

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
