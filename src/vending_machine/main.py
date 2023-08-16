from dataclasses import dataclass
from enum import Enum


class ValidMoney(Enum):
    nickel = 5
    dime = 10
    quarter = 25


@dataclass(frozen=True)
class CoinSpec:
    weight: int
    size: str


class CoinScale(Enum):
    penny = CoinSpec(1, "tiny")
    nickel = CoinSpec(2, "mini")
    dime = CoinSpec(3, "mini")
    quarter = CoinSpec(4, "small")


class VendingMachine:
    def __init__(self):
        self.inserted = "INSERT COIN"
        self.returned = []

    def collect(self, spec: str):
        coin = CoinScale(spec).name
        if coin in ValidMoney._member_names_:
            try:
                self.inserted += ValidMoney.__members__[coin].value
            except:
                self.inserted = ValidMoney.__members__[coin].value
        else:
            self.returned.append(coin)
