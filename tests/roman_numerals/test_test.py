import unittest
from enum import Enum
from typing import List

from parameterized import parameterized


class NumeralMapping(Enum):
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100


class NumeralMappingService:

    def get_roman_numeral(self, number) -> str:
        return [n.name for n in NumeralMapping if n.value == number][0]


class NumeralService:
    def __init__(self, number: int, numeral_sequence: List[int]):
        self.number = number
        self.numeral_sequence = numeral_sequence
        self.residues = [self.number - n.value for n in NumeralMapping]

    def get_closest_smaller_numeral_number(self) -> int:
        closest_smaller_residue = min([n for n in self.residues if n >= 0])
        closest_smaller_residue_index = self.residues.index(closest_smaller_residue)
        return [num for pos, num in enumerate([n for n in self.numeral_sequence]) if pos == closest_smaller_residue_index][0]

    def get_closest_greater_numeral_number(self) -> int:
        closest_greater_residue_index = self.residues.index(self.get_closest_greater_number_residue())
        return [num for pos, num in enumerate([n for n in self.numeral_sequence]) if pos == closest_greater_residue_index][0]

    def get_closest_greater_number_residue(self) -> int:
        return max([n for n in self.residues if n <= 0])

    def get_closest_smaller_tenth_number(self) -> int:
        closest_smaller_residue = min([n for n in self.residues if n >= 0])
        closest_smaller_tenth_index = self.residues.index(closest_smaller_residue) if self.residues.index(closest_smaller_residue) % 2 == 0 else self.residues.index(closest_smaller_residue) - 1
        print(closest_smaller_tenth_index)
        return [num for pos, num in enumerate([n for n in self.numeral_sequence]) if pos == closest_smaller_tenth_index][0]


class TestNumeralService(unittest.TestCase):

    @parameterized.expand(
        [
            (1, 0),
            (2, -3),
            (3, -2),
            (4, -1),
            (5, 0),
        ]
    )
    def test_get_closest_greater_number_residue(self, number, expected):
        self.assertEqual(NumeralService(number, [n.value for n in NumeralMapping]).get_closest_greater_number_residue(), expected)

    @parameterized.expand(
        [
            (1, 1),
            (2, 1),
            (3, 1),
            (4, 1),
            (5, 5),
        ]
    )
    def test_get_closest_smaller_numeral_number(self, number, expected):
        self.assertEqual(NumeralService(number, [n.value for n in NumeralMapping]).get_closest_smaller_numeral_number(), expected)

    @parameterized.expand(
        [
            (1, 1),
            (2, 5),
            (3, 5),
            (4, 5),
            (5, 5),
        ]
    )
    def test_get_closest_greater_numeral_number(self, number, expected):
        self.assertEqual(NumeralService(number, [n.value for n in NumeralMapping]).get_closest_greater_numeral_number(), expected)

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
        self.assertEqual(NumeralService(number, [n.value for n in NumeralMapping]).get_closest_smaller_tenth_number(), expected)


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
        self.assertEqual(NumeralMappingService().get_roman_numeral(number), expected)


class NumeralApp:
    def __init__(self):
        self.mapping_service = NumeralMappingService()

    def convert(self, number:int) -> str:
        closest_greater_number_residue = NumeralService(number, [n.value for n in NumeralMapping]).get_closest_greater_number_residue()
        if closest_greater_number_residue == 0:
            return self.mapping_service.get_roman_numeral(number)
        else:
            closest_smaller_number = NumeralService(number, [n.value for n in NumeralMapping]).get_closest_smaller_numeral_number()
            closest_greater_number = NumeralService(number, [n.value for n in NumeralMapping]).get_closest_greater_numeral_number()
            if (number % closest_smaller_number == 0) & (closest_greater_number + closest_greater_number_residue != number):#number < 4:
                return self.mapping_service.get_roman_numeral(closest_smaller_number) * round(number / closest_smaller_number)
            else:
                if closest_greater_number_residue == - NumeralService(number, [n.value for n in NumeralMapping]).get_closest_smaller_tenth_number():
                    if closest_smaller_number == NumeralService(number, [n.value for n in NumeralMapping]).get_closest_smaller_tenth_number():
                        second_closest_smaller_number = NumeralService(
                            closest_smaller_number, [n.value for n in NumeralMapping]).get_closest_smaller_numeral_number()
                    else:
                        second_closest_smaller_number = NumeralService(
                            closest_smaller_number - 1, [n.value for n in NumeralMapping]).get_closest_smaller_numeral_number()
                    print(second_closest_smaller_number)
                    closest_greater_number = NumeralService(number, [n.value for n in NumeralMapping]).get_closest_greater_numeral_number()
                    return self.mapping_service.get_roman_numeral(second_closest_smaller_number) + self.mapping_service.get_roman_numeral(closest_greater_number)
                else:
                    if number % closest_smaller_number == 0:
                        return self.mapping_service.get_roman_numeral(closest_smaller_number) * round(
                            number / closest_smaller_number)
                    else:
                        second_closest_smaller_number = NumeralService(
                            closest_smaller_number - 1, [n.value for n in NumeralMapping]).get_closest_smaller_numeral_number()
                        print(second_closest_smaller_number)
                        roman_numeral_substring = self.mapping_service.get_roman_numeral(second_closest_smaller_number) * round((number - closest_smaller_number)/second_closest_smaller_number)
                        return self.mapping_service.get_roman_numeral(closest_smaller_number) + roman_numeral_substring


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

