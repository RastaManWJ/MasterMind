class Codebreaker:
    def __init__(self):
        self.points = 0
        self.guess = [None, None, None, None]

    def add_point(self):
        self.points += 1

    def reset_points(self):
        self.points = 0

    def change_first_color(self, color):
        self.guess[0] = color

    def change_second_color(self, color):
        self.guess[1] = color

    def change_third_color(self, color):
        self.guess[2] = color

    def change_fourth_color(self, color):
        self.guess[3] = color

    def confirm_guess(self):
        if None in self.guess:
            return False
        return True
