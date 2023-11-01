
from game.models import BagTiles
class Player:
    def __init__(self,name, bag_tiles):
        self.name = name
        self.bag_tiles = bag_tiles
        self.tiles = []
        self.points = 0
        

    def draw_tiles(self, bag, num_tiles):
        if num_tiles <= len(bag.tiles):
            self.tiles.extend(bag.tiles[:num_tiles])
            del bag.tiles[:num_tiles]

    def exchange_tiles(self, bag, tiles_to_exchange):
        if all(tile in self.tiles for tile in tiles_to_exchange):
            bag.tiles.extend(tiles_to_exchange)
            self.tiles = [tile for tile in self.tiles if tile not in tiles_to_exchange]

            return True
        else:
            return False
  
    def check_tile_in_hand(self, tile):
       return tile in self.tiles
   
   
    def get_hand_size(self):
        return len(self.tiles)

    def view_points(self):
        return self.points
    
    def view_tiles(self):
        return self.tiles[:]
#

    def take_tiles(self,amount,bag=BagTiles):
        for _ in range(amount):
            self.rack.append(bag.take(1))
    
    def set(self, tiles):
        rack = set(tile.letter for tile in self.rack) 
        return set(tile.letter for tile in tiles).issubset(rack) 
    
    def set_joker(self):
        for tile in self.rack:
            if tile.is_joker() is True:
                return True
        return False
    
    def find_joker(self):
        for i, tile in enumerate(self.rack):
            if tile.is_joker() is True:
                return i
        return False

