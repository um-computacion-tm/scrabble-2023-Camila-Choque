class Board:
    def __init__(self):
        self.grid = [
            [ None for _ in range(15) ]
            for _ in range(15)
        ]

        ######ARREGLAR

    #def place_tiles(self, tiles, coordinates):
       
        #if len(tiles) != len(coordinates):
            #print("La cantidad de fichas y coordenadas no coincide.")
            #return False

        #for tile, (row, col) in zip(tiles, coordinates):
            # Verificar si la casilla está vacía
            #if self.is_empty(row, col):
                # Colocar la ficha en la casilla
             #   self.grid[row][col].set_tile(tile)
            #else:
             #   print(f"La casilla en ({row}, {col}) ya está ocupada.")
              #  return False

        #return True