import unittest

from LinkedList import getArray
from LinkedList import getLinkedList
from reverse_linked_list import reverse_linked_list
from find_middle import find_middle

class TestLinkedListAlgorithms(unittest.TestCase):
    def testReverseLinkedList(self):
        case = range(100)
        rev = list(case)
        rev.reverse()
        self.assertEqual(rev, \
                getArray( reverse_linked_list(getLinkedList(case)) ))

    def testFindMiddle(self):
        size = 100
        node = find_middle(getLinkedList(range(1, size + 1)))
        self.assertEqual(node.val, size / 2)
        size -= 1
        node = find_middle(getLinkedList(range(1, size + 1)))
        self.assertEqual(node.val, size / 2 + 1)

from random import randrange
from list_merge_sort import list_merge_sort

class TestLinkedListSorting(unittest.TestCase):
    def checkSortImpl(self, sort):
        array = [randrange(5000) for i in range(5000)]
        head = getLinkedList(array)
        head = sort(head)
        array.sort()
        for num in array:
            self.assertEqual(head.val, num)
            head = head.next
        self.assertEqual(head, None)

    def testListMergeSort(self):
        self.checkSortImpl(list_merge_sort)

if __name__ == "__main__":
    unittest.main()
