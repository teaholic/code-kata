from dataclasses import dataclass


@dataclass(frozen=True)
class Driver:
    id: str
    points: int


@dataclass(frozen=True)
class Board:
    results: set[Driver]


class ScoringService:
    def __init__(self, drivers: set[Driver]):
        self.drivers = drivers
        self.points = [25, 18, 15]

    def score(self, board: Board):
        return set(
            [
                Driver(driver.id, driver.points + point)
                for driver, point in zip(board.results, self.points)
            ]
        )
