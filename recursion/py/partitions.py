from copy import deepcopy
def partitions(nums):
    """ Semba, 1984 """
    if len(nums) == 0:
        return []
    front = [[[nums[0]]]]
    for num in nums[1:]:
        nextLayer = []
        for partition in front:
            children = [deepcopy(partition) for _ in range(len(partition) + 1)]
            children[-1].append([])
            for i in range(len(partition) + 1):
                children[i][i].append(num)
            nextLayer += children
        front = nextLayer
    return front
