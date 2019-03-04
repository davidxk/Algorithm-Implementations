from time import time

if __name__ == '__main__':
    timeA, timeB = 0, 0
    size = 1000
    data = 1000
    for i in range(9999):
        time0 = time()
        a = [data for i in xrange(size)]
        time1 = time()

        time2 = time()
        b = []
        for i in xrange(size):
            b.append(data)
        time3 = time()

        timeA += time1 - time0
        timeB += time3 - time2

    print "init  : ", timeA
    print "append: ", timeB
    print int(100 * timeA / timeB), "%"

