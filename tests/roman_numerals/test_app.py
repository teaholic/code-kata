import unittest
from enum import Enum

from parameterized import parameterized


class RomanNumerals(Enum):
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100


class MyRomanNumeralsApp:
    def convert(self, number: int) -> str:
        residues = [number - n.value for n in RomanNumerals]
        min_residue = min([n for n in residues if n >= 0])
        if min_residue == 0: # Number matches a single char roman numeral
            min_residue_index = residues.index(min_residue)
            exact_match_pos = [num for pos, num in enumerate([n.value for n in RomanNumerals]) if pos == min_residue_index][0]
            return [n.name for n in RomanNumerals if n.value == exact_match_pos][0]
        else:
            return "O"


class RomanNumeralsApp:
    def convert(self, number: int) -> str:
        if number < 9:
            return self._convert_unit(number)
        elif number <= 10:
            subtract = "I" if 10 - number == 1 else ""
            return subtract + "X"
        elif number < 20:
            unit = number % 10
            roman_unit = self._convert_unit(unit)
            tens = "X"
            return tens + roman_unit
        elif number < 90:
            return self._convert_tens(number)
        elif number == 90:
            return "XC"
        else:
            raise Exception("Unable to convert " + str(number))

    def _convert_unit(self, number: int) -> str:
        if number <= 3:
            return "I" * number
        elif number < 5:
            return "IV"
        elif number == 5:
            return "V"
        elif number < (10 - 1):
            add = "I" * (number - 5)
            return "V" + add

    def _convert_tens(self, number: int) -> str:
        if number <= 30:
            return "X" * round(number / 10)
        elif number < 50:
            return "XL"
        elif number == 50:
            return "L"
        elif number < (100 - 10):
            add = "X" * round((number - 50) / 10)
            return "L" + add


class TestRomanNumeralsApp(unittest.TestCase):
    @parameterized.expand(
        [
            [0, ""],
            [1, "I"],
            [2, "II"],
            [3, "III"],
            [4, "IV"],
            [5, "V"],
            [6, "VI"],
            [7, "VII"],
            [8, "VIII"],
            [9, "IX"],
            [10, "X"],
            [20, "XX"],
            [30, "XXX"],
            [40, "XL"],
            [50, "L"],
            [60, "LX"],
            [70, "LXX"],
            [80, "LXXX"],
            [90, "XC"],
        ]
    )
    def test_convert_success(self, number, expected):

        self.assertEqual(MyRomanNumeralsApp().convert(number), expected)

    def test_convert_error(self):

        with self.assertRaises(Exception):
            RomanNumeralsApp().convert(1000)
