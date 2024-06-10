from enum import Enum


class Multiplier(Enum):
    Fizz = 3
    Buzz = 5
    Whizz = 7
    Bang = 11


class FizzBuzzApp:

    def run(self, request:int):
        result = self._run(request)
        if result == "":
            return request
        return result

    def _run(self, request:int):
        result = ""
        for multiplier in Multiplier:
            if request % multiplier.value == 0:
                result += Multiplier(multiplier.value).name
        return result
