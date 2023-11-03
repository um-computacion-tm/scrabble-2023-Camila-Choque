import unittest
from game.models import (BagTiles,Tile)
from unittest.mock import patch


class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)

    def test_is_joker(self):
        tile = Tile("?",0)
        self.assertEqual(tile.is_joker(),True)

    def  test_convert_tile(self):
        tile = Tile("A",1)
        tile.convert_tile("B",2)
        self.assertEqual(tile.letter,"B")
        self.assertEqual(tile.value,2)




class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')

    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(
            len(bag.tiles),
            28,
        )
        self.assertEqual(
            patch_shuffle.call_count,
            1,
        )
        self.assertEqual(
            patch_shuffle.call_args[0][0],
            bag.tiles,
        )


    def test_take(self):
        bag = BagTiles()
        initial_tiles_count = len(bag.tiles)  
        tiles = bag.take(2)
        self.assertEqual(
            len(bag.tiles),
            initial_tiles_count - len(tiles), 
        )
        self.assertEqual(
            len(tiles),
            2,
        )

    def test_put(self):
        bag = BagTiles()
        put_tiles = [Tile('Z', 1), Tile('Y', 1)]
        initial_tiles_count = len(bag.tiles) 
        bag.put(put_tiles)
        self.assertEqual(
            len(bag.tiles),
            initial_tiles_count + len(put_tiles), 
        )

    def test_initial_tiles(self):
        bag = BagTiles()
        self.assertEqual(len(bag.tiles), 28)
        bag.initial_tiles()
        self.assertEqual(len(bag.tiles), 100)




if __name__ == '__main__':
    unittest.main()