from unittest import TestCase
from parameterized import parameterized

from vending_machine.main import VendingMachine, CoinScale


class TestCoinScale(TestCase):
    @parameterized.expand(
        [
            [(1, "tiny"), "penny"],
            [(2, "mini"), "nickel"],
            [(3, "mini"), "dime"],
            [(4, "small"), "quarter"],
        ]
    )
    def test_collect(self, spec, expected):
        self.assertEqual(CoinScale(spec).name, expected)


class TestVendingMachine(TestCase):
    machine = VendingMachine()

    @parameterized.expand(
        [
            [(1, "tiny"), "INSERT COIN", ["penny"]],
            [(2, "mini"), 5, ["penny"]],
            [(3, "mini"), 15, ["penny"]],
            [(4, "small"), 40, ["penny"]],
        ]
    )
    def test_collect(self, spec, expected_inserted, expected_returned):
        self.machine.collect(spec)
        self.assertEqual(self.machine.inserted, expected_inserted)
        self.assertEqual(self.machine.returned, expected_returned)
