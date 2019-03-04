from time import time

if __name__ == '__main__':
    timeA, timeB = 0, 0
    size = 9999
    data = 1000
    for i in range(1000):
        time0 = time()
        a = [data] * size
        time1 = time()

        time2 = time()
        b = [data for i in range(size)]
        time3 = time()
        timeA += time1 - time0
        timeB += time3 - time2
    print "[0] * size              : ", timeA
    print "[0 for i in range(size)]: ", timeB
    print int(100 * timeA / timeB), "%"
