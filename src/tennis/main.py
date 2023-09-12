from typing import List

from tennis.model import Point, PointService, Score, RankingService, Ranking


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
        print(ranking)
        top_scorer = ranking.top_scorer_index
        opponent = ranking.least_scorer_index
        if scores[top_scorer].value == 5:
            return players[top_scorer]
        elif scores[top_scorer].value == 3:
            print("top_scorer has scored at least forty")
            if scores[top_scorer].value - scores[opponent].value >= 2:
                print("top_scorer scored at least 2 points more than opponent")
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
            scores=self.dashboard.update(), players=list(set(game))
        )
