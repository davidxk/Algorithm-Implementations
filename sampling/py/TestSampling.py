import unittest
from WeightdRandomSample import weighted_random_sample

class TestSampling(unittest.TestCase):
    def testWeightedSampling(self):
        size = 1000
        for i in range(100):
            result = sum(weighted_random_sample([1, 2]) for i in range(size))
            self.assertLessEqual(result, size * 0.72)
            self.assertGreaterEqual(result, size * 0.62)

if __name__ == "__main__":
    unittest.main()
