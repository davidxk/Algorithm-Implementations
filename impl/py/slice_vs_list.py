from time import time

if __name__ == '__main__':
    timeA, timeB = 0, 0
    size = 15000
    original = [i for i in range(size)]
    for i in range(15000):
        time0 = time()
        b = list(original)
        time1 = time()

        time2 = time()
        a = original[:]
        time3 = time()

        timeA += time1 - time0
        timeB += time3 - time2

    print "slice: ", timeA
    print "list : ", timeB
    print int(100 * timeA / timeB), "%"
