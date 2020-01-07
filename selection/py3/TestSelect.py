import random
import time
import unittest
from quick_select import quick_select
from bfprt_select import bfprt_select

class TestSelect(unittest.TestCase):
    def __test_select__(self, select):
        size = random.randrange(4000, 5000)
        array = [random.randrange(int(size * 1.2)) for i in range(size)]
        copy = sorted(array)
        time1 = time.time()
        for i in range(100):
            random.shuffle(array)
            rank = random.randrange(1, size + 1)
            retval = select(array, rank)
            self.assertEqual(retval, copy[rank - 1])
        time2 = time.time()
        print(time2 - time1, select)

    def testQuickSelect(self):
        self.__test_select__(quick_select)

    def testBFPRTSelect(self):
        self.__test_select__(bfprt_select)

if __name__ == '__main__':
    unittest.main()
