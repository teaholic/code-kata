from unittest import TestCase

from leaderboard.main import Driver, DriverService


class TestResultService(TestCase):
    def test_score(self):
        race1 = [Driver("b", 0), Driver("a", 0), Driver("c", 0), Driver("d", 0)]
        race2 = [Driver("b", 0), Driver("a", 0), Driver("c", 0), Driver("d", 0)]
        service = DriverService()

        expected = [
            Driver("b", 25+25),
            Driver("a", 18+18),
            Driver("c", 15+15),
            Driver("d", 0+0)
        ]
        actual = service.score(races=[race1, race2])
        self.assertEqual(actual, expected)
