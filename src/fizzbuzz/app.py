from typing import List

from fizzbuzz.handler import Handler


class FizzBuzzApp:
    def __init__(self, handlers: List[Handler]):
        self.handlers = handlers

    def run(self, n):
        return self._sanitize(n, [handler.handle(n) for handler in self.handlers])

    def _sanitize(self, n, res: List[str]):
        if "".join(res) == "":
            return n
        return "".join(res)
