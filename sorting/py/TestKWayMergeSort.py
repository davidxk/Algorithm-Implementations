import operator
import unittest
from random import randrange
from k_way_merge_sort import k_way_merge_sort

class TestKWayMergeSort(unittest.TestCase):
    def testKWayMergeSort(self):
        for i in range(50):
            k = randrange(2, 20)
            arrays = [[randrange(9999) for _ in range(1000)] for _ in range(k)]
            for array in arrays:
                array.sort()
            expect = reduce(operator.add, arrays)
            expect.sort()
            result = k_way_merge_sort(arrays)
            self.assertEqual(result, expect)

if __name__ == '__main__':
    print "This could take up to 2 seconds. "
    unittest.main()
