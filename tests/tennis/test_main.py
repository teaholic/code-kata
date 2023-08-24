from unittest import TestCase
from tennis.main import Dashboard, Umpire, TennisGame, Point


class TestPoint(TestCase):
    def test_next(self):
        test_cases = [
            [Point.love, Point.fifteen],
            [Point.fifteen, Point.thirty],
            [Point.thirty, Point.forty],
        ]

        for starting_score, expected in test_cases:
            actual = Point(starting_score.value + 1)
            self.assertEqual(actual, expected)


class TestDashboard(TestCase):
    def test_update(self):
        test_cases = [
            [["1", "1", "1", "2", "1"], {"1": Point(4), "2": Point(1)}],
            [["2", "1", "1", "2", "2", "1", "2", "2"], {"1": Point(3), "2": Point(5)}],
            [
                ["2", "1", "1", "2", "2", "1", "2", "1", "1", "1"],
                {"1": Point(6), "2": Point(4)},
            ],
        ]

        for game, expected in test_cases:
            dashboard = Dashboard(game)
            dashboard.update()
            self.assertEqual(dashboard.scores, expected)


class TestUmpire(TestCase):
    def test_find_winner(self):
        test_cases = [
            [{"1": Point(4), "2": Point(1)}, "1"],
            [{"1": Point(3), "2": Point(5)}, "2"],
            [{"1": Point(6), "2": Point(4)}, "1"],
            [{"1": Point(3), "2": Point(1)}, "invalid game"],
            [{"1": Point(6), "2": Point(5)}, "invalid game"],
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
