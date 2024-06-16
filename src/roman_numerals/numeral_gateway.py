from typing import List


class NumeralGateway:
    def __init__(self, number: int, numeral_sequence: List[int]):
        self.number = number
        self.enumerated_numeral_sequence = enumerate([n for n in numeral_sequence])
        self.residues = SubtractionService(
            number=number, numeral_sequence=numeral_sequence
        ).run()

    def get_closest_smaller_number(self) -> int:
        closest_smaller_residue = min([n for n in self.residues if n >= 0])
        closest_smaller_residue_index = self.residues.index(closest_smaller_residue)
        return [
            num
            for pos, num in self.enumerated_numeral_sequence
            if pos == closest_smaller_residue_index
        ][0]

    def get_closest_greater_number(self) -> int:
        closest_greater_residue_index = self.residues.index(
            self.get_closest_greater_residue()
        )
        return [
            num
            for pos, num in self.enumerated_numeral_sequence
            if pos == closest_greater_residue_index
        ][0]

    def get_closest_greater_residue(self) -> int:
        return max([n for n in self.residues if n <= 0])

    def get_closest_smaller_tenth(self) -> int:
        closest_smaller_residue = min([n for n in self.residues if n >= 0])
        closest_smaller_tenth_index = (
            self.residues.index(closest_smaller_residue)
            if self.residues.index(closest_smaller_residue) % 2 == 0
            else self.residues.index(closest_smaller_residue) - 1
        )
        print(closest_smaller_tenth_index)
        return [
            num
            for pos, num in self.enumerated_numeral_sequence
            if pos == closest_smaller_tenth_index
        ][0]


class SubtractionService:
    def __init__(self, number: int, numeral_sequence: List[int]):
        self.number = number
        self.numeral_sequence = numeral_sequence

    def run(self) -> List[int]:
        return [self.number - n for n in self.numeral_sequence]
