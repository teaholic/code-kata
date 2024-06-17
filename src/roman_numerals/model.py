from enum import Enum
from typing import List


class RomanToArabicMapping(Enum):
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000


class RomanToArabicMappingService:

    def __init__(self):
        self.enumerated_numeral_sequence = list(enumerate([n.value for n in RomanToArabicMapping]))

    def get_roman_numeral(self, arabic_numeral) -> str:
        return [n.name for n in RomanToArabicMapping if n.value == arabic_numeral][0]

    def get_order_of_magnitude_index(self, index: int) -> int:
        return (
                index
                if index % 2 == 0
                else index - 1
            )

    def get_number_from(self, index: int) -> int:
        return [
            num
            for pos, num in self.enumerated_numeral_sequence
            if pos == index
        ][0]

    def get_closest_smaller_order_of_magnitude(self, index: int) -> int:
        closest_smaller_order_of_magnitude_index = self.get_order_of_magnitude_index(index)
        return self.get_number_from(closest_smaller_order_of_magnitude_index)

    def get_numeral_sequence(self) -> List[int]:
        return [n.value for n in RomanToArabicMapping]