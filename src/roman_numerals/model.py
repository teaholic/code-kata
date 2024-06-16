from enum import Enum
from typing import List


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
