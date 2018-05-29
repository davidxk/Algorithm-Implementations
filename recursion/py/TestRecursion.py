from permutations import permutations, permutationsWithDup
from combinations import combinations, combinationsWithDup
from subsets import subsets, subsetsWithDup
import itertools
import random
import unittest

class TestRecursion(unittest.TestCase):
    def testPermutations(self):
        for i in range(7):
            case = range(i)
            result = permutations(case)
            result = set(map(tuple, result))
            expect = itertools.permutations(case)
            expect = set(expect)
            self.assertEqual(result, expect)

    def testPermutationsWithDup(self):
        for i in range(50):
            case = [random.randrange(3) for i in range(random.randrange(3, 8))]
            result = permutationsWithDup(case)
            result = set(map(tuple, result))
            expect = itertools.permutations(case)
            expect = set(expect)
            self.assertEqual(result, expect)

    def testCombinations(self):
        for i in range(15):
            case = range(i)
            k = random.randrange(len(case) + 1)
            result = combinations(case, k)
            result = set(map(tuple, result))
            expect = itertools.combinations(case, k)
            expect = set(expect)
            self.assertEqual(result, expect)

    def testCombinationsWithDup(self):
        for i in range(20):
            case = [random.randrange(5) for i in range(random.randrange(5, 15))]
            k = random.randrange(len(case) + 1)
            result = combinationsWithDup(case, k)
            result = set(map(tuple, result))
            expect = itertools.combinations(case, k)
            expect = set(expect)
            self.assertEqual(result, expect)

    def testSubsets(self):
        for size in range(11):
            case = range(size)
            result = subsets(case)
            result = set(map(tuple, result))
            expect = set()
            for j in range(size + 1):
                comb = itertools.combinations(case, j)
                expect |= set(comb)
            self.assertEqual(result, expect)

    def testSubsetsWithDup(self):
        for i in range(20):
            case = [random.randrange(3) for i in range(random.randrange(3, 8))]
            result = subsetsWithDup(case)
            result = set(map(tuple, result))
            expect = set()
            for j in range(len(case) + 1):
                comb = itertools.combinations(case, j)
                expect |= set(comb)
            self.assertEqual(result, expect)

if __name__ == "__main__":
    unittest.main()
    unittest.main()
