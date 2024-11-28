LOVE = 0
FIFTEEN = 1
THIRTY = 2
FORTY = 3
GAME = 4
SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty", "Game"]

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = LOVE
        self.player2_score = LOVE

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def score_is_tied(self):
        return self.player1_score == self.player2_score

    def score_is_deuce(self):
        return self.score_is_tied() and self.player1_score >= FORTY

    def score_situation_when_score_is_tied(self):
        if self.score_is_deuce():
            return "Deuce"
        return f"{SCORE_NAMES[self.player1_score]}-All"

    def score_is_game_or_more(self):
        return self.player1_score >= GAME or self.player2_score >= GAME

    def score_situation_when_score_is_game_or_more(self):
        score_difference = self.player1_score - self. player2_score
        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        elif score_difference == -1:
            return f"Advantage {self.player2_name}"
        elif score_difference >= 2:
            return f"Win for {self.player1_name}"
        return f"Win for {self.player2_name}"

    def score_situation_before_score_is_game(self):
        return f"{SCORE_NAMES[self.player1_score]}-{SCORE_NAMES[self.player2_score]}"

    def get_score(self):
        if self.score_is_tied():
            return self.score_situation_when_score_is_tied()
        elif self.score_is_game_or_more():
            return self.score_situation_when_score_is_game_or_more()
        else:
            return self.score_situation_before_score_is_game()
