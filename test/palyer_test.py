import unittest
from game.games_player import Player


class TetsPlayer(unittest.TestCase):
    def tests_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,


         )
        





if __name__ == '__main__':
    unittest.main()