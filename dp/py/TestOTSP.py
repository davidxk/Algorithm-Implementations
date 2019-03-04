import itertools
import random
import unittest
import time
from oTSP import *

class TestSeatArrangement(unittest.TestCase):
    def setUp(self, size = 8):
        valRange = 10
        self.dist = [[0] * size for i in range(size)]
        for i in range(size):
            for j in range(i + 1, size):
                self.dist[i][j] = self.dist[i][j] = random.randrange(valRange)

    def bruteForceARow(self, matrix):
        maxUtil = 0
        for perm in itertools.permutations(range(len(matrix))):
            util = 0
            for i in range(1, len(matrix)):
                util += matrix[perm[i]][perm[i - 1]]
            maxUtil = max(util, maxUtil)
        return maxUtil

    def testARow(self):
        for i in range(10):
            self.setUp()
            self.assertEqual(self.bruteForceARow(self.dist), seat_arrangement(self.dist))

    def testARow_(self):
        for i in range(10):
            self.setUp()
            self.assertEqual(self.bruteForceARow(self.dist), seat_arrangement_(self.dist))

    def __speed_test__(self, algo):
        time1 = time.time()
        for i in range(10):
            self.setUp(12)
            algo(self.dist)
        time2 = time.time()
        print time2 - time1

    def testRunningTime(self):
        self.__speed_test__(seat_arrangement)
        self.__speed_test__(seat_arrangement_)

if __name__ == "__main__":
    unittest.main()
