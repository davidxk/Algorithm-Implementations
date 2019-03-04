from pyskip import SkipList
from HashSet import HashSet
import bisect
import random
import time
import matplotlib.pyplot as plt

class TestComplexity:
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
        duration = time2 - time1
        print "%s:\t%f" % (name, time2 - time1)
        return duration

def plot_complexity(scales, durations):
    plt.plot(scales, durations[0], "g", scales, durations[1], "b", scales, durations[2], "y", scales, durations[3], "r")
    plt.show()

if __name__ == "__main__":
    test = TestComplexity()
    scales = range(10000, 100000, 1000)
    durs = [[], [], [], []]
    for scale in scales:
        print "n = %d" % scale
        array = range(scale)
        ssett = {num for num in range(scale)}
        hashset = HashSet()
        skiplist = SkipList()
        for num in range(scale):
            skiplist.add(num)
            hashset.add(num)
        durs[0] += [test.compare(scale, ssett, "set")]
        durs[1] += [test.compareList(scale, array, "list")]
        durs[2] += [test.compare(scale, hashset, "hash")]
        durs[3] += [test.compare(scale, skiplist, "skip")]
        print
    plot_complexity(scales, durs)
