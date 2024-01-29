import unittest

from src_lib.fibonacci_day import (
    get_day,
    fibonacci_recursive,
    get_fibonacci_day
)
from tests_consts import FIBONACCI_KWARGS


class TestLib(unittest.TestCase):
    MAX_DAY = 31
    MIN_DAY = 1

    def test_get_day_positive(self):
        """day is int"""

        value = get_day()
        self.assertIsInstance(value, int)

    def test_get_day_exist(self):
        """1 <= day <= 31"""

        value = get_day()
        self.assertLessEqual(value, self.MAX_DAY)
        self.assertGreaterEqual(value, self.MIN_DAY)

    def test_fibonacci_recursive_exist(self):
        fibonacci = {}

        for i in range(self.MIN_DAY + 1, self.MAX_DAY + 2):
            fibonacci[i] = fibonacci_recursive(i)

        self.assertEqual(fibonacci, FIBONACCI_KWARGS)

    def test_get_fibonacci_day_exist(self):
        fibonacci_day = {}

        for i in range(self.MIN_DAY, self.MAX_DAY + 1):
            fibonacci_day[i + 1] = get_fibonacci_day(i)

        self.assertEqual(fibonacci_day, FIBONACCI_KWARGS)


if __name__ == '__main__':
    unittest.main()
