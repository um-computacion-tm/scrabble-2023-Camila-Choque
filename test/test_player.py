import unittest
from game.player import Player
from game.models import BagTiles 
from game.models import Tile


class TetsPlayer(unittest.TestCase):
    def tests_init(self):
        bag = BagTiles()
        player_1 = Player("player1", bag)
        self.assertEqual(
            len(player_1.tiles), 0,)
        
        
    def test_draw_tile(self):
        bag = BagTiles()
        player = Player("", bag)
        player.draw_tiles(bag, 1)
        self.assertNotIn("A", player.tiles)


    def test_exchange_tiles(self):
        player = Player("", BagTiles())
        bag_tiles = BagTiles()

        player.draw_tiles(bag_tiles, 4)

        initial_bag_count = len(bag_tiles.tiles)
        initial_player_count = len(player.tiles)

        tiles_to_exchange = player.tiles[:2]
        player.exchange_tiles(bag_tiles, tiles_to_exchange)

        self.assertEqual(len(player.tiles), initial_player_count - 2)

        self.assertEqual(len(bag_tiles.tiles), initial_bag_count + 2)
        


    def test_check_tile_in_hand(self):
    
        player = Player("", BagTiles())
        player.tiles = ["A", "B", "C", "D", "E"]
        self.assertEqual(player.check_tile_in_hand("B"), True)
        self.assertEqual(player.check_tile_in_hand("X"), False)

    
    def test_get_hand_size(self):
        
        player = Player("", BagTiles())
        player.tiles = ["A", "B", "C", "D", "E"]
        hand_size = player.get_hand_size()
        self.assertEqual(hand_size, 5)
    
    def test_view_points(self):
        player = Player(name = "Player 1", bag_tiles= "")
        player.points = 15
        points = player.view_points()
        self.assertEqual(points, player.points)

    def test_view_tiles(self):
        player = Player(name='Player 1', bag_tiles="")
        player.tiles = [Tile('A', 1), Tile('B', 2), Tile('C', 3)]
        tiles = player.view_tiles()
        self.assertEqual(tiles, player.tiles)


        





if __name__ == '__main__':
    unittest.main()