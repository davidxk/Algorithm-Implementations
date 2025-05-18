import unittest
from pretty_printing import *


class PrettyPrintingProblem:
    def __init__(self, words, max_line_len):
        self.words = words
        self.max_line_len = max_line_len


class TestSegmentedLeastSquares(unittest.TestCase):
    def setUp(self):
        case1 = PrettyPrintingProblem([
            "Though", "much", "is", "taken", "much", "abides", "and", "though",
            "We", "are", "not", "now", "that", "strength", "which", "in",
            "old", "days", "Moved", "earth", "and", "heaven", "that", "which",
            "we", "are", "we", "are", "One", "equal", "temper", "of", "heroic",
            "hearts", "Made", "weak", "by", "time", "and", "fate", "but",
            "strong", "in", "will", "To", "strive", "to", "seek", "to", "find",
            "and", "not", "to", "yield"
        ], 40)
        case2 = PrettyPrintingProblem([
            "Call", "me", "Ishmael", "Some", "years", "ago", "never", "mind",
            "how", "long", "precisely", "having", "little", "or", "no",
            "money", "in", "my", "purse", "and", "nothing", "particular", "to",
            "intingest", "me", "on", "shore", "I", "thought", "I", "would",
            "sail", "about", "a", "little", "and", "see", "the", "watingy",
            "part", "of", "the", "world"
        ], 40)
        self.cases = [case1, case2]

    def testComputeOPT(self):
        for case in self.cases:
            min1 = pretty_printing(case.words, case.max_line_len)
            min2 = pretty_printing_memo(case.words, case.max_line_len)
            self.assertEqual(min1, min2)

    @unittest.skip("no need for testing; only printing for visualization")
    def testFindSolution(self):
        for case in self.cases:
            sol, _ = pretty_printing_sol(case.words, case.max_line_len)
            print('\n'.join(sol) + '\n')


if __name__ == "__main__":
    unittest.main()
