from abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):
    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class MultipleOfThree(Handler):
    def handle(self, request: int) -> str:
        if request % 3 == 0:
            return "Fizz"
        return ""


class MultipleOfFive(Handler):
    def handle(self, request: int) -> str:
        if request % 5 == 0:
            return "Buzz"
        return ""


class MultipleOfSeven(Handler):
    def handle(self, request: int) -> str:
        if request % 7 == 0:
            return "Whizz"
        return ""


class MultipleOfEleven(Handler):
    def handle(self, request: int) -> str:
        if request % 11 == 0:
            return "Bang"
        return ""
