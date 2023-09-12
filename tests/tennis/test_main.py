from unittest import TestCase
from tennis.main import (
    Dashboard,
    Umpire,
    TennisGame,
    Point,
    Score,
)


class TestDashboard(TestCase):
    def test_update(self):
        test_cases = [
            [["1", "1", "2", "1"], Score(player1=Point(3), player2=Point(1))],
            [["2", "1", "1", "2", "2"], Score(player1=Point(2), player2=Point(3))],
            [["2", "1", "2", "1", "2", "1"], Score(player1=Point(4), player2=Point(4))],
        ]

        for game, expected in test_cases:
            dashboard = Dashboard(game)
            actual = dashboard.update()
            self.assertEqual(actual.player1, expected.player1)
            self.assertEqual(actual.player2, expected.player2)


class TestUmpire(TestCase):
    def test_find_winner(self):
        test_cases = [
            [Score(player1=Point(4), player2=Point(1)), "Player 1"],
            [Score(player1=Point(0), player2=Point(4)), "Player 2"],
            [Score(player1=Point(3), player2=Point(2)), "invalid game"],
            [Score(player1=Point(1), player2=Point(2)), "invalid game"],
        ]

        umpire = Umpire()
        for scores, expected in test_cases:
            actual = umpire.find_winner(scores, ["Player 1", "Player 2"])
            self.assertEqual(actual, expected)


class TestTennisGame(TestCase):
    def test_run(self):
        test_cases = [
            [["1", "1", "1", "2", "1"], "1"],
            [["2", "1", "1", "2", "2", "2"], "2"],
            [["2", "1", "1", "2", "1", "1"], "1"],
            [["a", "b", "a", "a"], "invalid game"],
        ]

        for game, expected in test_cases:
            engine = TennisGame(game)
            actual = engine.run(game)
            self.assertEqual(actual, expected)
