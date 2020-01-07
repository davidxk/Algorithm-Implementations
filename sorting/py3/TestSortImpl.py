from collections import Counter
from random import randrange
import time
import random
import unittest

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from heap_sort import heap_sort
from quick_sort_lomuto import quick_sort_lomuto
from quick_sort import quick_sort

class TestSortImpl(unittest.TestCase):
    def __check_sort_impl__(self, sort_algo):
        time1 = time.time()
        for i in range(10):
            size = random.randrange(1000, 2000)
            array = [random.randrange(size) for i in range(size)]
            copy = list(array)
            copy.sort()
            sort_algo(array)
            self.assertEqual(array, copy)
        time2 = time.time()
        print(sort_algo, time2 - time1)

    def testBubbleSort(self):
        self.__check_sort_impl__(bubble_sort)

    def testInsertionSort(self):
        self.__check_sort_impl__(insertion_sort)

    def testSelectionSort(self):
        self.__check_sort_impl__(selection_sort)

    def testMergeSort(self):
        self.__check_sort_impl__(merge_sort)

    def testHeapSort(self):
        self.__check_sort_impl__(heap_sort)

    def testQuickSortLomuto(self):
        self.__check_sort_impl__(quick_sort_lomuto)

    def testQuickSort(self):
        self.__check_sort_impl__(quick_sort)

if __name__ == '__main__':
    unittest.main()
