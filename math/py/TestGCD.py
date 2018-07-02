import unittest
import fractions
import random
import mymath

class TestGCD(unittest.TestCase):
    def testGCD(self):
        for i in range(100):
            a, b = random.randrange(100000), random.randrange(100000)
            self.assertEqual(mymath.gcd(a, b), fractions.gcd(a, b))

if __name__ == "__main__":
    unittest.main()
