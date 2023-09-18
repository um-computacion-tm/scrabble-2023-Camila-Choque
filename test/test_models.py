import unittest
from game.models import (BagTiles,Tile)
from unittest.mock import patch
#from game.models import Joker


class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)
""""
class TestJoker(unittest.TestCase):
    def test_joker_with_wildcard(self):
        # Crea una instancia de JokerClass con el carácter comodín '*'
        joker_instance = Joker('*')

        # Llama a la función joker con una nueva letra
        joker_instance.Joker('A')

        # Verifica que el carácter comodín se haya actualizado a 'A'
        self.assertEqual(joker_instance.letter, 'A')

    def test_joker_without_wildcard(self):
        # Crea una instancia de JokerClass con una letra no comodín
        joker_instance = Joker('B')

        # Intenta llamar a la función joker con una nueva letra
        # Esto debería generar una excepción NotAJoker
        with self.assertRaises(Joker):
            joker_instance.Joker('C')
"""





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