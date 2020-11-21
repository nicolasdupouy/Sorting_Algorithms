import unittest

from BubbleSort import *


class BubbleSortTestCase(unittest.TestCase):
    def test_should_sort_array_of_positive_numbers(self):
        array = [6, 3, 0, 5, 1]
        array_expected = [0, 1, 3, 5, 6]
        self.assertEqual(array_expected, bubble_sort(array))
        self.assertEqual(array_expected, bubble_sort_not_so_naive_implementation(array))

    def test_should_sort_array_of_positive__and_negative_numbers(self):
        array = [-4, 6, 3, 0, -33, 5, 1]
        array_expected = [-33, -4, 0, 1, 3, 5, 6]

        self.assertEqual(array_expected, bubble_sort(array))
        self.assertEqual(array_expected, bubble_sort_not_so_naive_implementation(array))

    def test_bubble_sort_timeit(self):
        bubble_sort_one_million_calls([-4, 6, 3, 0, -33, 5, 1])
        bubble_sort_not_so_naive_implementation_one_million_calls([-4, 6, 3, 0, -33, 5, 1])


if __name__ == '__main__':
    unittest.main()
