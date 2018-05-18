from sys import stdout
from random import randrange, choice, shuffle

times = 100

def test_equal_range(equal_range, scale = 100):
    size = int(5000 * scale)
    array = [randrange(size) for i in range(size)]
    array.sort()
    for i in range(times):
        stdout.write("\rLoop " + str(i+1) + "/100")
        stdout.flush()
        target = randrange(int(size * 1.10))
        retval = equal_range(array, target) 
        if target not in array:
            if retval != (-1, -1):
                return False
            else:
                continue
        left = lower(array, target) + 1
        right = higher(array, target) - 1
        if retval != (left, right):
            return False
    return True

def test_higher(higher, scale = 100):
    size = int(5000 * scale)
    array = [randrange(size) for i in range(size)]
    array.sort()
    for i in range(times):
        stdout.write("\rLoop " + str(i+1) + "/100")
        stdout.flush()
        target = randrange(int(size * 1.10))
        retval = higher(array, target) 
        for i, num in enumerate(array):
            if num > target:
                expect = i
                break
        else:
            expect = len(array)
        if retval != expect:
            return False
    return True

def test_lower(lower, scale = 100):
    size = int(5000 * scale)
    array = [randrange(size) for i in range(size)]
    array.sort()
    for i in range(times):
        stdout.write("\rLoop " + str(i+1) + "/100")
        stdout.flush()
        target = randrange(int(size * 1.10))
        retval = lower(array, target) 
        for i, num in enumerate(array):
            if num >= target:
                expect = i - 1
                break
        else:
            expect = len(array) - 1
        if retval != expect:
            return False
    return True

def test_binary_search(search, scale = 100):
    size = int(5000 * scale)
    array = [i for i in range(size)]
    for i in range(times):
        target = randrange(int(size * 1.10))
        retval = search(array, target) 
        try:
            expect = array.index(target)
        except ValueError:
            if retval == -1:
                continue
        if retval != expect:
            return False
    return True

from binary_search import binary_search
from binary_search import lower
from binary_search import higher
from binary_search import equal_range
if __name__ == '__main__':
    print "Testing binary search ... "
    if not test_binary_search(binary_search, 1):
        print "WA: ", binary_search
    print "Testing lower bound ... "
    if not test_lower(lower, 10):
        print "\nWA: ", lower
    print "\nTesting upper bound ... "
    if not test_higher(higher, 10):
        print "\nWA: ", higher
    print "\nTesting equal_range ..."
    if not test_equal_range(equal_range, 10):
        print "\nWA: ", equal_range
    print
