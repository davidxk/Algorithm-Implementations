import itertools
import random
import unittest
import time
from GridSeatArrangement import *

class TestSeatArrangement(unittest.TestCase):
    def setUp(self, size = 8):
        valRange = 10
        self.dist = [[0] * size for i in range(size)]
        for i in range(size):
            for j in range(i + 1, size):
                self.dist[i][j] = self.dist[i][j] = random.randrange(valRange)

    def bruteForceGrid(self, matrix, k):
        maxUtil = 0
        for perm in itertools.permutations(range(len(matrix))):
            util = 0
            for i in range(len(matrix)):
                if i % k != 0:
                    util += matrix[perm[i]][perm[i - 1]]
                if i / k != 0:
                    util += matrix[perm[i]][perm[i - k]]
            maxUtil = max(util, maxUtil)
        return maxUtil

    def testGrid(self):
        for i in range(10):
            self.setUp()
            self.assertEqual(self.bruteForceGrid(self.dist), seat_arrangement_grid(self.dist))

    def testGrid_(self):
        for i in range(10):
            self.setUp()
            self.assertEqual(self.bruteForceGrid(self.dist), seat_arrangement_grid_(self.dist))

    def __speed_test__(self, algo):
        time1 = time.time()
        for i in range(10):
            self.setUp(12)
            algo(self.dist)
        time2 = time.time()
        print time2 - time1

    def testRunningTime(self):
        self.__speed_test__(seat_arrangement_grid)
        self.__speed_test__(seat_arrangement_grid_)

if __name__ == "__main__":
    unittest.main()

