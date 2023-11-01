from game.models import Tile


class Cell:
    def __init__(self, multiplier , multiplier_type ):
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
        
    def remove_letter(self):
        letter = self.letter  # Guarda la letra que se va a eliminar
        self.letter = None  # Establece la propiedad letter en None después de la eliminación
        return letter  # Devuelve la letra eliminada
    
    def __repr__(self):
        if self.letter:
            return repr(self.letter)
        if self.multiplier > 1:
            return f'{"W" if self.multiplier_type == "word" else "L"}x{self.multiplier}'
        else:
            return
        
    def deactive_cell(self):
        self.status = 'desactive'

