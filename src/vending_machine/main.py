from enum import Enum


class ValidMoney(Enum):
    nickel = 5
    dime = 10
    quarter = 25


class CoinScale(Enum):
    penny = (1, "tiny")
    nickel = (2, "mini")
    dime = (3, "mini")
    quarter = (4, "small")


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
