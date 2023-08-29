import unittest
from game.player import Player


class TetsPlayer(unittest.TestCase):
    def tests_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,

         )
        
        

class TestPlayer(unittest.TestCase):
    def test_draw_tile(self):
        player = Player()
        player.draw_tile("B")
        self.assertNotIn("A", player.hand)


        





if __name__ == '__main__':
    unittest.main()