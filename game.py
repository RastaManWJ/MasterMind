from codebreaker import CodeBreaker
from codemaker import CodeMaker


class Game:
    def __init__(self, rows):
        self.rows = rows
        self.current_row = 0
        self.finished = False
        self.winner = ''    #'Codemaker' or 'Codebreaker'

    def _board_reset(self):
        self.rows = 0
        self.current_row = 0

    def _next_row(self):
        if self.current_row != self.rows:
            self.current_row += 1
        else:
            self.finished = True
            self.game_ends('CodeMaker')

    def game_ends(self, winner):
        self.winner = winner

    def _ask_for_code(self, codebreaker):
        guessing = True
        while guessing:
            if codebreaker.confirm_guess():
                end_guess = input(__prompt="Do you want to change your guess? [Y/N]")
                if end_guess == "N":
                    guessing = not guessing
                elif end_guess != "Y":
                    print("You provided wrong answer!")
            print("Your code is: {}".format(codebreaker.get_guess()))
            peg_id = input(__prompt="Which peg do you want to change? [1-4]")
            if peg_id not in range(1, 4):
                print("You provided wrong peg number!")
                continue
            peg_color = input(__prompt="Change peg number {} to: [0-5] ".format(peg_id))
            if peg_color not in range(0, 5):
                print("You provided wrong peg value!")
                continue
            if peg_id == 1:
                codebreaker.change_first_color(peg_color)
            if peg_id == 2:
                codebreaker.change_second_color(peg_color)
            if peg_id == 3:
                codebreaker.change_third_color(peg_color)
            if peg_id == 4:
                codebreaker.change_fourth_color(peg_color)

    def run_game(self):
        codebreaker = CodeBreaker()
        codemaker = CodeMaker()
        codemaker.draw_code()
        while self.finished or codemaker.codebreaker_wins_condition():
            code = self.ask_for_code(codebreaker)


