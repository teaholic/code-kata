import unittest

from parameterized import parameterized

from fizzbuzz.app import FizzBuzzApp
from fizzbuzz.handler import MultipleOfThree, MultipleOfFive, MultipleOfSeven, MultipleOfEleven


class TestFizzBuzzApp(unittest.TestCase):
    @parameterized.expand(
        [
            [1, 1],
            [2, 2],
            [3, "Fizz"],
            [4, 4],
            [5, "Buzz"],
            [6, "Fizz"],
            [7, "Whizz"],
            [8, 8],
            [9, "Fizz"],
            [10, "Buzz"],
            [11, "Bang"],
            [12, "Fizz"],
            [13, 13],
            [14, "Whizz"],
            [15, "FizzBuzz"],
            [16, 16],
            [17, 17],
            [18, "Fizz"],
            [19, 19],
            [20, "Buzz"],
            [21, "FizzWhizz"],
            [22, "Bang"],
        ]
    )
    def test_run(self, n, expected):
        chain_of_responsibility = [MultipleOfThree(), MultipleOfFive(), MultipleOfSeven(), MultipleOfEleven()]
        actual = FizzBuzzApp(chain_of_responsibility).run(n)
        self.assertEqual(actual, expected)
