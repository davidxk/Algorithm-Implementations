import bisect
import mybisect
import random
import unittest

class TestMybisect(unittest.TestCase):
    def setUp(self):
        self.array = [random.randrange(1000) for i in range(100)]
        self.array.sort()
        self.cases = [random.randrange(-1100, 1100) for i in range(100)]

    def testBisect(self):
        for case in self.cases:
            self.assertEqual(mybisect.bisect(self.array, case), \
                    bisect.bisect(self.array, case))

    def testBisectLeft(self):
        for case in self.cases:
            self.assertEqual(mybisect.bisect_left(self.array, case), \
                    bisect.bisect_left(self.array, case))

if __name__ == "__main__":
    unittest.main()
