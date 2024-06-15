import unittest
from enum import Enum

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
    def __init__(self, number: int):
        self.number = number
        self.residues = [self.number - n.value for n in NumeralMapping]

    def get_closest_smaller_numeral_number(self) -> int:
        closest_smaller_residue = min([n for n in self.residues if n >= 0])
        closest_smaller_residue_index = self.residues.index(closest_smaller_residue)
        return [num for pos, num in enumerate([n.value for n in NumeralMapping]) if pos == closest_smaller_residue_index][0]

    def get_closest_greater_numeral_number(self) -> int:
        closest_greater_residue_index = self.residues.index(self.get_closest_greater_number_residue())
        return [num for pos, num in enumerate([n.value for n in NumeralMapping]) if pos == closest_greater_residue_index][0]

    def get_closest_greater_number_residue(self) -> int:
        return max([n for n in self.residues if n <= 0])


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
        self.assertEqual(NumeralService(number).get_closest_greater_number_residue(), expected)

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
        self.assertEqual(NumeralService(number).get_closest_smaller_numeral_number(), expected)

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
        self.assertEqual(NumeralService(number).get_closest_greater_numeral_number(), expected)


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
        closest_greater_number_residue = NumeralService(number).get_closest_greater_number_residue()
        if closest_greater_number_residue == 0:
            return self.mapping_service.get_roman_numeral(number)
        else:
            if number < 4:
                closest_smaller_number = NumeralService(number).get_closest_smaller_numeral_number()
                return self.mapping_service.get_roman_numeral(closest_smaller_number) * round(number / closest_smaller_number)
            else:
                closest_smaller_number = NumeralService(number).get_closest_smaller_numeral_number()
                print(closest_smaller_number)
                print(NumeralService(number).get_closest_greater_number_residue())
                if NumeralService(number).get_closest_greater_number_residue() == -1:
                    if closest_smaller_number == 1:
                        second_closest_smaller_number = NumeralService(
                            closest_smaller_number).get_closest_smaller_numeral_number()
                    else:
                        second_closest_smaller_number = NumeralService(
                            closest_smaller_number - 1).get_closest_smaller_numeral_number()
                    print(second_closest_smaller_number)
                    closest_greater_number = NumeralService(number).get_closest_greater_numeral_number()
                    return self.mapping_service.get_roman_numeral(second_closest_smaller_number) + self.mapping_service.get_roman_numeral(closest_greater_number)
                else:
                    print("Corner case")
                    if number % closest_smaller_number == 0:
                        return self.mapping_service.get_roman_numeral(closest_smaller_number) * round(
                            number / closest_smaller_number)
                    else:
                        second_closest_smaller_number = NumeralService(
                            closest_smaller_number - 1).get_closest_smaller_numeral_number()
                        roman_numeral_substring = self.mapping_service.get_roman_numeral(second_closest_smaller_number) * (number - closest_smaller_number)
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
        ]
    )
    def test_convert(self, number, expected):
        self.assertEqual(NumeralApp().convert(number), expected)

