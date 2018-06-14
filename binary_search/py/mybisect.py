"""0, 0, 0, 1, 1, 1, 2, 2, 2"""
"""        ^                """
# Equivalent to ceiling(array, target), target <= ceiling
# Insert 1 or 0.5 in above example
# Thus, lower = ceiling - 1
def bisect_left(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        center = (left + right) / 2
        if array[center] == target:
            right = center - 1
        elif array[center] < target:
            left = center + 1
        else:
            right = center - 1
    return left

"""0, 0, 0, 1, 1, 1, 2, 2, 2"""
"""                 $       """
# Equivalent to higher(array, target), target < higher
# Insert 1 or 1.5 in above example
# Thus, floor = higher - 1
def bisect(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        center = (left + right) / 2
        if array[center] == target:
            left = center + 1
        elif array[center] < target:
            left = center + 1
        else:
            right = center - 1
    return left
