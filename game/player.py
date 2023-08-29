
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []


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

    





