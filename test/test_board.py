import unittest
from game.board import Board


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


class TestPlaceTiles(unittest.TestCase):
    def setUp(self):
        # Crea una instancia de la clase Board para cada prueba
        self.board = Board()

    


if __name__ == '__main__':
    unittest.main()
