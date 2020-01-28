from random import randrange

class Codemaker:
    def __init__(self):
        self.code = [None]*4
        self.key_pegs = [0]*4
        self.key_peg_amount = 0

    def draw_code(self):
        code = []
        for i in range(4):
            code.append(randrange(5))
        self.code = code

    def reset_code(self):
        self.code = [None]*4

    def codebreaker_wins_condition(self):
        if all(self.key_pegs) == 2:
            return True
        return False

    def check_for_ideal_placement(self, guess):
        for peg_id in range(len(self.code)):
            if self.code[peg_id] == guess[peg_id]:
                self.key_pegs[self.key_peg_amount] = 2
                self.key_peg_amount += 1
                guess[peg_id] = None
        return guess

    def check_for_color_pairs(self, guess):
        temp_guess = guess
        for peg_id in range(len(self.code)):
            if self.code[peg_id] in guess:
                guess.remove(self.code[peg_id])
                self.key_pegs[self.key_peg_amount] = 1
                self.key_peg_amount += 1

    def provide_feedback(self, guess):
        guess = self.check_for_ideal_placement(guess)
        self.check_for_color_pairs(guess)
        return self.key_pegs

    def reset_feedback_pegs(self):
        self.key_pegs = [0]*4
        self.key_peg_amount = 0
