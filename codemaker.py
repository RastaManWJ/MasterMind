from random import randrange

class AI:
    def __init__(self):
        self.code = [None, None, None, None]

    def draw_code(self):
        code = []
        for i in range(4):
            code.append(randrange(5))
        self.code = code

    def reset_code(self):
        self.code = [None, None, None, None]

    def check_guess(self, guess):
        pass

    def provide_feedback(self):
        pass