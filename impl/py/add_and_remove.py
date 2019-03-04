from time import time

if __name__ == '__main__':
    times = 50
    size = 100000
    mymap = set()
    for cnt in range(times):
        time0 = time()
        for i in range(size):
            mymap.add(i)
        for i in range(size):
            mymap.remove(i)
        time1 = time()

        timeA = time1 - time0
        print timeA
