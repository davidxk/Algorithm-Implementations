import random
import time
import unittest
from knapsack import *

class TestKnapsack(unittest.TestCase):
    def setUp(self):
        self.cases = []
        for i in range(50):
            nItems = random.randrange(40, 61)
            capacity = random.randrange(100, 301)
            weights = [random.randint(1, 11) for _ in range(nItems)]
            values = [random.randint(10, 101) for _ in range(nItems)]
            self.cases.append([weights, values, capacity])

    def testKnapsackResult(self):
        for weights, values, capacity in self.cases:
            max1 = knapsack(weights, values, capacity)
            max2 = knapsack_two_rows(weights, values, capacity)
            max3 = knapsack_one_row(weights, values, capacity)
            max4 = knapsack_memo(weights, values, capacity)
            self.assertEqual(max1, max2)
            self.assertEqual(max1, max3)
            self.assertEqual(max1, max4)

    def __speed_test__(self, algo):
        time1 = time.time()
        for i in range(20):
            weights, values, capacity = self.cases[i]
            algo(weights, values, capacity)
        time2 = time.time()
        print("%-45s\t%f" % (algo, time2 - time1))

    def testRunningTime(self):
        print()
        self.__speed_test__(knapsack)
        self.__speed_test__(knapsack_two_rows)
        self.__speed_test__(knapsack_one_row)
        self.__speed_test__(knapsack_memo)

if __name__ == "__main__":
    print("This could take up to 10 seconds")
    unittest.main()
