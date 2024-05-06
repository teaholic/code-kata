import unittest

from parameterized import parameterized

class Input:
    def __init__(self, value):
        self.value = value

    def is_multiple_of_three(self):
        return self.value % 3 == 0

    def is_multiple_of_five(self):
        return self.value % 5 == 0

    def is_multiple_of_three_and_five(self):
        return (self.value % 3 == 0) & (self.value % 5 == 0)


class FizzBuzzApp:

    def run(self, value:int):
        my_input = Input(value)
        if my_input.is_multiple_of_three_and_five():
            return "FizzBuzz"
        elif my_input.is_multiple_of_three():
            return "Fizz"
        elif my_input.is_multiple_of_five():
            return "Buzz"
        return value



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
