from unittest import TestCase

from src.leaderboard.main import Driver, ScoringService


class TestScoringService(TestCase):
    def test_score(self):
        service = ScoringService(
            (Driver("a", 0), Driver("b", 0), Driver("c", 0), Driver("d", 0))
        )

        expected = {Driver("a", 18), Driver("b", 25), Driver("c", 15)}
        actual = service.score(
            [Driver("b", 0), Driver("a", 0), Driver("c", 0), Driver("d", 0)]
        )

        self.assertEqual(actual, expected)
