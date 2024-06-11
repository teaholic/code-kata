from dataclasses import dataclass
from enum import Enum

@dataclass(frozen=True)
class Request:
    number: int

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
        output = ""
        result = []
        while output != "FizzBuzzWhizzBang":
            output = self.service.run(Request(number=n))
            print(output)
            result.append(output)
            n += 1
        return result


class FizzBuzzService:

    def run(self, request:Request):
        result = self._run(request)
        if result == "":
            return request.number
        return result

    def _run(self, request:Request):
        result = ""
        for multiplier in Multiplier:
            if request.number % multiplier.value == 0:
                result += Multiplier(multiplier.value).name
        return result
