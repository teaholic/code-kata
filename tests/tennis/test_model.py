from unittest import TestCase

from tennis.model import Point, PointService, Score, Ranking, RankingService


class TestScoreService(TestCase):
    def test_update(self):
        test_cases = [
            [Point(0), Point(1)],
            [Point(1), Point(2)],
            [Point(2), Point(3)],
            [Point(3), Point(4)],
            [Point(4), Point(5)],
            [Point.LOVE, Point.FIFTEEN],
            [Point.FIFTEEN, Point.THIRTY],
            [Point.THIRTY, Point.FORTY],
            [Point.FORTY, Point.DEUCE],
            [Point.DEUCE, Point.ADVANTAGE],
        ]

        service = PointService()
        for point, expected in test_cases:
            actual = service.update(point)
            self.assertEqual(actual, expected)


class TestRankingService(TestCase):
    def test_compute(self):
        test_cases = [
            [
                Score(Point(0), Point(2)),
                Ranking(top_scorer_index=1, least_scorer_index=0),
            ],
            [
                Score(Point(3), Point(1)),
                Ranking(top_scorer_index=0, least_scorer_index=1),
            ],
        ]

        service = RankingService()
        for score, expected in test_cases:
            actual = service.compute(score)
            self.assertEqual(actual.top_scorer_index, expected.top_scorer_index)
            self.assertEqual(actual.least_scorer_index, expected.least_scorer_index)
