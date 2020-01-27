import unittest
import math
import random
import mymath

class TestMymath(unittest.TestCase):
    def testGCD(self):
        for i in range(100):
            a, b = random.randrange(100000), random.randrange(100000)
            self.assertEqual(mymath.gcd(a, b), math.gcd(a, b))

    def testExtendedEuclidean(self):
        for i in range(100):
            a, b = random.randrange(100000), random.randrange(100000)
            r, s, t = mymath.egcd(a, b)
            self.assertEqual(r, math.gcd(a, b))
            self.assertEqual(a * s + b * t, r)

    def testModInv(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        for prime in primes:
            for num in range(1, prime):
                self.assertEqual(num * mymath.mod_inv(num, prime) % prime, 1)

    def testChineseRemainderTheorem(self):
        moduli, remainders = [3, 5, 7], [2, 3, 2]
        self.assertEqual(mymath.chinese_remainder_theorem(moduli, remainders), 23)

    def testFracCeiling(self):
        for i in range(100):
            a, b = random.randrange(100000), random.randrange(100000)
            big, small = max(a, b), min(a, b)
            expected = big // small
            if big % small != 0:
                expected += 1
            self.assertEqual(mymath.frac_ceiling(big, small), expected)

if __name__ == "__main__":
    unittest.main()
