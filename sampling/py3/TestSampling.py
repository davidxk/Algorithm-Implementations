import unittest
from collections import Counter
from simple_random_sample import *
from weightd_random_sample import weighted_random_sample

class TestSampling(unittest.TestCase):
    def __test_srs__(self, algo, isIter):
        size = 10
        array = list(range(size))
        cnt = Counter()
        times = 1000
        for i in range(times):
            if isIter:
                sample = algo(iter(array), size // 2)
            else:
                sample = algo(array, size // 2)
            self.assertEqual(len(sample), size // 2)
            for num in sample:
                cnt[num] += 1
        for num in array:
            self.assertGreater(cnt[num], 0.4 * times)
            self.assertLess(cnt[num], 0.6 * times)

    def testWeightedSampling(self):
        size = 1000
        for i in range(100):
            result = sum(weighted_random_sample([1, 2]) for i in range(size))
            self.assertLessEqual(result, size * 0.72)
            self.assertGreaterEqual(result, size * 0.62)

    def testDrawByDraw(self):
        self.__test_srs__(draw_by_draw, False)

    def testSelectionRejection(self):
        self.__test_srs__(selection_rejection, False)

    def testReservoirSampling(self):
        self.__test_srs__(reservoir_sampling, True)

if __name__ == "__main__":
    unittest.main()
