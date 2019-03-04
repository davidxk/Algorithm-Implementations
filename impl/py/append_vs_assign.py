from time import time

if __name__ == '__main__':
    timeA, timeB = 0, 0
    size = 1000
    for i in xrange(9999):
        time0 = time()
        a = [None] * size
        for num in range(size):
            a[num] = num
        time1 = time()

        time2 = time()
        b = []
        for num in range(size):
            b.append(num)
        time3 = time()

        timeA += time1 - time0
        timeB += time3 - time2

    print "assign: ", timeA
    print "append: ", timeB
    print int(100 * timeA / timeB), "%"
