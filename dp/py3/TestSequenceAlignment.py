import unittest
import random
import collections
from sequence_alignment import *

class TestSequenceAlignment(unittest.TestCase):
    def __gen_case__(self):
        bases = "ATCG"
        X = str().join(random.choice(bases) for i in range(50))
        Y = str().join(random.choice(bases) for i in range(50))
        gap_penalty = 2
        mmat = [[0, 1, 2, 3],
                [1, 0, 3, 2],
                [2, 3, 0, 1],
                [3, 2, 1, 0]]
        mismatch_penalty = collections.defaultdict(dict)
        for i in range(len(bases)):
            for j in range(len(bases)):
                mismatch_penalty[bases[i]][bases[j]] = mmat[i][j]
        return X, Y, gap_penalty, mismatch_penalty

    def testTableFilling(self):
        for i in range(10):
            X, Y, gap_penalty, mismatch_penalty = self.__gen_case__()
            min1 = sequence_alignment_memo(X, Y, gap_penalty, mismatch_penalty)
            min2 = sequence_alignment(X, Y, gap_penalty, mismatch_penalty)

if __name__ == "__main__":
    unittest.main()
