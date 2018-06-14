from binary_search import binary_search, lower, higher, equal_range
import unittest
import random

class TestBinarySearch(unittest.TestCase):
    def setUp(self, scale = 100):
        self.times = 100
        self.size = int(3000 * scale)
        self.array = [random.randrange(self.size) for i in range(self.size)]
        self.array.sort()

    def test_equal_range(self):
        for i in range(self.times):
            target = random.randrange(int(self.size * 1.10))
            retval = equal_range(self.array, target) 
            if target not in self.array:
                if retval != (-1, -1):
                    return False
                else:
                    continue
            left = lower(self.array, target) + 1
            right = higher(self.array, target) - 1
            self.assertEqual(retval, (left, right))

    def test_higher(self):
        for i in range(self.times):
            target = random.randrange(int(self.size * 1.10))
            retval = higher(self.array, target) 
            for i, num in enumerate(self.array):
                if num > target:
                    expect = i
                    break
            else:
                expect = len(self.array)
            self.assertEqual(retval, expect)

    def test_lower(self):
        for i in range(self.times):
            target = random.randrange(int(self.size * 1.10))
            retval = lower(self.array, target) 
            for i, num in enumerate(self.array):
                if num >= target:
                    expect = i - 1
                    break
            else:
                expect = len(self.array) - 1
            self.assertEqual(retval, expect)

    def test_binary_search(self):
        self.array = [i for i in range(self.size)]
        for i in range(self.times):
            target = random.randrange(int(self.size * 1.10))
            retval = binary_search(self.array, target) 
            try:
                expect = self.array.index(target)
            except ValueError:
                self.assertEqual(retval, -1)
                continue
            self.assertEqual(retval, expect)

if __name__ == '__main__':
    print "These tests could take up to 10 secends to finish"
    unittest.main()
