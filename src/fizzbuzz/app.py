from dataclasses import dataclass
from enum import Enum


class Multiplier(Enum):
    Fizz = 3
    Buzz = 5
    Whizz = 7
    Bang = 11


@dataclass(frozen=True)
class Request:
    number: int

    def is_multiple_of(self, multiplier: Multiplier) -> bool:
        return self.number % multiplier.value == 0


@dataclass(frozen=True)
class Result:
    value: str


class ResultFactory:
    @staticmethod
    def create(request) -> Result:
        result = ""
        for multiplier in Multiplier:
            if request.is_multiple_of(multiplier):
                result += Multiplier(multiplier.value).name
        return Result(value=result)


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
    def __init__(self):
        self.factory = ResultFactory()

    def run(self, request: Request):
        result = self.factory.create(request)
        if result.value == "":
            return request.number
        return result.value
