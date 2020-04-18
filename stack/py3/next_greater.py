def next_greater(nums):
    stack = []
    greater = [float("inf")] * len(nums)
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            greater[stack.pop()] = nums[i]
        stack.append(i)
    return greater

def next_greater_reverse(nums):
    stack = []
    greater = [float("inf")] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            greater[i] = stack[-1]
        stack.append(nums[i])
    return greater

# Find next element greater than curr and the last element greater than or equal
# to curr for each element in the array
def next_gt_last_ge(nums):
    stack = []
    nGt = [float("inf")] * len(nums)
    lGe = [float("inf")] * len(nums)
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            left = stack.pop()
            nGt[left] = num
        if stack:
            lGe[i] = nums[stack[-1]]
        stack.append(i)
    return nGt, lGe
