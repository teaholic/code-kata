from fizzbuzz.model import Input


class FizzBuzzApp:
    def run(self, value: int):
        my_input = Input(value)
        if my_input.is_multiple_of_three_and_five():
            return "FizzBuzz"
        elif my_input.is_multiple_of_three():
            return "Fizz"
        elif my_input.is_multiple_of_five():
            return "Buzz"
        return value
