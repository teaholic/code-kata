class Input:
    def __init__(self, value):
        self.value = value

    def is_multiple_of_three(self) -> bool:
        return self.value % 3 == 0

    def is_multiple_of_five(self) -> bool:
        return self.value % 5 == 0

    def is_multiple_of_three_and_five(self) -> bool:
        return (self.value % 3 == 0) & (self.value % 5 == 0)