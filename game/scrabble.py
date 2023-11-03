from game.board import Board
from game.player import Player
from game.models import BagTiles
from game.dictionary import Dictionary


class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for index in range(players_count):
            self.players.append(Player(name= index +1))
        
        self.current_player = None
        self.turn = 0
        self.dict = Dictionary ()


    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        else:
            #index = index del current player + 1
            #len(self.players)
            index = self.players.index(self.current_player) 
            if index == len(self.players) - 1:
               self.current_player = self.players[0]
            else:
                self.current_player = self.players[index + 1]
            
    
    
        
            