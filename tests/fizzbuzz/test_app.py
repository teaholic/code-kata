import unittest

from parameterized import parameterized


class FizzBuzzApp:

    def run(self, input:int):
        return "Fizz"



class TestFizzBuzzApp(unittest.TestCase):

    @parameterized.expand([
        [3, "Fizz"],
    ])
    def test_run(self, input, expected):
        actual = FizzBuzzApp().run(input)
        self.assertEqual(actual, expected)
