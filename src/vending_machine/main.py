from enum import Enum


class ValidMoney(Enum):
    nickel = 5
    dime = 10
    quarter = 25


class VendingMachine:
    def __init__(self):
        self.inserted = "INSERT COIN"
        self.returned = []

    def collect(self, coin: str):
        if coin in ValidMoney._member_names_:
            print(coin)
            print(ValidMoney.__members__[coin].value)
            try:
                self.inserted += ValidMoney.__members__[coin].value
            except:
                self.inserted = ValidMoney.__members__[coin].value
        else:
            self.returned.append(coin)
