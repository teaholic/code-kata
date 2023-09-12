from unittest import TestCase

from parameterized import parameterized

from tennis.main import (
    Dashboard,
    Umpire,
    TennisGame,
    Point,
    Score,
)


class TestDashboard(TestCase):
    @parameterized.expand(
        [
            [["1", "1", "2", "1"], Score(player1=Point.FORTY, player2=Point.FIFTEEN)],
            [
                ["2", "1", "1", "2", "2"],
                Score(player1=Point.THIRTY, player2=Point.FORTY),
            ],
            [
                ["2", "1", "2", "1", "2", "1"],
                Score(player1=Point.DEUCE, player2=Point.DEUCE),
            ],
            [
                ["2", "1", "2", "1", "2", "1", "1"],
                Score(player1=Point.ADVANTAGE, player2=Point.DEUCE),
            ],
        ]
    )
    def test_update(self, game, expected):
        dashboard = Dashboard(game)
        actual = dashboard.update()
        self.assertEqual(actual.player1.name, expected.player1.name)
        self.assertEqual(actual.player2.name, expected.player2.name)


class TestUmpire(TestCase):
    umpire = Umpire()

    @parameterized.expand(
        [
            [Score(player1=Point.FORTY, player2=Point.FIFTEEN), "Player 1"],
            [Score(player1=Point.LOVE, player2=Point.FORTY), "Player 2"],
            [Score(player1=Point.ADVANTAGE, player2=Point.THIRTY), "Player 1"],
            [Score(player1=Point.DEUCE, player2=Point.ADVANTAGE), "Player 2"],
            [Score(player1=Point.FORTY, player2=Point.THIRTY), "invalid game"],
            [Score(player1=Point.FIFTEEN, player2=Point.THIRTY), "invalid game"],
            [Score(player1=Point.FORTY, player2=Point.FORTY), "invalid game"],
            [Score(player1=Point.DEUCE, player2=Point.DEUCE), "invalid game"],
        ]
    )
    def test_find_winner(self, scores, expected):
        actual = self.umpire.find_winner(scores, ["Player 1", "Player 2"])
        self.assertEqual(actual, expected)


class TestTennisGame(TestCase):
    @parameterized.expand(
        [
            [["1", "1", "1", "2"], "1"],
            [["2", "1", "1", "1"], "1"],
            [["2", "1", "1", "2", "2", "2", "2"], "2"],
            [["2", "1", "1", "2", "1", "2", "1"], "1"],
            [["a", "b", "a"], "invalid game"],
            [["2", "1", "1", "2", "1", "1"], "invalid game"],
        ]
    )
    def test_run(self, game, expected):
        engine = TennisGame(game)
        actual = engine.run(game)
        self.assertEqual(actual, expected)
