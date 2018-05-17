# For node i, its parent is        i - (i & (-i))
# For node i, its right sibling is i + (i & (-i))
# For the right most child, its right sibling is the right sibling
#     of the first ancestor that is not a right-most child
# Each node stores sum array[i - (i & (-i)): i + 1]
# Each number array[i] appears in all right siblings of node i
# Sum array[0: i + 1] is the sum from node i to the root
# Sum array[: 13] = sum array[12] array[8: 12] array[:8]

class BinaryIndexedTree:
    def __init__(self, array):
        self.tree = [0] + array
        for i in range(len(self.tree)):
            sib = i + (i & (-i))
            if sib < len(self.tree):
                self.tree[sib] += self.tree[i]

    def getSum(self, i):
        i += 1
        summation = 0
        while i > 0:
            summation += self.tree[i]
            i -= i & (-i)
        return summation

    def update(self, i, delta):
        i += 1
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def getRange(self, i, j):
        return self.getSum(j) - self.getSum(i - 1)
