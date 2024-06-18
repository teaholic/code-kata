from src.roman_numerals.numeral_gateway import NumeralGateway
from src.roman_numerals.model import RomanToArabicMappingService


class NumeralApp:
    def convert(self, number: int) -> str:
        return NumeralConversion(number).run()


class ArabicNumber:
    def __init__(self, number):
        self.number = number
        self.api = NumeralGateway(number)

    def has_one_digit_roman_match(self) -> bool:
        return self.api.get_closest_greater_distance() == 0

    def is_smaller_than_four(self) -> bool:
        closest_smaller_number = self.api.get_closest_smaller_number()
        closest_greater_number = self.api.get_closest_greater_number()
        closest_greater_number_distance = self.api.get_closest_greater_distance()
        return (self.number % closest_smaller_number == 0) & (
                closest_greater_number + closest_greater_number_distance != self.number
            )

    def case_3(self) -> bool:
        closest_greater_number_distance = self.api.get_closest_greater_distance()
        return (
            closest_greater_number_distance
            == -self.api.get_closest_smaller_order_of_magnitude()
        )

    def case_4(self) -> bool:
        closest_smaller_number = self.api.get_closest_smaller_number()
        return self.number % closest_smaller_number == 0



class NumeralConversion:
    def __init__(self, number):
        self.number = number
        self.mapping_service = RomanToArabicMappingService()
        self.api = NumeralGateway(number)
        self.number_api = ArabicNumber(number)

    def run(self) -> str:
        if self.number_api.has_one_digit_roman_match():  # closest_greater_number_distance == 0:
            return self.mapping_service.get_roman_numeral(self.number)
        elif self.number_api.is_smaller_than_four():  # number < 4:
            closest_smaller_number = self.api.get_closest_smaller_number()
            return self.mapping_service.get_roman_numeral(
                closest_smaller_number
            ) * round(self.number / closest_smaller_number)
        elif self.number_api.case_3():
            return self._convert_case_3()
        elif self.number_api.case_4():
            closest_smaller_number = self.api.get_closest_smaller_number()
            return self.mapping_service.get_roman_numeral(
                closest_smaller_number
            ) * round(self.number / closest_smaller_number)
        else:
            closest_smaller_number = self.api.get_closest_smaller_number()
            second_closest_smaller_number = NumeralGateway(
                closest_smaller_number - 1,
            ).get_closest_smaller_number()
            roman_numeral_substring = self.mapping_service.get_roman_numeral(
                second_closest_smaller_number
            ) * round(
                (self.number - closest_smaller_number)
                / second_closest_smaller_number
            )
            return (
                self.mapping_service.get_roman_numeral(
                    closest_smaller_number
                )
                + roman_numeral_substring
            )

    def _convert_case_3(self):
        closest_smaller_number = self.api.get_closest_smaller_number()
        if (
                closest_smaller_number
                == self.api.get_closest_smaller_order_of_magnitude()
        ):
            second_closest_smaller_number = NumeralGateway(
                closest_smaller_number
            ).get_closest_smaller_number()
        else:
            second_closest_smaller_number = NumeralGateway(
                closest_smaller_number - 1
            ).get_closest_smaller_number()
        print(second_closest_smaller_number)
        closest_greater_number = self.api.get_closest_greater_number()
        return self.mapping_service.get_roman_numeral(
            second_closest_smaller_number
        ) + self.mapping_service.get_roman_numeral(closest_greater_number)
