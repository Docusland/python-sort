"""
    Coding exercise for IT students.
"""

import unittest
import sort


class SortTest(unittest.TestCase):
    """
    Coding exercise for IT students.
    The target of this script is to store different algorithms that sort an array.
    An explanation on the different sort algorithms is available in the sort.py script file.
    """

    def test_bubble_sort(self):
        """ Test Bubble Sort. read sort.py for instructions. """
        sample = [3, 1, 10, 5, 654, 45, 8, 5, 31, 123]
        sorted_sample = [1, 3, 5, 5, 8, 10, 31, 45, 123, 654]
        self.assertEqual(sorted_sample, sort.bubble_sort(sample))

    def test_insertion_sort(self):
        """ Test Insertion Sort. read sort.py for instructions. """
        sample = [3, 1, 10, 5, 654, 45, 8, 5, 31, 123]
        sorted_sample = [1, 3, 5, 5, 8, 10, 31, 45, 123, 654]
        self.assertEqual(sorted_sample, sort.insertion_sort(sample))

    def tests_selection_sort(self):
        """ Test Selection Sort. read sort.py for instructions. """
        sample = [3, 1, 10, 5, 654, 45, 8, 5, 31, 123]
        sorted_sample = [1, 3, 5, 5, 8, 10, 31, 45, 123, 654]
        self.assertEqual(sorted_sample, sort.selection_sort(sample))

    def tests_merge_sort(self):
        """ Test Merge Sort. read sort.py for instructions. """
        sample = [3, 1, 10, 5, 654, 45, 8, 5, 31, 123]
        sorted_sample = [1, 3, 5, 5, 8, 10, 31, 45, 123, 654]
        self.assertEqual(sorted_sample, sort.merge_sort(sample))

    def tests_quick_sort(self):
        """ Test Quick Sort. read sort.py for instructions. """
        sample = [3, 1, 10, 654, 45, 5, 8, 5, 31, 123]
        sorted_sample = [1, 3, 5, 5, 8, 10, 31, 45, 123, 654]
        self.assertEqual(sorted_sample, sort.quick_sort(sample))

    def tests_heap_sort(self):
        """ Test Heap Sort. read sort.py for instructions. """
        sample = [3, 1, 10, 654, 45, 5, 8, 5, 31, 123]
        sorted_sample = [1, 3, 5, 5, 8, 10, 31, 45, 123, 654]
        self.assertEqual(sorted_sample, sort.heap_sort(sample))

    if __name__ == '__main__':
        unittest.main()
