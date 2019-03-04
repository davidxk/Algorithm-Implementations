def shoppingOffers(prices, specials, needs):
    def helper(needs):
        tup = tuple(needs)
        if tup in cache:
            return cache[tup]
        for need in needs:
            if need > 0:
                break
        else:
            return 0
        minimum = float("inf")
        for offer in specials:
            newNeeds = list(needs)
            for i in range(len(offer) - 1):
                newNeeds[i] = needs[i] - offer[i]
                if newNeeds[i] < 0:
                    break
            else:
                minimum = min(offer[-1] + helper(newNeeds), minimum)
        for i in range(len(prices)):
            if needs[i] is not 0:
                needsI, needs[i] = needs[i], 0
                minimum = min(prices[i] * needsI + helper(needs), minimum)
                needs[i] = needsI
        cache[tup] = minimum
        return minimum
    cache = {}
    return helper(needs)

def combinationSum4(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def helper(target):
            if target in cache:
                return cache[target]
            elif target < 0:
                return 0
            elif target == 0:
                return 1
            result = 0
            for num in nums:
                result += helper(target - num)
            cache[target] = result
            return cache[target]
        cache = {}
        return helper(target)

def add_plus_minus(nums, S):
    def helper(start, target):
        if (start, target) in cache:
            return cache[(start, target)]
        elif start == len(nums):
            cache[(start, target)] = (target == 0)
            return cache[(start, target)]
        elif not -abs(sums[start]) <= target <= abs(sums[start]):
            return 0
        cache[(start, target)] = helper(start + 1, target - nums[start]) + \
                helper(start + 1, target + nums[start])
        return cache[(start, target)]
    cache = {}
    sums = list(nums)
    for i in range(len(nums)-2, -1, -1):
        sums[i] += sums[i + 1]
    return helper(0, S)
