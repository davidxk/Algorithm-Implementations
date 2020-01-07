import unittest
import random
from majority_vote import majority_vote, majority_vote_general

class TestMajorityVote(unittest.TestCase):
    def testMajorityVote(self):
        size = random.randrange(100, 500)
        for count in range(size):
            array = [0] * count
            array += [random.randrange(1, 3) for _ in range(size - count)]
            elect = None
            for num in set(array):
                if array.count(num) > len(array) / 2:
                    elect = num
            random.shuffle(array)
            self.assertEqual(majority_vote(array), elect)

    def testMajorityVoteGeneral(self):
        size = random.randrange(100, 500)
        for i in range(100):
            k = random.randrange(2, 10)
            value = random.randrange(1, 10)
            array = [random.randrange(value) for _ in range(size)]
            elect = []
            for num in set(array):
                if array.count(num) > len(array) / k:
                    elect.append(num)
            self.assertEqual(set(elect), set(majority_vote_general(array, k)))

    def testMajorityVoteEdgeCase(self):
        size = random.randrange(100, 500)
        for i in range(100):
            k = random.randrange(1, int(size * 1.5))
            value = random.randrange(1, 10)
            array = [random.randrange(value) for _ in range(size)]
            elect = []
            for num in set(array):
                if array.count(num) > len(array) / k:
                    elect.append(num)
            self.assertEqual(set(elect), set(majority_vote_general(array, k)))

if __name__ == "__main__":
    unittest.main()
