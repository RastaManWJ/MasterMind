from codebreaker import CodeBreaker
from codemaker import CodeMaker


class Game:
    def __init__(self, rows):
        self.rows = rows
        self.current_row = 0
        self.finished = False
        self.winner = ''    #'Codemaker' or 'Codebreaker'

    def board_reset(self):
        self.rows = 0
        self.current_row = 0

    def next_row(self):
        if self.current_row != self.rows:
            self.current_row += 1
        else:
            self.finished = True
            self.game_ends('CodeMaker')

    def game_ends(self, winner):
        self.winner = winner

    def run_game(self):
        codebreaker = CodeBreaker()
        codemaker = CodeMaker()
        codemaker.draw_code()
        while self.finished or codemaker.codebreaker_wins_condition():
            pass


