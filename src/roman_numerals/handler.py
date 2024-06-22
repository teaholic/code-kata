from abc import ABC, abstractmethod

from src.roman_numerals.decimal_system import DecimalSystem


class Handler(ABC):
    @abstractmethod
    def can_handle(self, request: DecimalSystem) -> bool:
        pass

    @abstractmethod
    def handle(self, request: DecimalSystem, mapping) -> str:
        pass


class ExactMatchHandler(Handler):
    def can_handle(self, request: DecimalSystem) -> bool:
        res = request.get_closest_greater_distance() == 0
        if res:
            print("ExactMatchHandler")
        return res

    def handle(self, request: DecimalSystem, mapping) -> str:
        return mapping.get_roman_numeral(request.value)


class BeforeExactMatchHandler(Handler):
    def can_handle(self, request: DecimalSystem) -> bool:
        closest_greater_number_distance = request.get_closest_greater_distance()
        res = (
            closest_greater_number_distance
            == -request.get_closest_smaller_order_of_magnitude()
        )
        if res:
            print("BeforeExactMatchHandler")
        return res

    def handle(self, request: DecimalSystem, mapping) -> str:
        second_closest_smaller_number = request.get_second_smaller_number()
        closest_greater_number = request.get_closest_greater_number()
        return mapping.get_roman_numeral(
            second_closest_smaller_number
        ) + mapping.get_roman_numeral(closest_greater_number)


class AfterSmallerMatchHandler(Handler):
    def can_handle(self, request: DecimalSystem) -> bool:
        closest_smaller_number = request.get_closest_smaller_number()
        res = request.value % closest_smaller_number == 0
        if res:
            print("AfterSmallerMatchHandler")
        return res

    def handle(self, request: DecimalSystem, mapping) -> str:
        closest_smaller_number = request.get_closest_smaller_number()
        return mapping.get_roman_numeral(closest_smaller_number) * round(
            request.value / closest_smaller_number
        )


class BeforeGreaterMatchHandler(Handler):
    def can_handle(self, request: DecimalSystem) -> bool:
        res = True
        if res:
            print("BeforeGreaterMatchHandler")
        return res

    def handle(self, request: DecimalSystem, mapping) -> str:
        closest_smaller_number = request.get_closest_smaller_number()
        second_closest_smaller_number = request.get_second_smaller_number()
        roman_numeral_substring = mapping.get_roman_numeral(
            second_closest_smaller_number
        ) * round(
            (request.value - closest_smaller_number) / second_closest_smaller_number
        )
        return (
            mapping.get_roman_numeral(closest_smaller_number) + roman_numeral_substring
        )


class ErrorHandler(Handler):
    def can_handle(self, request: DecimalSystem) -> bool:
        return True

    def handle(self, request: DecimalSystem, mapping) -> str:
        return f"Unsupported request {request.value}"
