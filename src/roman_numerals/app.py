from src.roman_numerals.service import ArabicToRomanNumeralService
from src.roman_numerals.decimal_system import DecimalSystem
from src.roman_numerals.mapping import ArabicRomanMappingService, RomanToArabicMapping


class NumeralConversionApp:
    def convert(self, arabic_number: int) -> str:
        roman_numeral_sequence = [n.value for n in RomanToArabicMapping]
        return ArabicToRomanNumeralService().convert(
            DecimalSystem(arabic_number, roman_numeral_sequence),
            ArabicRomanMappingService(),
        )
