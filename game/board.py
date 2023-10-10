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
        
"""""
    def place_tiles(self, tiles, coordinates_x,coordinates_y):
       
        if len(tiles) != len(coordinates):
            print("La cantidad de fichas y coordenadas no coincide.")
            return False

        for tile, (row, col) in zip(tiles, coordinates):
             #Verificar si la casilla está vacía
            if self.is_empty(row, col):
                # Colocar la ficha en la casilla
                self.grid[row][col].set_tile(tile)
            else:
                print(f"La casilla en ({row}, {col}) ya está ocupada.")
                return False

        return True
"""""
