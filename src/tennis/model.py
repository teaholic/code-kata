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
