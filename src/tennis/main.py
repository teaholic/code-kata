from enum import Enum
from typing import NamedTuple, List


class Point(Enum):
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3
    WIN = 4


class PointService:
    def update(self, point: Point):
        return Point(point.value + 1)


class Score(NamedTuple):
    player1: Point
    player2: Point

    def get_top_scorer(self):
        if self.player1.value > self.player2.value:
            return 0
        else:
            return 1

    def get_least_scorer(self):
        if self.player1.value < self.player2.value:
            return 0
        else:
            return 1


class Dashboard:
    def __init__(self, game):
        self.game = game
        [self.player1, self.player2] = set(game)
        self.scores = {self.player1: Point(0), self.player2: Point(0)}
        self.service = PointService()

    def update(self) -> Score:
        for match_id in range(len(self.game)):
            match_winner = self.game[match_id]
            self.scores[match_winner] = self.service.update(self.scores[match_winner])
        return Score(self.scores[self.player1], self.scores[self.player2])


class Umpire:
    def find_winner(self, scores: Score, players: List[str]) -> str:
        top_scorer = scores.get_top_scorer()
        opponent = scores.get_least_scorer()
        if scores[top_scorer].value >= 4:
            print("top_scorer points > 4")
            if scores[top_scorer].value - scores[opponent].value >= 2:
                print("top_scorer scored at least 2 points more than opponent")
                return players[top_scorer]
            else:
                return "invalid game"
        else:
            return "invalid game"


class TennisGame:
    def __init__(self, game):
        self.dashboard = Dashboard(game)
        self.umpire = Umpire()

    def run(self, game) -> str:
        return self.umpire.find_winner(
            scores=self.dashboard.update(), players=list(set(game))
        )
