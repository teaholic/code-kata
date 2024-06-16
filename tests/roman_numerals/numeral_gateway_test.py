import unittest

from parameterized import parameterized

from src.roman_numerals.model import RomanToArabicMapping
from src.roman_numerals.numeral_gateway import NumeralGateway


class TestNumeralGateway(unittest.TestCase):
    number_sequence = [n.value for n in RomanToArabicMapping]

    @parameterized.expand(
        [(1, 0), (2, -3), (3, -2), (4, -1), (5, 0),]
    )
    def test_get_closest_greater_number_distance(self, number, expected):
        self.assertEqual(
            NumeralGateway(number, self.number_sequence).get_closest_greater_distance(),
            expected,
        )

    @parameterized.expand(
        [(1, 1), (2, 1), (3, 1), (4, 1), (5, 5),]
    )
    def test_get_closest_smaller_numeral_number(self, number, expected):
        self.assertEqual(
            NumeralGateway(number, self.number_sequence).get_closest_smaller_number(),
            expected,
        )

    @parameterized.expand(
        [(1, 1), (2, 5), (3, 5), (4, 5), (5, 5),]
    )
    def test_get_closest_greater_numeral_number(self, number, expected):
        self.assertEqual(
            NumeralGateway(number, self.number_sequence).get_closest_greater_number(),
            expected,
        )

    @parameterized.expand(
        [
            (1, 1),
            (2, 1),
            (3, 1),
            (4, 1),
            (5, 1),
            (6, 1),
            (7, 1),
            (8, 1),
            (9, 1),
            (10, 10),
            (20, 10),
            (30, 10),
            (40, 10),
            (50, 10),
            (90, 10),
            (100, 100),
        ]
    )
    def test_get_closest_smaller_tenth_number(self, number, expected):
        self.assertEqual(
            NumeralGateway(number, self.number_sequence).get_closest_smaller_tenth(),
            expected,
        )
