class Codebreaker:
    def __init__(self):
        self.points = 0
        self.guess = [None, None, None, None]

    def add_point(self):
        self.points += 1

    def reset_points(self):
        self.points = 0

    def prepare_guess(self, color0, color1, color2, color3):
        self.guess = [color0, color1, color2, color3]