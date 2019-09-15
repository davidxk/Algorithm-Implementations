import unittest
import random
import string
from longest_common_subsequence import *

class TestLongestCommonSubsequence(unittest.TestCase):
    def __gen_case__(self):
        str1 = str().join(random.choice(string.ascii_lowercase) for _ in range(50))
        str2 = str().join(random.choice(string.ascii_lowercase) for _ in range(50))
        return str1, str2

    def testTableFilling(self):
        for i in range(50):
            str1, str2 = self.__gen_case__()
            max1 = longest_common_subsequence_memo(str1, str2)
            max2 = longest_common_subsequence(str1, str2)
            self.assertEqual(max1, max2)

if __name__ == "__main__":
    unittest.main()
