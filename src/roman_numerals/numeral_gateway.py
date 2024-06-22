from functools import cached_property
from typing import List


class NumeralDescriptor:
    def __init__(self, number: int, numeral_sequence: List[int]):
        self.number = number
        self.numeral_sequence = numeral_sequence
        self.distances = [number - n for n in numeral_sequence]
        self.enumerated_numeral_sequence = list(enumerate(numeral_sequence))

    @cached_property
    def value(self) -> int:
        return self.number

    def get_closest_smaller_number(self) -> int:
        closest_smaller_distance = min([n for n in self.distances if n >= 0])
        closest_smaller_distance_index = self.distances.index(closest_smaller_distance)
        return self._get_number_from(closest_smaller_distance_index)

    def get_second_smaller_number(self) -> int:
        closest_smaller_number = self.get_closest_smaller_number()
        if closest_smaller_number == self.get_closest_smaller_order_of_magnitude():
            return NumeralDescriptor(
                closest_smaller_number, self.numeral_sequence
            ).get_closest_smaller_number()
        return NumeralDescriptor(
            closest_smaller_number - 1, self.numeral_sequence
        ).get_closest_smaller_number()

    def get_closest_greater_number(self) -> int:
        closest_greater_distance_index = self.distances.index(
            self.get_closest_greater_distance()
        )
        return self._get_number_from(closest_greater_distance_index)

    def get_closest_greater_distance(self) -> int:
        return max([n for n in self.distances if n <= 0])

    def get_closest_smaller_order_of_magnitude(self) -> int:
        closest_smaller_distance = min([n for n in self.distances if n >= 0])
        return self._get_closest_smaller_order_of_magnitude(
            self.distances.index(closest_smaller_distance)
        )

    def _get_number_from(self, index: int) -> int:
        return [num for pos, num in self.enumerated_numeral_sequence if pos == index][0]

    def _get_closest_smaller_order_of_magnitude(self, index: int) -> int:
        closest_smaller_order_of_magnitude_index = self._get_order_of_magnitude_index(
            index
        )
        return self._get_number_from(closest_smaller_order_of_magnitude_index)

    def _get_order_of_magnitude_index(self, index: int) -> int:
        return index if index % 2 == 0 else index - 1
