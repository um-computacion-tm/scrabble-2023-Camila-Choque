from game.models import Tile


class Cell:
    def __init__(self, multiplier, multiplier_type):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = None

    def add_letter(self, letter:Tile):
        self.letter = letter

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        else:
            return self.letter.value

    def calculate_total_value(cells):
        total_value = 0
        for cell in cells:
            if cell.letter is not None:
                total_value += cell.calculate_value()
        return total_value