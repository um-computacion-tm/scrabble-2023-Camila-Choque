import unittest
from game.board import Board
from game.models import Tile



class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )

    def test_word_inside_board(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        assert word_is_valid == True
    
    def test_place_tiles(self):
        board = Board()
        tile = Tile("A",1)
        self.assertTrue(board.place_tiles(7,7,tile))
        self.assertFalse(board.place_tiles(7,7,tile)) 


    def test_validate_word(self):
        board = Board()
        tile_a = Tile('A', 1)
        tile_b = Tile('B', 2)
        tile_c = Tile('C', 3)

        board.place_tiles(7, 7, tile_a)
        board.place_tiles(7, 8, tile_b)
        board.place_tiles(7, 9, tile_c)

        self.assertTrue(board.validate_word(7, 7, 'ABC', 'Horizontal'))
        self.assertFalse(board.validate_word(7, 7, 'ACB', 'Horizontal'))
        self.assertTrue(board.validate_word(7, 7, 'A', 'Vertical'))
        self.assertFalse(board.validate_word(7, 7, 'AB', 'Vertical'))


    def test_place_word_horizontal(self):
        board = Board()
        word = "Calcular"
        location = (7, 4)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == True
    
    def test_word_inside_board_vertical(self):
        board = Board()
        word = "Facultad"
        location = (4, 5)  # Ubicación dentro del tablero
        orientation = "Vertical"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        self.assertTrue(word_is_valid)
    
    """""
    def test_place_word_empty_board_vertical_fine(self):
        board = Board()
        word = "Facultad"
        location = (4, 7)
        orientation = "Vertical"

        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True

    def test_place_word_empty_board_vertical_wrong(self):
        board = Board()
        word = "Facultad"
        location = (4, 2)
        orientation = "Vertical"

        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False

    """""
if __name__ == '__main__':
    unittest.main()
