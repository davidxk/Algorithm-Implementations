from math import log

class RMQSegmentTree:
    def __init__(self, array):
        self.n = len(array)
        x = int(log(len(array), 2)) + 1
        size = 2 ** x * 2
        self.tree = [0] * size
        self.build(0, array, 0, self.n - 1)

    def build(self, i, array, left, right):
        if left >= right:
            self.tree[i] = array[left]
        else:
            center = (left + right) / 2
            self.build(2 * i + 1, array, left, center)
            self.build(2 * i + 2, array, center + 1, right)
            self.tree[i] = min(self.tree[2 * i + 1], self.tree[2 * i + 2])

    def query(self, qLeft, qRight):
        return self.queryUtil(0, qLeft, qRight, 0, self.n - 1)

    def queryUtil(self, i, qLeft, qRight, left, right):
        if qLeft <= left and right <= qRight:
            return self.tree[i]

        if qRight < left or right < qLeft:
            return float("inf")

        center = (left + right) / 2
        return min(self.queryUtil(2 * i + 1, qLeft, qRight, left, center), \
                self.queryUtil(2 * i + 2, qLeft, qRight, center + 1, right))

    def update(self, index, delta):
        left, right = 0, self.n - 1
        i = 0
        while left < right:
            center = (left + right) / 2
            if index <= center:
                i = i * 2 + 1
                right = center
            else:
                i = i * 2 + 2
                left = center + 1
        self.tree[i] += delta
        while i > 0:
            i = (i - 1) / 2
            self.tree[i] = min(self.tree[i * 2 + 1], self.tree[i * 2 + 2])

    def updateRecursive(self, index, delta):
        self.updateRecursiveUtil(index, delta, 0, 0, self.n - 1)

    def updateRecursiveUtil(self, index, delta, i, left, right):
        if left >= right:
            self.tree[i] += delta
            return
        center = (left + right) / 2
        if index <= center:
            self.updateRecursiveUtil(index, delta, 2 * i + 1, left, center)
        else:
            self.updateRecursiveUtil(index, delta, 2 * i + 2, center + 1, right)
        self.tree[i] = min(self.tree[2 * i + 1], self.tree[2 * i + 2])

class SumSegmentTree:
    def __init__(self, array):
        self.n = len(array)
        x = int(log(len(array), 2)) + 1
        size = 2 ** x * 2
        self.tree = [0] * size
        self.build(0, array, 0, self.n - 1)

    def build(self, i, array, left, right):
        if left >= right:
            self.tree[i] = array[left]
        else:
            center = (left + right) / 2
            self.build(2 * i + 1, array, left, center)
            self.build(2 * i + 2, array, center + 1, right)
            self.tree[i] = self.tree[2 * i + 1] + self.tree[2 * i + 2]

    def query(self, qLeft, qRight):
        return self.queryUtil(0, qLeft, qRight, 0, self.n - 1)

    def queryUtil(self, i, qLeft, qRight, left, right):
        if qLeft <= left and right <= qRight:
            return self.tree[i]

        if qRight < left or right < qLeft:
            return 0

        center = (left + right) / 2
        return self.queryUtil(2 * i + 1, qLeft, qRight, left, center) + \
                self.queryUtil(2 * i + 2, qLeft, qRight, center + 1, right)

    def update(self, index, delta):
        left, right = 0, self.n - 1
        i = 0
        while left < right:
            center = (left + right) / 2
            if index <= center:
                i = i * 2 + 1
                right = center
            else:
                i = i * 2 + 2
                left = center + 1
        while i >= 0:
            self.tree[i] += delta
            i = (i - 1) / 2
