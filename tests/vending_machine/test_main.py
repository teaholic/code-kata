from unittest import TestCase
from parameterized import parameterized

from vending_machine.main import VendingMachine


class TestVendingMachine(TestCase):
    machine = VendingMachine()

    @parameterized.expand(
        [
            ["penny", "INSERT COIN", ["penny"]],
            ["nickel", 5, ["penny"]],
            ["dime", 15, ["penny"]],
            ["quarter", 40, ["penny"]],
        ]
    )
    def test_collect(self, coin, expected_inserted, expected_returned):
        self.machine.collect(coin)
        self.assertEqual(self.machine.inserted, expected_inserted)
        self.assertEqual(self.machine.returned, expected_returned)
