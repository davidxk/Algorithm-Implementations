import unittest
import random

from LinkedList import getArray
from LinkedList import getLinkedList
from reverse_linked_list import reverse_linked_list
from find_middle import find_middle
from cycle_detection import cycle_detection, cycle_finding

class TestLinkedListAlgorithms(unittest.TestCase):
    def testReverseLinkedList(self):
        case = range(100)
        rev = list(case)
        rev.reverse()
        self.assertEqual(rev, \
                getArray( reverse_linked_list(getLinkedList(case)) ))

    def testFindMiddle(self):
        size = 100
        node = find_middle(getLinkedList(range(size)))
        self.assertEqual(node.val, size // 2)
        size -= 1
        node = find_middle(getLinkedList(range(size)))
        self.assertEqual(node.val, size // 2)

    def testCycleDetection(self):
        size = 100
        head = getLinkedList(range(size))
        curr = head
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next
        if random.random() < 0.5:
            node = random.choice(nodes)
            nodes[-1].next = node
            self.assertTrue(cycle_detection(head))
            self.assertEqual(node, cycle_finding(head))
        else:
            self.assertFalse(cycle_detection(head))
            self.assertIsNone(cycle_finding(head))

from random import randrange
from list_merge_sort import list_merge_sort
from list_quick_sort import list_quick_sort

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

    def testListQuickSort(self):
        self.checkSortImpl(list_quick_sort)

if __name__ == "__main__":
    unittest.main()
