import unittest

from BubbleSort import *

class BubbleSortTestCase(unittest.TestCase):
    def test_should_sort_array_of_positive_numbers(self):
        array = [6, 3, 0, 5, 1]
        array_expected = [0, 1, 3, 5, 6]
        self.assertEqual(array_expected, bubbleSort(array))


if __name__ == '__main__':
    unittest.main()
