from main import Main 
from game.models import Tile

def test_valid_player_count(self,mock_input):
        main = Main()
        number = "2"
        self.assertEqual(main.valid_player_count(number), True)
        
def test_take_turn_player_play(self, mock_input, mock_print, mock_object):
        main = Main()
        main.game.next_turn()
        player = main.game.current_player
        player.rack = [Tile('H', 4), Tile('O', 1), Tile('L', 1), Tile('A', 1)]
        main.take_turn()