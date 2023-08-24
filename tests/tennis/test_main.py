from unittest import TestCase
from tennis.main import Dashboard, Umpire, TennisGame


class TestDashboard(TestCase):
    def test_update(self):
        test_cases = [
            [["1", "1", "1", "2", "1"], {"1": 4, "2": 1}],
            [["2", "1", "1", "2", "2", "1", "2", "2"], {"1": 3, "2": 5}],
            [["2", "1", "1", "2", "2", "1", "2", "1", "1", "1"], {"1": 6, "2": 4}],
        ]

        for game, expected in test_cases:
            dashboard = Dashboard(game)
            dashboard.update()
            self.assertEqual(dashboard.scores, expected)


class TestUmpire(TestCase):
    def test_find_winner(self):
        test_cases = [
            [{"1": 4, "2": 1}, "1"],
            [{"1": 3, "2": 5}, "2"],
            [{"1": 6, "2": 4}, "1"],
            [{"1": 3, "2": 1}, "invalid game"],
            [{"1": 6, "2": 5}, "invalid game"],
        ]

        umpire = Umpire()
        for scores, expected in test_cases:
            actual = umpire.find_winner(scores)
            self.assertEqual(actual, expected)


class TestTennisGame(TestCase):
    def test_run(self):
        test_cases = [
            [["1", "1", "1", "2", "1"], "1"],
            [["2", "1", "1", "2", "2", "1", "2", "2"], "2"],
            [["2", "1", "1", "2", "2", "1", "2", "1", "1", "1"], "1"],
            [["a", "b", "a", "a"], "invalid game"],
            [["2", "1", "1", "2", "2", "1", "2", "1", "1"], "invalid game"],
        ]

        for game, expected in test_cases:
            engine = TennisGame(game)
            actual = engine.run(game)
            self.assertEqual(actual, expected)
