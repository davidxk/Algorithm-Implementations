# Boyer–Moore majority vote algorithm: finds the majority element of a sequence
# Time:  O(n)
# Space: O(1) assume count(majority) > length / 2
# If majority less than half, sort and count within O(n log n) time O(1) space

# The majority numbers are united: they add to the count of their peers
# Other numbers tries to subtract majority numbers' count to zero
# Other numbers could fight amongst themselves, subtracting each other's count
# Even all other numbers get united to take on the big one, they are 1 short

def majority_vote(nums):
    candy, count = None, 0
    for num in nums:
        if count == 0:
            candy, count = num, 1
        elif num == candy:
            count += 1
        else:
            count -= 1
    return candy if nums.count(candy) > len(nums) / 2 else None

# If there are only 2 people present, then everyone accounts for more than 1/3
# Suppose there are k seats and numbers got voted could seat on one of the seats
# Once all k seats are seated, voting for a k+1th candidate
#    would bring down the vote for everyone sitting in the k seats
# To kick the majority out of chair, the rest gets united and keeps on 
#    voting for the k+1th number
# They would need k-1 times as many vote as the majority
# Sadly they don't have that many numbers. 

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
