import unittest

from parameterized import parameterized


class FizzBuzzApp:

    def run(self, input:int):
        if input % 3 == 0:
            return "Fizz"
        return input



class TestFizzBuzzApp(unittest.TestCase):

    @parameterized.expand([
        [1, 1],
        [2, 2],
        [3, "Fizz"],
    ])
    def test_run(self, input, expected):
        actual = FizzBuzzApp().run(input)
        self.assertEqual(actual, expected)
