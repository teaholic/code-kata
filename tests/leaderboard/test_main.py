from unittest import TestCase

from parameterized import parameterized

from src.leaderboard.main import Driver, ScoringService, Board


class TestScoringService(TestCase):
    def test_score(self):
        service = ScoringService({Driver("a", 0), Driver("b", 0), Driver("c", 0), Driver("d", 0)})
        races = [
            Board(results={Driver("b", 0), Driver("a", 0), Driver("c", 0), Driver("d", 0)}),
            Board(results={Driver("a", 0), Driver("c", 0), Driver("d", 0), Driver("b", 0)})
            ]

        expected = {Driver("a", 18+25), Driver("b", 25+0), Driver("c", 15+18), Driver("d", 0+15)}
        actual = service.score(races)

        self.assertEqual(actual, expected)
