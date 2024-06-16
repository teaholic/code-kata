from src.roman_numerals.numeral_gateway import NumeralGateway
from src.roman_numerals.model import RomanToArabicMappingService, RomanToArabicMapping


class NumeralApp:
    def __init__(self):
        self.mapping_service = RomanToArabicMappingService()

    def convert(self, number:int) -> str: # Todo: extract and model NumeralGateway calculations
        closest_greater_number_residue = NumeralGateway(number, [n.value for n in RomanToArabicMapping]).get_closest_greater_residue()
        if closest_greater_number_residue == 0:
            return self.mapping_service.get_roman_numeral(number)
        else:
            closest_smaller_number = NumeralGateway(number, [n.value for n in RomanToArabicMapping]).get_closest_smaller_number()
            closest_greater_number = NumeralGateway(number, [n.value for n in RomanToArabicMapping]).get_closest_greater_number()
            if (number % closest_smaller_number == 0) & (closest_greater_number + closest_greater_number_residue != number):#number < 4:
                return self.mapping_service.get_roman_numeral(closest_smaller_number) * round(number / closest_smaller_number)
            else:
                if closest_greater_number_residue == - NumeralGateway(number, [n.value for n in RomanToArabicMapping]).get_closest_smaller_tenth():
                    if closest_smaller_number == NumeralGateway(number, [n.value for n in RomanToArabicMapping]).get_closest_smaller_tenth():
                        second_closest_smaller_number = NumeralGateway(
                            closest_smaller_number, [n.value for n in RomanToArabicMapping]).get_closest_smaller_number()
                    else:
                        second_closest_smaller_number = NumeralGateway(
                            closest_smaller_number - 1, [n.value for n in RomanToArabicMapping]).get_closest_smaller_number()
                    print(second_closest_smaller_number)
                    closest_greater_number = NumeralGateway(number, [n.value for n in RomanToArabicMapping]).get_closest_greater_number()
                    return self.mapping_service.get_roman_numeral(second_closest_smaller_number) + self.mapping_service.get_roman_numeral(closest_greater_number)
                else:
                    if number % closest_smaller_number == 0:
                        return self.mapping_service.get_roman_numeral(closest_smaller_number) * round(
                            number / closest_smaller_number)
                    else:
                        second_closest_smaller_number = NumeralGateway(
                            closest_smaller_number - 1, [n.value for n in RomanToArabicMapping]).get_closest_smaller_number()
                        print(second_closest_smaller_number)
                        roman_numeral_substring = self.mapping_service.get_roman_numeral(second_closest_smaller_number) * round((number - closest_smaller_number)/second_closest_smaller_number)
                        return self.mapping_service.get_roman_numeral(closest_smaller_number) + roman_numeral_substring
