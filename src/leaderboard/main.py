import operator
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Driver:
    id: str
    points: int


class DriverService:
    def __init__(self):
        self.points = [25, 18, 15]

    def score(self, races: List[List[Driver]]) -> List[Driver]:
        updated_drivers = []
        for race in races:
            updated_drivers.extend(self.__score_single(race))

        aggregated_drivers = []
        for driver_id in set([d.id for d in updated_drivers]):
            filtered_drivers = list(filter(lambda d: d.id==driver_id, updated_drivers))
            aggregated_points = sum([driver.points for driver in filtered_drivers])
            aggregated_drivers.append(Driver(id=driver_id, points=aggregated_points))

        ordered_drivers = sorted(aggregated_drivers, key=operator.attrgetter("points"), reverse=True)
        return ordered_drivers

    def __score_single(self, race: List[Driver]) -> List[Driver]:
        ranked_drivers = list(enumerate(race))

        results = []
        for (rank, driver) in ranked_drivers:
            updated_points = driver.points + self.points[rank] if len(self.points) > rank else 0
            updated_driver = Driver(id=driver.id, points=updated_points)
            results.append(updated_driver)
        return results
