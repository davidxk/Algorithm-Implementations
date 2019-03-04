from time import time

if __name__ == '__main__':
    with open("words", 'r') as fd:
        words = fd.readlines()

    time0 = time()
    string = str().join(words)
    time1 = time()

    time2 = time()
    string = str()
    for word in words:
        string += word
    time3 = time()

    print "join: ", time1 - time0
    print "cat+: ", time3 - time2
    print int(100 * (time1 - time0) / (time3 - time2)), "%"
