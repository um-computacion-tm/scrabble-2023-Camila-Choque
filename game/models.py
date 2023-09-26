import random

class JokerA(Exception):
    pass 

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

    
class joker():  
    def __init__(self):
        self.letter = "*"
        
     #Cambia la letra de un objeto de la clase 
    def joker(self, new_letter):
        if self.letter == "*":
            self.letter = new_letter
        else:
            raise JokerA(Exception)


class BagTiles:
    #Constructor
    def __init__(self):
        self.tiles = [
            Tile('A', 1),
            Tile('E', 1),
            Tile('O', 1),
            Tile('I', 1),
            Tile('S', 1),
            Tile('N', 1),
            Tile('L', 1),
            Tile('R', 1),
            Tile('U', 1),
            Tile('T', 1),
            Tile('D', 2),
            Tile('G', 2),
            Tile('C', 3),
            Tile('B', 3),
            Tile('M', 3),
            Tile('P', 3),
            Tile('H', 4),
            Tile('F', 4),
            Tile('V', 4),
            Tile('Y', 4),
            Tile('CH', 5),
            Tile('Q', 5),
            Tile('J', 8),
            Tile('LL', 8),
            Tile('Ñ', 8),
            Tile('RR', 8),
            Tile('X', 8),
            Tile('Z', 10),
        ]
        random.shuffle(self.tiles)

    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.tiles.pop())
        return tiles
    
    def put(self, tiles):
        self.tiles.extend(tiles)

    def initial_tiles(self):
        # Diccionario con las fichas iniciales y sus cantidades
        initial_tiles = {
            'A': 6
            , 'E': 9, 'O': 6, 'I': 3, 'S': 3, 'N': 2, 'L': 1,
            'R': 2, 'U': 2, 'T': 1, 'D': 2, 'G': 1, 'C': 2, 'B': 1,
            'M': 1, 'P': 3, 'H': 1, 'Ñ': 2, 'F': 4, 'Y': 2, 'V': 2,
            'CH': 2, 'Q': 2, 'J': 4, 'LL': 1, 'X': 1, 'Z': 2,
            'RR': 4,  
        }
        for letter, count in initial_tiles.items():
            self.tiles.extend([letter] * count)

        # Agregar las fichas predeterminadas a la bolsa
        #self.tiles.extend(self.default_tiles)
    """
        # Crear una lista para almacenar las fichas adicionales necesarias
        total = []

        # Crear un diccionario para contar cuántas fichas de cada letra tenemos en la bolsa actualmente
        current_tiles_count = {letter: 0 for letter in initial_tiles.keys()}

        # Contar las fichas actuales en la bolsa
        for tile in self.tiles:
            current_tiles_count[tile.letter] += 1"""