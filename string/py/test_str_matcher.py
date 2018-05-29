from random import random
from time import time

def gen_str(size):
    text = []
    for i in range(size):
        rand_base = random()
        if rand_base < 0.25:
            text.append('A')
        elif rand_base < 0.50:
            text.append('T')
        elif rand_base < 0.75:
            text.append('C')
        else:
            text.append('G')
    return str().join(text)

def test_str_matcher(matcher):
    time0 = time()
    for i in range(100):
        text = gen_str(20000)
        patt = gen_str(10)
        if matcher(patt, text) != text.find(patt):
            return False
    time1 = time()
    print time1 - time0, matcher
    return True


from kmp_matcher import kmp_matcher
from naive_matcher import naive_matcher

if __name__ == "__main__":
    for matcher in [naive_matcher, kmp_matcher]:
        if not test_str_matcher(matcher):
            print "WA: ", matcher
