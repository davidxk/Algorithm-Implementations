from math import log

# Segment Tree is a complete binary tree
# Tree size is 2 * power-of-2-ceiling of the array size
# Array elements are leaf nodes in the bottom layer of the tree

class RMQSegmentTree:
    def __init__(self, array):
        #if len(array) < 2:
            #raise IndexError("Cannot build segment tree for len(array) < 2")
        self.n = len(array)
        x = int(log(self.n - 1, 2)) + 1
        size = 2 ** x * 2
        self.tree = [0] * size
        self.build(0, array, 0, self.n - 1)

    def build(self, i, array, left, right):
        if left >= right:
            self.tree[i] = array[left]
        else:
            center = (left + right) // 2
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

        center = (left + right) // 2
        return min(self.queryUtil(2 * i + 1, qLeft, qRight, left, center), \
                self.queryUtil(2 * i + 2, qLeft, qRight, center + 1, right))

    def update(self, index, delta):
        left, right = 0, self.n - 1
        i = 0
        while left < right:
            center = (left + right) // 2
            if index <= center:
                i = i * 2 + 1
                right = center
            else:
                i = i * 2 + 2
                left = center + 1
        self.tree[i] += delta
        while i > 0:
            i = (i - 1) // 2
            self.tree[i] = min(self.tree[i * 2 + 1], self.tree[i * 2 + 2])

    def recursiveUpdate(self, index, delta):
        self.recursiveUpdateUtil(index, delta, 0, 0, self.n - 1)

    def recursiveUpdateUtil(self, index, delta, i, left, right):
        if left >= right:
            self.tree[i] += delta
            return
        center = (left + right) // 2
        if index <= center:
            self.recursiveUpdateUtil(index, delta, 2 * i + 1, left, center)
        else:
            self.recursiveUpdateUtil(index, delta, 2 * i + 2, center + 1, right)
        self.tree[i] = min(self.tree[2 * i + 1], self.tree[2 * i + 2])

# Example of a segment tree with range update using lazy propagation
class RSQSegmentTree:
    def __init__(self, array):
        self.n = len(array)
        x = int(log(self.n - 1, 2)) + 1
        size = 2 ** x * 2
        self.tree = [0] * size
        self.lazy = [0] * size
        self.build(0, array, 0, self.n - 1)

    def build(self, i, array, left, right):
        if left >= right:
            self.tree[i] = array[left]
        else:
            center = (left + right) // 2
            self.build(2 * i + 1, array, left, center)
            self.build(2 * i + 2, array, center + 1, right)
            self.tree[i] = self.tree[2 * i + 1] + self.tree[2 * i + 2]

    def lazyPropagate(self, i, left, right):
        if self.lazy[i] != 0:
            self.tree[i] += (right - left + 1) * self.lazy[i]
            if left < right:
                self.lazy[2 * i + 1] += self.lazy[i]
                self.lazy[2 * i + 2] += self.lazy[i]
            self.lazy[i] = 0

    def query(self, qLeft, qRight):
        return self.queryUtil(0, qLeft, qRight, 0, self.n - 1)

    def queryUtil(self, i, qLeft, qRight, left, right):
        self.lazyPropagate(i, left, right)

        if qLeft <= left and right <= qRight:
            return self.tree[i]

        if qRight < left or right < qLeft:
            return 0

        center = (left + right) // 2
        return self.queryUtil(2 * i + 1, qLeft, qRight, left, center) + \
                self.queryUtil(2 * i + 2, qLeft, qRight, center + 1, right)

    def update(self, index, delta):
        left, right = 0, self.n - 1
        i = 0
        while left < right:
            center = (left + right) // 2
            if index <= center:
                i = i * 2 + 1
                right = center
            else:
                i = i * 2 + 2
                left = center + 1
        while i >= 0:
            self.tree[i] += delta
            i = (i - 1) // 2

    def rangeUpdate(self, qLeft, qRight, delta):
        self.rangeUpdateUtil(qLeft, qRight, delta, 0, 0, self.n - 1)

    def rangeUpdateUtil(self, qLeft, qRight, delta, i, left, right):
        self.lazyPropagate(i, left, right)

        if qLeft <= left and right <= qRight:
            self.lazy[i] += delta
            self.lazyPropagate(i, left, right)
            return

        if qRight < left or right < qLeft:
            return

        center = (left + right) // 2
        self.rangeUpdateUtil(qLeft, qRight, delta, 2 * i + 1, left, center)
        self.rangeUpdateUtil(qLeft, qRight, delta, 2 * i + 2, center + 1, right)
        self.tree[i] = self.tree[2 * i + 1] + self.tree[2 * i + 2]

