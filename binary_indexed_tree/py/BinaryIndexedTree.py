class BinaryIndexedTree:
    def __init__(self, array):
        self.tree = [0] + array
        for i in range(len(self.tree)):
            j = i + (i & (-i))
            if j < len(self.tree):
                self.tree[j] += self.tree[i]

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
