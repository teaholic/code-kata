import unittest
from parameterized import parameterized

from src.roman_numerals.mapping import ArabicRomanMappingService


class TestArabicRomanMappingService(unittest.TestCase):
    @parameterized.expand(
        [(1, "I"), (5, "V"), (10, "X"), (50, "L"), (100, "C"), (500, "D"), (1000, "M")]
    )
    def test_get_roman_numeral(self, number, expected):
        self.assertEqual(
            ArabicRomanMappingService().get_roman_numeral(number), expected
        )
