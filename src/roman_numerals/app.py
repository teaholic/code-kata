from src.roman_numerals.handler import (
    ExactMatchHandler,
    BeforeExactMatchHandler,
    AfterSmallerMatchHandler,
    ArabicToRomanNumeralService,
    ErrorHandler,
    BeforeGreaterMatchHandler,
)
from src.roman_numerals.numeral_gateway import NumeralDescriptor
from src.roman_numerals.model import RomanToArabicMappingService, RomanToArabicMapping


class NumeralConversionApp:
    def convert(self, arabic_number: int) -> str:
        handlers = [
            ExactMatchHandler(),
            BeforeExactMatchHandler(),
            AfterSmallerMatchHandler(),
            BeforeGreaterMatchHandler(),
            ErrorHandler(),
        ]
        roman_numeral_sequence = [n.value for n in RomanToArabicMapping]
        return ArabicToRomanNumeralService(handlers).convert(
            NumeralDescriptor(arabic_number, roman_numeral_sequence),
            RomanToArabicMappingService(),
        )
