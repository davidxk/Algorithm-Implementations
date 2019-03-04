from SkipList import SkipList
import bisect
import random
import time
#import matplotlib.pyplot as plt

class tsetComplexity:
    def compareList(self, n, container, name):
        time1 = time.time()
        for i in range(1000):
            num = random.randrange(n)
            index = bisect.bisect(container, num)
            if index < len(container) and container[index] == num:
                container.remove(num)
            num = random.randrange(n + n / 2)
            index = bisect.bisect(container, num)
            if index < len(container) and container[index] != num:
                container.insert(index, num)
        time2 = time.time()
        duration = time2 - time1
        print "%s:\t%f" % (name, duration)
        return duration

    def compare(self, n, container, name):
        time1 = time.time()
        for i in range(1000):
            num = random.randrange(n)
            if num in container:
                container.remove(num)
            num = random.randrange(n + n / 2)
            container.add(num)
        time2 = time.time()
        print "%s:\t%f" % (name, time2 - time1)

def plot_complexity(scales, array, ssett, skip):
    pass

if __name__ == "__main__":
    tset = tsetComplexity()
    """
    for scale in [10000, 50000, 90000]:
        print "n = %d" % scale
        array = range(scale)
        ssett = {num for num in range(scale)}
        skiplist = SkipList()
        for num in range(scale):
            skiplist.add(num)
        tset.compare(scale, ssett, "set")
        tset.compare(scale, skiplist, "skip")
        tset.compareList(scale, array, "list")
        print
    """
    skiplist = SkipList()
    for num in range(10000):
        skiplist.add(num)
    tset.compare(10000, skiplist, "skip")
