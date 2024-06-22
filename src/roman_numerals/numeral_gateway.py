from functools import cached_property

from roman_numerals.model import RomanToArabicMappingService


class NumeralDescriptor:
    def __init__(self, number: int):
        self.number = number
        self.service = RomanToArabicMappingService()
        self.distances = [number - n for n in self.service.get_numeral_sequence()]

    @cached_property
    def value(self) -> int:
        return self.number

    def get_closest_smaller_number(self) -> int:
        closest_smaller_distance = min([n for n in self.distances if n >= 0])
        closest_smaller_distance_index = self.distances.index(closest_smaller_distance)
        return self.service.get_number_from(closest_smaller_distance_index)

    def get_closest_greater_number(self) -> int:
        closest_greater_distance_index = self.distances.index(
            self.get_closest_greater_distance()
        )
        return self.service.get_number_from(closest_greater_distance_index)

    def get_closest_greater_distance(self) -> int:
        return max([n for n in self.distances if n <= 0])

    def get_closest_smaller_order_of_magnitude(self) -> int:
        closest_smaller_distance = min([n for n in self.distances if n >= 0])
        return self.service.get_closest_smaller_order_of_magnitude(
            self.distances.index(closest_smaller_distance)
        )
