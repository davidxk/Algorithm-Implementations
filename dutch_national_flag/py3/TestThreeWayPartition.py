import unittest
import random
from collections import Counter
from three_way_partition import three_way_partition

class TestThreeWayPartition(unittest.TestCase):
    def testThreeWayPartition(self):
        size = 1000
        case = [random.randrange(3) for i in range(size)]
        cnt = Counter(case)
        three_way_partition(case)
        for i, num in enumerate(case):
            if i > 0:
                self.assertTrue(case[i - 1] <= case[i])
            cnt[num] -= 1
        self.assertEqual(sum(cnt.values()), 0)

if __name__ == "__main__":
    unittest.main()
