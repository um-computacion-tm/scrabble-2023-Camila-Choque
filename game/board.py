from game.cell import Cell
class Board:
    def __init__(self):
        self.grid = [[Cell(1, "") for _ in range(15)] for _ in range(15)]

    

    def validate_word_inside_board(self, word, location, orientation):
        #WORK IN PROGRESS
        position_x = location[0]
        position_y = location[1]
        len_word = len(word)
        if orientation == "H":
            if position_x + len_word > 15:
                return False
            else:
                return True
        else:
            pass
        

    def place_tiles(self, location_x, location_y, tile):
        if 0 <= location_x < 15 and 0 <= location_y < 15:
            cell = self.grid[location_x][location_y]
            if cell.letter is None:
                cell.add_letter(tile)
                return True
        return False

