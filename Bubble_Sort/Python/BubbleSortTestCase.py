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
        self.time_function_with_one_million_calls(bubble_sort, [-4, 6, 3, 0, -33, 5, 1])
        self.time_function_with_one_million_calls(bubble_sort_not_so_naive_implementation, [-4, 6, 3, 0, -33, 5, 1])

    @staticmethod
    def time_function_with_one_million_calls(f, array):
        import timeit
        start = timeit.default_timer()

        for t in range(1000000):
            f(array)

        stop = timeit.default_timer()
        execution_time_in_seconds = stop - start

        print(f"Program Executed in [function {f.__name__}] "+str(execution_time_in_seconds))


if __name__ == '__main__':
    unittest.main()