"""
# In 'start-middle-stop' convention
# General merge function has to be able to handle 'None' properly
# Verified
class SegmentTree:
    def __init__(self, array=[], merge=min, length=None):
        self.merge = merge
        self.n = len(array) or length
        x = int(log(self.n - 1, 2)) + 1
        size = 2 ** x * 2
        self.tree = [0] * size
        self.lazy = [0] * size
        if array:
            self.build(array, 0, 0, self.n)

    def build(self, array, i, start, stop):
        if stop - start <= 1:
            self.tree[i] = array[start]
        else:
            middle = (start + stop) // 2
            self.build(array, 2 * i + 1, start, middle)
            self.build(array, 2 * i + 2, middle, stop)
            self.tree[i] = self.merge(self.tree[2 * i + 1], self.tree[2 * i + 2])

    def lazyPropagate(self, i, start, stop):
        if self.lazy[i] != 0:
            # self.tree[i] += self.lazy[i] # For RMQ
            self.tree[i] += (stop - start) * self.lazy[i]
            if stop - start > 1:
                self.lazy[2 * i + 1] += self.lazy[i]
                self.lazy[2 * i + 2] += self.lazy[i]
            self.lazy[i] = 0

    def query(self, qStart, qStop):
        return self.queryUtil(0, qStart, qStop, 0, self.n)

    def queryUtil(self, i, qStart, qStop, start, stop):
        self.lazyPropagate(i, start, stop)

        if qStart <= start and stop <= qStop:
            return self.tree[i]

        if qStop <= start or stop <= qStart:
            return None

        middle = (start + stop) // 2
        return self.merge(self.queryUtil(2 * i + 1, qStart, qStop, start, middle),
                self.queryUtil(2 * i + 2, qStart, qStop, middle, stop))

    def update(self, index, delta):
        self.recursiveUpdate(index, delta)

    def recursiveUpdate(self, index, delta):
        self.recursiveUpdateUtil(index, delta, 0, 0, self.n)

    def recursiveUpdateUtil(self, index, delta, i, start, stop):
        if stop - start <= 1:
            self.tree[i] += delta
            return
        middle = (start + stop) // 2
        if index < middle:
            self.recursiveUpdateUtil(index, delta, 2 * i + 1, start, middle)
        else:
            self.recursiveUpdateUtil(index, delta, 2 * i + 2, middle, stop)
        self.tree[i] = self.merge(self.tree[2 * i + 1], self.tree[2 * i + 2])

    def rangeUpdate(self, qStart, qStop, delta):
        # May need to update by setting range to a value instead of adding delta
        # Replace all "+=" with "=" and "delta" with "value"
        self.rangeUpdateUtil(qStart, qStop, delta, 0, 0, self.n)

    def rangeUpdateUtil(self, qStart, qStop, delta, i, start, stop):
        self.lazyPropagate(i, start, stop)

        if qStart <= start and stop <= qStop:
            self.lazy[i] += delta
            self.lazyPropagate(i, start, stop)
            return

        if qStop <= start or stop <= qStart:
            return

        middle = (start + stop) // 2
        self.rangeUpdateUtil(qStart, qStop, delta, 2 * i + 1, start, middle)
        self.rangeUpdateUtil(qStart, qStop, delta, 2 * i + 2, middle, stop)
        self.tree[i] = self.merge(self.tree[2 * i + 1], self.tree[2 * i + 2])
"""
