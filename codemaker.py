from random import randrange

class Codemaker:
    def __init__(self):
        self.code = [None]*4

    def draw_code(self):
        code = []
        for i in range(4):
            code.append(randrange(5))
        self.code = code

    def reset_code(self):
        self.code = [None]*4

    def check_guess(self, guess):
        pass

    def provide_feedback(self):
        pass