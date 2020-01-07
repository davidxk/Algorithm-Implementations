from kmp_matcher import kmp_matcher
from naive_matcher import naive_matcher
import unittest
import random
from time import time

class TestStringMathcer(unittest.TestCase):
    def __gen_str__(self, size):
        text = []
        for i in range(size):
            rand_base = random.random()
            if rand_base < 0.25:
                text.append('A')
            elif rand_base < 0.50:
                text.append('T')
            elif rand_base < 0.75:
                text.append('C')
            else:
                text.append('G')
        return str().join(text)

    def __check_matcher__(self, matcher):
        time0 = time()
        for i in range(100):
            text = self.__gen_str__(10000)
            patt = self.__gen_str__(random.randrange(10, 50))
            self.assertEqual(matcher(patt, text), text.find(patt))
        time1 = time()
        print(time1 - time0, matcher)

    def testNaiveMatcher(self):
        self.__check_matcher__(naive_matcher)

    def testKMPMatcher(self):
        self.__check_matcher__(kmp_matcher)

if __name__ == "__main__":
    unittest.main()
