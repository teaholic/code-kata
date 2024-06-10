import unittest

from parameterized import parameterized

from fizzbuzz.handler import MultipleOfThree, MultipleOfFive, MultipleOfSeven, MultipleOfEleven, HandlerFactory, Handler


class TestHandler(unittest.TestCase):

    @parameterized.expand(
        [
            [1, ""],
            [2, ""],
            [3, "Fizz"],
            [4, ""],
            [5, ""],
            [6, "Fizz"],
            [7, ""],
            [8, ""],
            [9, "Fizz"],
            [10, ""],
            [11, ""],
            [12, "Fizz"],
            [13, ""],
            [14, ""],
            [15, "Fizz"],
            [16, ""],
            [17, ""],
            [18, "Fizz"],
            [19, ""],
            [20, ""],
            [21, "Fizz"],
            [22, ""],
        ]
    )
    def test_handle_multiples_of_three(self, i, expected):
        self.assertEqual(expected, MultipleOfThree().handle(i))

    @parameterized.expand(
        [
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, "Buzz"],
            [6, ""],
            [7, ""],
            [8, ""],
            [9, ""],
            [10, "Buzz"],
            [11, ""],
            [12, ""],
            [13, ""],
            [14, ""],
            [15, "Buzz"],
            [16, ""],
            [17, ""],
            [18, ""],
            [19, ""],
            [20, "Buzz"],
            [21, ""],
            [22, ""],
        ]
    )
    def test_handle_multiples_of_five(self, i, expected):
        self.assertEqual(expected, MultipleOfFive().handle(i))

    @parameterized.expand(
        [
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
            [6, ""],
            [7, "Whizz"],
            [8, ""],
            [9, ""],
            [10, ""],
            [11, ""],
            [12, ""],
            [13, ""],
            [14, "Whizz"],
            [15, ""],
            [16, ""],
            [17, ""],
            [18, ""],
            [19, ""],
            [20, ""],
            [21, "Whizz"],
            [22, ""],
        ]
    )
    def test_handle_multiples_of_seven(self, i, expected):
        self.assertEqual(expected, MultipleOfSeven().handle(i))

    @parameterized.expand(
        [
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""],
            [5, ""],
            [6, ""],
            [7, ""],
            [8, ""],
            [9, ""],
            [10, ""],
            [11, "Bang"],
            [12, ""],
            [13, ""],
            [14, ""],
            [15, ""],
            [16, ""],
            [17, ""],
            [18, ""],
            [19, ""],
            [20, ""],
            [21, ""],
            [22, "Bang"],
        ]
    )
    def test_handle_multiples_of_eleven(self, i, expected):
        self.assertEqual(expected, MultipleOfEleven().handle(i))
