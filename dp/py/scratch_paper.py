
def subset_sum_dfs(nums, K):
    nums.sort()
    mapping = {1 << i: nums[i] for i in range(len(nums))}
    target = K
    dest = (1 << len(nums)) - 1
    summ = {0: 0}
    front = [0]
    while front:
        subset = front.pop()
        temp = subset ^ dest
        while temp:
            mask = temp & (-temp)
            num = mapping[mask]
            child = subset | mask
            if child not in summ and num <= target - summ[subset]:
                if child == dest:
                    return True
                summ[child] = summ[subset] + num
                front.append(child)
            temp -= mask
    return False

