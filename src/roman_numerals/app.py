from src.roman_numerals.model import NumeralMappingService, NumeralService, NumeralMapping


class NumeralApp:
    def __init__(self):
        self.mapping_service = NumeralMappingService()

    def convert(self, number:int) -> str:
        closest_greater_number_residue = NumeralService(number, [n.value for n in NumeralMapping]).get_closest_greater_number_residue()
        if closest_greater_number_residue == 0:
            return self.mapping_service.get_roman_numeral(number)
        else:
            closest_smaller_number = NumeralService(number, [n.value for n in NumeralMapping]).get_closest_smaller_numeral_number()
            closest_greater_number = NumeralService(number, [n.value for n in NumeralMapping]).get_closest_greater_numeral_number()
            if (number % closest_smaller_number == 0) & (closest_greater_number + closest_greater_number_residue != number):#number < 4:
                return self.mapping_service.get_roman_numeral(closest_smaller_number) * round(number / closest_smaller_number)
            else:
                if closest_greater_number_residue == - NumeralService(number, [n.value for n in NumeralMapping]).get_closest_smaller_tenth_number():
                    if closest_smaller_number == NumeralService(number, [n.value for n in NumeralMapping]).get_closest_smaller_tenth_number():
                        second_closest_smaller_number = NumeralService(
                            closest_smaller_number, [n.value for n in NumeralMapping]).get_closest_smaller_numeral_number()
                    else:
                        second_closest_smaller_number = NumeralService(
                            closest_smaller_number - 1, [n.value for n in NumeralMapping]).get_closest_smaller_numeral_number()
                    print(second_closest_smaller_number)
                    closest_greater_number = NumeralService(number, [n.value for n in NumeralMapping]).get_closest_greater_numeral_number()
                    return self.mapping_service.get_roman_numeral(second_closest_smaller_number) + self.mapping_service.get_roman_numeral(closest_greater_number)
                else:
                    if number % closest_smaller_number == 0:
                        return self.mapping_service.get_roman_numeral(closest_smaller_number) * round(
                            number / closest_smaller_number)
                    else:
                        second_closest_smaller_number = NumeralService(
                            closest_smaller_number - 1, [n.value for n in NumeralMapping]).get_closest_smaller_numeral_number()
                        print(second_closest_smaller_number)
                        roman_numeral_substring = self.mapping_service.get_roman_numeral(second_closest_smaller_number) * round((number - closest_smaller_number)/second_closest_smaller_number)
                        return self.mapping_service.get_roman_numeral(closest_smaller_number) + roman_numeral_substring
