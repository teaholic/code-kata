from enum import Enum
from typing import List


class RomanToArabicMapping(Enum):
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100


class RomanToArabicMappingService:

    def get_roman_numeral(self, arabic_numeral) -> str:
        return [n.name for n in RomanToArabicMapping if n.value == arabic_numeral][0]


class NumeralService:
    def __init__(self, number: int, numeral_sequence: List[int]):
        self.number = number
        self.numeral_sequence = numeral_sequence

    def get_closest_smaller_number(self) -> int:
        closest_smaller_residue = min([n for n in self.__get_residues(self.number, self.numeral_sequence) if n >= 0])
        closest_smaller_residue_index = self.__get_residues(self.number, self.numeral_sequence).index(closest_smaller_residue)
        return [num for pos, num in enumerate([n for n in self.numeral_sequence]) if pos == closest_smaller_residue_index][0]

    def get_closest_greater_number(self) -> int:
        closest_greater_residue_index = self.__get_residues(self.number, self.numeral_sequence).index(self.get_closest_greater_residue())
        return [num for pos, num in enumerate([n for n in self.numeral_sequence]) if pos == closest_greater_residue_index][0]

    def get_closest_greater_residue(self) -> int:
        return max([n for n in self.__get_residues(self.number, self.numeral_sequence) if n <= 0])

    def get_closest_smaller_tenth(self) -> int:
        closest_smaller_residue = min([n for n in self.__get_residues(self.number, self.numeral_sequence) if n >= 0])
        closest_smaller_tenth_index = self.__get_residues(self.number, self.numeral_sequence).index(closest_smaller_residue) if self.__get_residues(self.number, self.numeral_sequence).index(closest_smaller_residue) % 2 == 0 else self.__get_residues(self.number, self.numeral_sequence).index(closest_smaller_residue) - 1
        print(closest_smaller_tenth_index)
        return [num for pos, num in enumerate([n for n in self.numeral_sequence]) if pos == closest_smaller_tenth_index][0]

    def __get_residues(self, number:int, numeral_sequence: List[int]) -> List[int]:
        return [number - n for n in numeral_sequence]