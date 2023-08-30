import unittest
from game.player import Player
from game.models import BagTiles


class TetsPlayer(unittest.TestCase):
    def tests_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,

         )
        
        
    def test_draw_tile(self):
        player = Player()
        player.draw_tile("B")
        self.assertNotIn("A", player.hand)


    def test_exchange_tiles(self):
        player = Player()
        bag_tiles = BagTiles()

        player.draw_tiles(bag_tiles, 4)

        initial_bag_count = len(bag_tiles.tiles)
        initial_player_count = len(player.tiles)

        tiles_to_exchange = player.tiles[:2]
        player.exchange_tiles(bag_tiles, tiles_to_exchange)

        self.assertEqual(len(player.tiles), initial_player_count - 2)

        self.assertEqual(len(bag_tiles.tiles), initial_bag_count + 2)


    def test_check_tile_in_hand(self):
    
        player = Player()
        player.tiles = ["A", "B", "C", "D", "E"]
        self.assertEqual(player.check_tile_in_hand("B"), True)
        self.assertEqual(player.check_tile_in_hand("X"), False)

    
    def test_get_hand_size(self):
        
        player = Player()
        player.tiles = ["A", "B", "C", "D", "E"]
        hand_size = player.get_hand_size()
        self.assertEqual(hand_size, 5)



        





if __name__ == '__main__':
    unittest.main()