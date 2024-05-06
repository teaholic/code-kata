import unittest

from parameterized import parameterized

from fizzbuzz.app import FizzBuzzApp


class TestFizzBuzzApp(unittest.TestCase):

    @parameterized.expand([
        [1, 1],
        [2, 2],
        [3, "Fizz"],
        [4, 4],
        [5, "Buzz"],
        [6, "Fizz"],
        [7, 7],
        [8, 8],
        [9, "Fizz"],
        [10, "Buzz"],
        [11, 11],
        [12, "Fizz"],
        [13, 13],
        [14, 14],
        [15, "FizzBuzz"],
    ])
    def test_run(self, input, expected):
        actual = FizzBuzzApp().run(input)
        self.assertEqual(actual, expected)
