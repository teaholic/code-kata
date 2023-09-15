from typing import List, NamedTuple, Set

from tennis.model import Point, PointService, Score, RankingService, Ranking


class PointRanking(NamedTuple):
    winner: str
    opponent: str


class PointRankingService:
    def run(self, winner: str, players: Set[str]) -> PointRanking:
        players.remove(winner)
        return PointRanking(winner=winner, opponent=list(players)[0])


class Dashboard:
    def __init__(self, game):
        self.game = game
        [self.player1, self.player2] = sorted(set(game))
        self.scores = {self.player1: Point(0), self.player2: Point(0)}
        self.point_service = PointService()
        self.ranking_service = PointRankingService()

    def update(self) -> Score:
        for match_id in range(len(self.game)):
            players: PointRanking = self.ranking_service.run(
                self.game[match_id], sorted(set(self.game))
            )
            self.scores[players.winner] = self.point_service.update(
                self.scores[players.winner]
            )
            self.__score_deuce(players)
        return Score(self.scores[self.player1], self.scores[self.player2])

    def __score_deuce(self, players: PointRanking):
        if self.scores[players.winner].value == 3:
            if self.scores[players.opponent].value == 3:
                self.scores[players.winner] = self.point_service.update(
                    self.scores[players.winner]
                )
                self.scores[players.opponent] = self.point_service.update(
                    self.scores[players.opponent]
                )


class Umpire:
    def __init__(self):
        self.service = RankingService()

    def find_winner(self, scores: Score, players: List[str]) -> str:
        ranking: Ranking = self.service.compute(scores)
        print(ranking)
        top_scorer = ranking.top_scorer_index
        opponent = ranking.least_scorer_index
        if scores[top_scorer].value == 5:
            print("The winner is " + players[top_scorer])
            return players[top_scorer]
        elif scores[top_scorer].value == 3:
            print("top_scorer has scored at least forty")
            if scores[top_scorer].value - scores[opponent].value >= 2:
                print("top_scorer scored at least 2 points more than opponent")
                print("The winner is " + players[top_scorer])
                return players[top_scorer]
            else:
                print(
                    "invalid game for top scorer "
                    + str(scores[top_scorer].value)
                    + " and opponent "
                    + str(scores[opponent].value)
                )
                return "invalid game"
        else:
            print("invalid game for top scorer " + str(scores[top_scorer].value))
            return "invalid game"


class TennisGame:
    def __init__(self, game):
        self.dashboard = Dashboard(game)
        self.umpire = Umpire()

    def run(self, game) -> str:
        return self.umpire.find_winner(
            scores=self.dashboard.update(), players=list(sorted(set(game)))
        )
