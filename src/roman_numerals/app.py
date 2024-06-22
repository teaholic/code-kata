from src.roman_numerals.decimal_system import DecimalSystem
from src.roman_numerals.mapping import ArabicMappingService
from src.roman_numerals.handler import (
    ExactMatchHandler,
    BeforeExactMatchHandler,
    AfterSmallerMatchHandler,
    ErrorHandler,
    BeforeGreaterMatchHandler,
)


class NumeralConversionApp:
    def __init__(self):
        self.handlers = [
            ExactMatchHandler(),
            BeforeExactMatchHandler(),
            AfterSmallerMatchHandler(),
            BeforeGreaterMatchHandler(),
            ErrorHandler(),
        ]

    def convert(self, arabic_number: int) -> str:
        roman_numeral_sequence = [1, 5, 10, 50, 100, 500, 1000]
        return self._convert(
            DecimalSystem(arabic_number, roman_numeral_sequence),
            ArabicMappingService(roman_numeral_sequence),
        )

    def _convert(self, request: DecimalSystem, mapping: ArabicMappingService) -> str:
        for handler in self.handlers:
            if handler.can_handle(request):
                return handler.handle(request, mapping)
