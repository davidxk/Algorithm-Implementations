"""0, 0, 0, 1, 1, 1, 2, 2, 2"""
"""        ^                """
# Equivalent to ceiling()
# Insert 1 or 0.5 in above example
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
# Equivalent to upper_bound()
# Insert 1 or 1.5 in above example
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
