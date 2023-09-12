import unittest
from game.models import (BagTiles,Tile)
from unittest.mock import patch


class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)


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

    def initial_tiles(self):
        expected_tiles_count = {
            'A': 11, 'E': 11, 'O': 8, 'I': 5, 'S': 5, 'N': 4, 'L': 3,
            'R': 4, 'U': 4, 'T': 3, 'D': 4, 'G': 1, 'C': 3, 'B': 1,
            'M': 1, 'P': 3, 'H': 1, 'Ñ': 8, 'F': 4, 'Y': 4, 'V': 4,
            'CH': 5, 'Q': 5, 'J': 8, 'LL': 8, 'X': 8, 'Z': 10,
            'RR': 8,  
        }




if __name__ == '__main__':
    unittest.main()