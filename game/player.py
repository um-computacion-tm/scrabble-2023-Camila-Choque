
from game.models import BagTiles

class Player:
    def __init__(self,name):
        self.name = name
        self.rack = []
        self.points = 0
        


    def exchange_tiles(self,index,bag=BagTiles):
        index = index - 1
        tile_to_exchange = self.rack.pop(index)
        new_tile = bag.take(1)
        bag.put([tile_to_exchange])
        self.rack.insert(index, new_tile)
    

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

