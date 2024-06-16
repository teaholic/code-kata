import unittest
from parameterized import parameterized

from src.roman_numerals.model import RomanToArabicMappingService


class TestNumeralMappingService(unittest.TestCase):

    @parameterized.expand(
        [
            (1, "I"),
            (5, "V"),
            (10, "X"),
            (50, "L"),
            (100, "C"),
        ]
    )
    def test_get_roman_numeral(self, number, expected):
        self.assertEqual(RomanToArabicMappingService().get_roman_numeral(number), expected)
