import unittest
import random
from weighted_interval_scheduling import *

class TestWeightedIntervalScheduling(unittest.TestCase):
    def __gen_cases__(self, n):
        cases = []
        for i in range(n):
            intervals = []
            for i in range(1000):
                startTime = random.randrange(1000)
                endTime = random.randrange(startTime + 1, startTime + 21)
                value = random.randrange(30)
                interval = (startTime, endTime, value)
                intervals.append(interval)
            intervals.sort(key=lambda interval: interval[1])
            case = zip(*intervals)
            cases.append(case)
        return cases

    def testComputeOPT(self):
        cases = self.__gen_cases__(100)
        for case in cases:
            startTimes, endTimes, values = case
            max1 = weighted_interval_scheduling(startTimes, endTimes, values)
            max2 = weighted_interval_scheduling_memo(startTimes, endTimes, values)
            self.assertEqual(max1, max2)

    def testFindSolution(self):
        cases = self.__gen_cases__(100)
        for case in cases:
            startTimes, endTimes, values = case
            sol1, max1 = weighted_interval_scheduling_sol(startTimes, endTimes, values)
            sol2, max2 = weighted_interval_scheduling_memo_sol(startTimes, endTimes, values)
            self.assertEqual(max1, max2)
            self.assertEqual(set(sol1), set(sol2))

if __name__ == "__main__":
    unittest.main()
