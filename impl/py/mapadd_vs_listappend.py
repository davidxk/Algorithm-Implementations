from time import time

if __name__ == '__main__':
    timeA, timeB = 0, 0
    size = 9999
    for i in range(1000):
        time0 = time()
        b = []
        for i in range(size):
            b.append(i)
        time1 = time()

        time2 = time()
        a = set()
        for i in range(size):
            a.add(i)
        time3 = time()

        timeA += time1 - time0
        timeB += time3 - time2

    print "list append: ", timeA
    print "map add    : ", timeB
    print int(100 * timeA / timeB), "%"
