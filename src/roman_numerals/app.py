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


class NumeralConversion:
    def __init__(self, number):
        self.number = number
        self.mapping_service = RomanToArabicMappingService()
        self.api = NumeralGateway(number)
        self.number_api = ArabicNumber(number)

    def run(self) -> str:
        closest_greater_number_distance = self.api.get_closest_greater_distance()
        if (
            self.number_api.has_one_digit_roman_match()
        ):  # closest_greater_number_distance == 0:
            return self.mapping_service.get_roman_numeral(self.number)
        else:
            closest_smaller_number = self.api.get_closest_smaller_number()
            closest_greater_number = self.api.get_closest_greater_number()
            if (self.number % closest_smaller_number == 0) & (
                closest_greater_number + closest_greater_number_distance != self.number
            ):  # number < 4:
                return self.mapping_service.get_roman_numeral(
                    closest_smaller_number
                ) * round(self.number / closest_smaller_number)
            else:
                if (
                    closest_greater_number_distance
                    == -self.api.get_closest_smaller_order_of_magnitude()
                ):
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
                else:
                    if self.number % closest_smaller_number == 0:
                        return self.mapping_service.get_roman_numeral(
                            closest_smaller_number
                        ) * round(self.number / closest_smaller_number)
                    else:
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
