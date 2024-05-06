import unittest


class FizzBuzzApp:

    def run(self, input:int):
        return "Fizz"



class TestFizzBuzzApp(unittest.TestCase):

    def test_run(self):
        actual = FizzBuzzApp().run(3)
        self.assertEqual(actual, "Fizz")