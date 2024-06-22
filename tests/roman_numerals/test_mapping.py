import unittest
from parameterized import parameterized

from src.roman_numerals.mapping import ArabicMappingService


class TestArabicRomanMappingService(unittest.TestCase):
    @parameterized.expand(
        [(1, "I"), (5, "V"), (10, "X"), (50, "L"), (100, "C"), (500, "D"), (1000, "M")]
    )
    def test_get_roman_numeral(self, number, expected):
        self.assertEqual(
            ArabicMappingService([1, 5, 10, 50, 100, 500, 1000]).get_roman_numeral(
                number
            ),
            expected,
        )
