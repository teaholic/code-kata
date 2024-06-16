import unittest

from parameterized import parameterized

from src.roman_numerals.app import NumeralApp


class TestNumeralApp(unittest.TestCase):
    @parameterized.expand(
        [
            (1, "I"),
            (2, "II"),
            (3, "III"),
            (4, "IV"),
            (5, "V"),
            (6, "VI"),
            (7, "VII"),
            (8, "VIII"),
            (9, "IX"),
            (10, "X"),
            (20, "XX"),
            (30, "XXX"),
            (40, "XL"),
            (50, "L"),
            (60, "LX"),
            (70, "LXX"),
            (80, "LXXX"),
            (90, "XC"),
            (100, "C"),
        ]
    )
    def test_convert(self, number, expected):
        self.assertEqual(NumeralApp().convert(number), expected)
