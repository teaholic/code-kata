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
