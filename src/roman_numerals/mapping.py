from enum import Enum


class RomanToArabicMapping(Enum):
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000


class ArabicRomanMappingService:
    def __init__(self):
        self.enumerated_numeral_sequence = list(
            enumerate([n.value for n in RomanToArabicMapping])
        )

    def get_roman_numeral(self, arabic_numeral) -> str:
        return [n.name for n in RomanToArabicMapping if n.value == arabic_numeral][0]
