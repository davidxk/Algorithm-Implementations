from permutations import permutations, permutationsWithDup
from permutations import permsDedupCounter, permsDedupArray
from combinations import combinations, combinationsWithDup
from subsets import subsets, subsetsWithDup
from partitions import partitions
import itertools
import random
import unittest

class TestRecursion(unittest.TestCase):
    def testPermutations(self):
        for i in range(7):
            case = list(range(i))
            result = permutations(case)
            result = set(map(tuple, result))
            expect = itertools.permutations(case)
            expect = set(expect)
            self.assertEqual(result, expect)

    def testPermutationsWithDup(self):
        for i in range(50):
            case = [random.randrange(3) for i in range(random.randrange(3, 8))]
            result1 = permutationsWithDup(case)
            result1 = set(map(tuple, result1))
            result2 = permsDedupCounter(case)
            result2 = set(map(tuple, result2))
            result3 = permsDedupArray(case)
            result3 = set(map(tuple, result3))
            expect = itertools.permutations(case)
            expect = set(expect)
            self.assertEqual(result1, expect)
            self.assertEqual(result2, expect)
            self.assertEqual(result3, expect)

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

    def testPartitions(self):
        case = [None] * 4
        expect = [None] * 4
        case[0] = [1]
        expect[0] = [[[1]]]
        case[1] = [1, 2]
        expect[1] = [[[1, 2]], [[1], [2]]]
        case[2] = [1, 2, 3]
        expect[2] = [
                [[1, 2, 3]],
                [[1, 2], [3]],
                [[1, 3], [2]],
                [[1], [2, 3]],
                [[1], [2], [3]]
                ]
        case[3] = [1, 2, 3, 4]
        expect[3] = [
                [[1, 2, 3, 4]],
                [[1, 2, 3], [4]],
                [[1, 2, 4], [3]],
                [[1, 2], [3, 4]],
                [[1, 2], [3], [4]],
                [[1, 3, 4], [2]],
                [[1, 3], [2, 4]],
                [[1, 3], [2], [4]],
                [[1, 4], [2, 3]],
                [[1], [2, 3, 4]],
                [[1], [2, 3], [4]],
                [[1, 4], [2], [3]],
                [[1], [2, 4], [3]],
                [[1], [2], [3, 4]],
                [[1], [2], [3], [4]]
                ]
        for i in range(len(case)):
            self.assertEqual(partitions(case[i]), expect[i])

if __name__ == "__main__":
    unittest.main()
    unittest.main()
