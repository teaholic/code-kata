from roman_numerals.decimal_system import DecimalSystem
from src.roman_numerals.handler import (
    ExactMatchHandler,
    BeforeExactMatchHandler,
    AfterSmallerMatchHandler,
    ErrorHandler,
    BeforeGreaterMatchHandler,
)


class ArabicToRomanNumeralService:
    def __init__(self):
        self.handlers = [
            ExactMatchHandler(),
            BeforeExactMatchHandler(),
            AfterSmallerMatchHandler(),
            BeforeGreaterMatchHandler(),
            ErrorHandler(),
        ]

    def convert(self, request: DecimalSystem, mapping) -> str:
        for handler in self.handlers:
            if handler.can_handle(request):
                return handler.handle(request, mapping)
