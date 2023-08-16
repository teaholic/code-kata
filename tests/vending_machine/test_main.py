from unittest import TestCase
from parameterized import parameterized

from vending_machine.main import VendingMachine, CoinScale


class TestCoinScale(TestCase):
    @parameterized.expand(
        [
            ["tiny", "penny"],
            ["mini", "nickel"],
            ["smaller", "dime"],
            ["small", "quarter"],
        ]
    )
    def test_collect(self, weight, expected):
        self.assertEqual(CoinScale.__members__[weight].value, expected)


class TestVendingMachine(TestCase):
    machine = VendingMachine()

    @parameterized.expand(
        [
            ["tiny", "INSERT COIN", ["penny"]],
            ["mini", 5, ["penny"]],
            ["smaller", 15, ["penny"]],
            ["small", 40, ["penny"]],
        ]
    )
    def test_collect(self, coin, expected_inserted, expected_returned):
        self.machine.collect(coin)
        self.assertEqual(self.machine.inserted, expected_inserted)
        self.assertEqual(self.machine.returned, expected_returned)
