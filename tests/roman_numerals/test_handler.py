import unittest

from parameterized import parameterized

from src.roman_numerals.decimal_system import DecimalSystem
from src.roman_numerals.mapping import ArabicMappingService
from src.roman_numerals.handler import ExactMatchHandler


class TestExactMatchHandler(unittest.TestCase):
    numeral_sequence = [1, 5, 10, 50, 100, 500, 1000]

    @parameterized.expand(
        [
            (1, True),
            (2, False),
            (3, False),
            (4, False),
            (5, True),
            (10, True),
            (50, True),
            (100, True),
            (500, True),
            (1000, True),
        ]
    )
    def test_can_handle(self, number, expected):
        self.assertEqual(
            ExactMatchHandler().can_handle(
                request=DecimalSystem(number, self.numeral_sequence)
            ),
            expected,
        )

    @parameterized.expand(
        [(1, "I"), (5, "V"), (10, "X"), (50, "L"), (100, "C"), (500, "D"), (1000, "M"),]
    )
    def test_handle(self, number, expected):
        self.assertEqual(
            ExactMatchHandler().handle(
                request=DecimalSystem(number, self.numeral_sequence),
                mapping=ArabicMappingService(self.numeral_sequence),
            ),
            expected,
        )
