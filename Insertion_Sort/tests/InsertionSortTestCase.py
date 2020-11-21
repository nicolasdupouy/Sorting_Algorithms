import unittest
from src.InsertionSort import insertion_sort


class InsertionSortTestCase(unittest.TestCase):
    def test_should_sort_array_of_positive_numbers(self):
        array = [6, 3, 0, 5, 1]
        array_expected = [0, 1, 3, 5, 6]
        self.assertEqual(array_expected, insertion_sort(array))

    def test_should_sort_array_of_positive__and_negative_numbers(self):
        array = [-4, 6, 3, 0, -33, 5, 1]
        array_expected = [-33, -4, 0, 1, 3, 5, 6]

        self.assertEqual(array_expected, insertion_sort(array))


if __name__ == '__main__':
    unittest.main()
