from enum import Enum
from typing import NamedTuple, List


class Point(Enum):
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3
    DEUCE = 4


class PointService:
    def update(self, point: Point) -> Point:
        return Point(point.value + 1)


class Score(NamedTuple):
    player1: Point
    player2: Point


class Ranking(NamedTuple):
    top_scorer_index: int
    least_scorer_index: int


class RankingService:
    def compute(self, score: Score) -> Ranking:
        if score.player1.value > score.player2.value:
            return Ranking(top_scorer_index=0, least_scorer_index=1)
        else:
            return Ranking(top_scorer_index=1, least_scorer_index=0)


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
            if self.scores[match_winner].value == 3:
                players = set(self.game)
                players.remove(match_winner)
                match_looser = list(players)[0]
                if self.scores[match_looser].value == 3:
                    self.scores[match_winner] = self.service.update(
                        self.scores[match_winner]
                    )
                    self.scores[match_looser] = self.service.update(
                        self.scores[match_looser]
                    )
        return Score(self.scores[self.player1], self.scores[self.player2])


class Umpire:
    def __init__(self):
        self.service = RankingService()

    def find_winner(self, scores: Score, players: List[str]) -> str:
        ranking: Ranking = self.service.compute(scores)
        top_scorer = ranking.top_scorer_index
        opponent = ranking.least_scorer_index
        if scores[top_scorer].value == 4:
            print("top_scorer has 4 points")
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
