from src.roman_numerals.handler import (
    ExactMatchHandler,
    BeforeExactMatchHandler,
    AfterSmallerMatchHandler,
    ArabicToRomanNumeralService,
    ErrorHandler,
    BeforeGreaterMatchHandler,
)
from src.roman_numerals.numeral_gateway import NumeralDescriptor
from src.roman_numerals.model import RomanToArabicMappingService


class NumeralConversionApp:
    def convert(self, arabic_number: int) -> str:
        handlers = [
            ExactMatchHandler(),
            BeforeExactMatchHandler(),
            AfterSmallerMatchHandler(),
            BeforeGreaterMatchHandler(),
            ErrorHandler(),
        ]
        return ArabicToRomanNumeralService(handlers).convert(
            NumeralDescriptor(arabic_number), RomanToArabicMappingService()
        )
