from enum import Enum


class ValidMoney(Enum):
    nickel = 5
    dime = 10
    quarter = 25


class CoinScale(Enum):
    tiny = "penny"
    mini = "nickel"
    smaller = "dime"
    small = "quarter"


class VendingMachine:
    def __init__(self):
        self.inserted = "INSERT COIN"
        self.returned = []

    def collect(self, weight: str):
        coin = CoinScale.__members__[weight].value
        if coin in ValidMoney._member_names_:
            try:
                self.inserted += ValidMoney.__members__[coin].value
            except:
                self.inserted = ValidMoney.__members__[coin].value
        else:
            self.returned.append(coin)
