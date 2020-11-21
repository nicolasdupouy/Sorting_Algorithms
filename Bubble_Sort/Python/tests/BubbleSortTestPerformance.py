import unittest
from src.BubbleSort import *
from tests.Timing import *


@time_with_one_million_calls
def bubble_sort_one_million_calls(array):
    return bubble_sort(array)


@time_with_one_million_calls
def bubble_sort_not_so_naive_implementation_one_million_calls(array):
    return bubble_sort_not_so_naive_implementation(array)


class BubbleSortTestPerformance(unittest.TestCase):
    @staticmethod
    def test_bubble_sort_timeit():
        bubble_sort_one_million_calls([-4, 6, 3, 0, -33, 5, 1])
        bubble_sort_not_so_naive_implementation_one_million_calls([-4, 6, 3, 0, -33, 5, 1])


if __name__ == '__main__':
    unittest.main()