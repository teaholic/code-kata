from unittest import TestCase
from parameterized import parameterized

from vending_machine.main import VendingMachine, CoinScale, CoinSpec


class TestCoinScale(TestCase):
    @parameterized.expand(
        [
            [CoinSpec(1, "tiny"), "penny"],
            [CoinSpec(2, "mini"), "nickel"],
            [CoinSpec(3, "mini"), "dime"],
            [CoinSpec(4, "small"), "quarter"],
        ]
    )
    def test_get(self, spec, expected):
        self.assertEqual(CoinScale(spec).name, expected)


class TestVendingMachine(TestCase):
    machine = VendingMachine()

    @parameterized.expand(
        [
            [CoinSpec(1, "tiny"), "INSERT COIN", ["penny"]],
            [CoinSpec(2, "mini"), 5, ["penny"]],
            [CoinSpec(3, "mini"), 15, ["penny"]],
            [CoinSpec(4, "small"), 40, ["penny"]],
        ]
    )
    def test_collect(self, spec, expected_inserted, expected_returned):
        self.machine.collect(spec)
        self.assertEqual(self.machine.inserted, expected_inserted)
        self.assertEqual(self.machine.returned, expected_returned)
