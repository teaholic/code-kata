from enum import Enum


class Multiplier(Enum):
    Fizz = 3
    Buzz = 5
    Whizz = 7
    Bang = 11


class FizzBuzzApp:
    def __init__(self):
        self.service = FizzBuzzService()

    def run(self):
        n = 1
        result = ""
        while result != "FizzBuzzWhizzBang":
            result = self.service.run(n)
            print(result)
            n += 1
        return result


class FizzBuzzService:

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
