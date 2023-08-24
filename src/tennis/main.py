class Dashboard:
    def __init__(self, game):
        self.game = game
        self.player1, self.player2 = set(game)
        self.scores = {self.player1: 0, self.player2: 0}

    def update(self):
        for match_id in range(len(self.game)):
            match_winner = self.game[match_id]
            self.scores[match_winner] += 1


class Umpire:
    def find_winner(self, scores: dict) -> str:
        top_scorer = max(scores, key=scores.get)
        opponent = min(scores, key=scores.get)
        if scores[top_scorer] >= 4:
            print("top_scorer points > 4")
            if scores[top_scorer] - scores[opponent] >= 2:
                print("top_scorer scored at least 2 points more than opponent")
                return top_scorer
            else:
                return "invalid game"
        else:
            return "invalid game"


class TennisGame:
    def __init__(self, game):
        self.dashboard = Dashboard(game)
        self.umpire = Umpire()

    def run(self, game) -> str:
        self.dashboard.update()
        return self.umpire.find_winner(self.dashboard.scores)
