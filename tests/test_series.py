# test_series.py
import unittest
from series import fibonacci, lucas, sum_series

class TestSeriesFunctions(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        # Add more test cases

    def test_lucas(self):
        self.assertEqual(lucas(0), 2)
        self.assertEqual(lucas(1), 1)
        self.assertEqual(lucas(2), 3)
        self.assertEqual(lucas(3), 4)
        self.assertEqual(lucas(4), 7)
        self.assertEqual(lucas(5), 11)
        self.assertEqual(lucas(6), 18)
        # Add more test cases

    def test_sum_series(self):
        self.assertEqual(sum_series(0), 0)
        self.assertEqual(sum_series(1), 1)
        self.assertEqual(sum_series(2), 1)
        self.assertEqual(sum_series(3), 2)
        self.assertEqual(sum_series(4), 3)
        self.assertEqual(sum_series(5), 5)
        self.assertEqual(sum_series(6), 8)
        # Add more test cases for Fibonacci series

        self.assertEqual(sum_series(0, 2, 1), 2)
        self.assertEqual(sum_series(1, 2, 1), 1)
        self.assertEqual(sum_series(2, 2, 1), 3)
        self.assertEqual(sum_series(3, 2, 1), 4)
        self.assertEqual(sum_series(4, 2, 1), 7)
        self.assertEqual(sum_series(5, 2, 1), 11)
        self.assertEqual(sum_series(6, 2, 1), 18)
        # Add more test cases for Lucas numbers

if __name__ == '__main__':
    unittest.main()
