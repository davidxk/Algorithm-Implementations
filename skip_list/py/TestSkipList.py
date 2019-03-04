import random
import unittest
import bisect
from SkipList import SkipList

class TestSkipList(unittest.TestCase):
    def setUp(self):
        self.skiplist = SkipList()
        self.size = 500

    def consistencyCheck(self, skiplist):
        length = len(skiplist)
        height = len(skiplist.head.next)
        curr = skiplist.head
        for i in range(length):
            self.assertLessEqual(len(curr.next), height)
            self.assertLess(curr.key, curr.next[0].key)
            curr = curr.next[0]
        self.assertEqual(curr.next[0].key, float("inf"))

    def testAppend(self):
        self.assertEqual(len(self.skiplist), 0)
        for i in range(self.size):
            self.assertNotIn(i, self.skiplist)
            self.skiplist.add(i)
            self.assertIn(i, self.skiplist)
            self.consistencyCheck(self.skiplist)
            self.assertEqual(len(self.skiplist), i + 1)

    def testRandomAdd(self):
        nums = range(self.size)
        random.shuffle(nums)
        for num in nums:
            self.skiplist.add(num)
        self.assertEqual(len(self.skiplist), len(nums))
        for num in nums:
            self.assertIn(num, self.skiplist)
        self.consistencyCheck(self.skiplist)

    def testRemoveTail(self):
        for i in range(self.size):
            self.skiplist.add(i)
        for i in reversed(range(self.size)):
            self.assertIn(i, self.skiplist)
            self.skiplist.remove(i)
            self.assertNotIn(i, self.skiplist)
            self.consistencyCheck(self.skiplist)
            self.assertEqual(len(self.skiplist), i)

    def testRemoveHead(self):
        for i in range(self.size):
            self.skiplist.add(i)
        for i in range(self.size):
            self.assertIn(i, self.skiplist)
            self.skiplist.remove(i)
            self.assertNotIn(i, self.skiplist)
            self.consistencyCheck(self.skiplist)
            self.assertEqual(len(self.skiplist), self.size - i - 1)

    def testRandomRemove(self):
        for i in range(self.size):
            self.skiplist.add(i)
        nums = range(self.size)
        random.shuffle(nums)
        for i, num in enumerate(nums):
            self.assertIn(num, self.skiplist)
            self.skiplist.remove(num)
            self.assertNotIn(num, self.skiplist)
            self.consistencyCheck(self.skiplist)
            self.assertEqual(len(self.skiplist), self.size - i - 1)

    def testFind(self):
        size = int(self.size ** 0.5)
        nums = range(size)
        random.shuffle(nums)
        for i, num in enumerate(nums):
            self.skiplist.add(num)
            for j in range(len(nums)):
                if j <= i:
                    self.assertIsNotNone(self.skiplist.find(nums[j]))
                else:
                    self.assertIsNone(self.skiplist.find(nums[j]))

        random.shuffle(nums)
        for i, num in enumerate(nums):
            self.skiplist.remove(num)
            for j in range(len(nums)):
                if j <= i:
                    self.assertIsNone(self.skiplist.find(nums[j]))
                else:
                    self.assertIsNotNone(self.skiplist.find(nums[j]))

    def testFloor(self):
        case = [random.randrange(self.size) for i in range(self.size)]
        for num in case:
            self.skiplist.add(num)
        case.sort()
        for i in range(100):
            target = random.randrange(-1, self.size)
            floor = -float("inf")
            index = bisect.bisect(case, target) - 1
            if 0 <= index < len(case):
                floor = case[index]
            self.assertEqual(self.skiplist.floor(target), floor)

    def testCeiling(self):
        case = [random.randrange(self.size) for i in range(self.size)]
        for num in case:
            self.skiplist.add(num)
        case.sort()
        for i in range(100):
            target = random.randrange(-1, self.size)
            ceiling = float("inf")
            index = bisect.bisect_left(case, target)
            if 0 <= index < len(case):
                ceiling = case[index]
            self.assertEqual(self.skiplist.ceiling(target), ceiling)

if __name__ == "__main__":
    unittest.main()
