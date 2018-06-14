# Boyer-Moore majority vote algorithm: finds the majority element of a sequence
# Time:  O(n)
# Space: O(1) assume count(majority) > length / 2
# If majority less than half, sort and count within O(n log n) time O(1) space
# Or use sampling algorithms

# The majority numbers are united: they add to the count of their peers
# Other numbers tries to subtract majority numbers' count to zero
# Other numbers could fight amongst themselves, subtracting each other's count
# Even all other numbers get united to take on the big one, they are 1 short

def majority_vote(nums):
    """ Boyer & Moore, 1981 """
    candy, count = None, 0
    for num in nums:
        if count == 0:
            candy, count = num, 1
        elif num == candy:
            count += 1
        else:
            count -= 1
    return candy if nums.count(candy) > len(nums) / 2 else None

# Generally, find all elements that appear more than 1/k times
# Time:  O(kn)
# Space: O(k)
#
# O  O
# O  O  O  <= opponents
# -  -  -  <= k - 1 chairs
#    x     <= majority
#    x

# If there are only k-1 numbers, then everyone accounts for more than 1/k;
# Suppose there are k-1 chairs and each num got voted could seat on one of them
# Once all k chairs are occupied, voting for a k+1th candidate would
#    bring down the vote for everyone sitting in the chairs
# In the worst possible scenario, the majority nums are all placed at the back
# And exactly k-1 opponents are seated in the chairs with about n/k votes
# The majority will be able to bring at least one of them down since it accounts
#    for more than n/k of the numbers within the array

from collections import Counter
def majority_vote_general(nums, k):
    if len(nums) < k:
        return list(set(nums))
    count = Counter()
    for num in nums:
        if num in count or len(count) < k - 1:
            count[num] += 1
        else:
            for candy in count:
                if count[candy] == 0:
                    count.pop(candy)
                    count[num] = 1
                    break
            else:
                for candy in count:
                    count[candy] -= 1
    return filter(lambda candy: count[candy] and \
            nums.count(candy) > len(nums) / k, count)
