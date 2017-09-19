from random import randrange, shuffle

def test_select(select):
    size = 5000
    array = [i for i in range(size)]
    for i in range(200):
        shuffle(array)
        rank = randrange(1, 5000)
        retval = select(array, rank)
        array.sort()
        expect = array[rank - 1]
        if retval != expect:
            return False
    return True

from randomized_select import randomized_select
from bfprt_select import bfprt_select
if __name__ == '__main__':
    print "This could take up to 10 seconds ..."
    for select in [randomized_select, bfprt_select]:
        if not test_select(select):
            print "WA:", select
        else:
            print select, "done"
