from enum import Enum


class RomanToArabicMapping(Enum):
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000


class ArabicMappingService:
    def __init__(self, numeral_sequence):
        self.roman_numerals = ["I", "V", "X", "L", "C", "D", "M"]
        self.mapping = list(zip(numeral_sequence, self.roman_numerals))

    def get_roman_numeral(self, arabic_numeral) -> str:
        return [r for n, r in self.mapping if n == arabic_numeral][0]
