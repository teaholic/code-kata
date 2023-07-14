from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Driver:
    id: str
    points: int


@dataclass(frozen=True)
class Race:
    results = List[Driver]


class ScoringService:
    def __init__(self, drivers):
        self.drivers = drivers
        self.points = [25, 18, 15]

    def score(self, race: List[Driver]):
        return set(
            [
                Driver(driver.id, driver.points + point)
                for driver, point in zip(race, self.points)
            ]
        )