import unittest
from game.player import Player
from game.models import BagTiles 
from game.models import Tile
from game.cell import Cell


class TetsPlayer(unittest.TestCase):

    def tests_init(self):
        player_1 = Player("player1")
        self.assertEqual(player_1.rack,[])
    
    def test_check_tile_in_hand(self):
    
        player = Player("")
        player.tiles = ["A", "B", "C", "D", "E"]
        self.assertEqual(player.check_tile_in_hand("B"), True)
        self.assertEqual(player.check_tile_in_hand("X"), False)

    def test_player_exchange(self):
        bag1 = BagTiles()
        player = Player("")
        player.rack = [Tile("A",1),Tile ("B",3),Tile ("C",2)]
        player.exchange_tiles(2,bag1)
        self.assertEqual(len(player.rack),3)
        self.assertEqual(len(bag1.tiles),28)


    
    def test_get_hand_size(self):
        
        player = Player("")
        player.tiles = ["A", "B", "C", "D", "E"]
        hand_size = player.get_hand_size()
        self.assertEqual(hand_size, 5)
    
    def test_view_points(self):
        player = Player(name = "Player 1")
        player.points = 15
        points = player.view_points()
        self.assertEqual(points, player.points)

    def test_view_tiles(self):
        player = Player(name='Player 1')
        player.tiles = [Tile('A', 1), Tile('B', 2), Tile('C', 3)]
        tiles = player.view_tiles()
        self.assertEqual(tiles, player.tiles)

#
    def take_tiles(self):
        bag1 = BagTiles()
        player = Player()
        player.take_tiles(3,bag1)
        self.assertEqual(len(player.rack),3)

    def test_set_joker_true(self):
        player = Player(name="Player1")
        player.rack = [Tile('A', 1), Tile('?', 0)]
        self.assertEqual(player.set_joker(), True)

    def test_set_joker_false(self):
        player = Player(name="Player1")
        player.rack = [Tile('A', 1), Tile('B', 2)]
        self.assertEqual(player.set_joker(), False)
    
    def test_find_joker(self):
        player = Player(name="Player1")
        player.rack = [Tile('A', 1), Tile('B', 2), Tile('?', 0)]
        self.assertEqual(player.find_joker(), 2)
    
    def test_no_find_joker(self):
        player = Player(name="Player1")
        player.rack = [Tile('A', 1), Tile('B', 2)]
        self.assertEqual(player.find_joker(), False)
#
    def test_validate_rack_true(self):
        player_1 = Player("")
        tiles = [Tile("H",1),Tile("O",1),Tile("L",1),Tile("A",1)]
        player_1.rack = [Tile("H",1),Tile("O",1),Tile("L",1),Tile("A",1), Tile("Z",1), Tile("Z",1), Tile("Z",1)]
        is_valid = player_1.set(tiles)
        assert is_valid == True
    
    def test_validate_rack_false(self):
        player_1 = Player("")
        tiles = [Tile("H",1),Tile("O",1),Tile("L",1),Tile("A",1)]
        player_1.rack = [Tile("H",1),Tile("O",1),Tile("E",1),Tile("A",1), Tile("Z",1), Tile("Z",1), Tile("Z",1)]
        is_valid = player_1.set(tiles)
        assert is_valid == False
    
    
        





if __name__ == '__main__':
    unittest.main()