# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.1] - 2023-08-27

### Added
      
    -Implemented the Tile class to represent a Scrabble tile with letters and values.
    -Implemented the BagTiles class to represent the Scrabble tile bag.
    -The tile bag is initialized with all Scrabble tiles and shuffled randomly.
    -Provided a take(count) method to take a specified number of tiles from the bag.
    -Provided a put(tiles) method to return tiles to the bag.

### Added
    
    -Implemented the ScrabbleGame class to represent a game of Scrabble.
    -Created a game board (Board) and a tile bag (BagTiles) upon initializing a game.
    -Allowed specifying the number of players when creating an instance of ScrabbleGame.
    -Created a list of players (players) with the specified number of players upon game instantiation.
    
    -Implemented the Board class to represent a game board for a word game (e.g., Scrabble).
    -Created a grid with dimensions 15x15, which is a common size for a standard Scrabble board.
    -Initialized the grid with None values to represent empty tiles or cells on the board.
    
    -Implemented the Player class to represent a player in the game.
    -Created a list of tiles (tiles) for the player upon initialization.
    

## [1.1.1] - 2023-08-28

### Added

    -Implemented the Cell class to represent a cell on a word game board (e.g., Scrabble).
    -Each cell holds information about the multiplier and multiplier type (multiplier and multiplier_type) applied to tiles placed on it.
    -Cells can hold a letter (letter) if a tile is placed on them.
    -Provided an add_letter(letter: Tile) method to add a letter to the cell.
    -Provided a calculate_value() method to calculate the value of the cell, considering the multiplier type and the letter contained in it.

### Added

   -Added the draw_tile method to the Player class to allow players to draw tiles and add them to their hand.
   -Added the test_draw_tile test case to the TestPlayer test suite.
   -Created an instance of the Player class for testing.
   -Added a tile "B" to the player's hand using the draw_tile method.
   -Verified that the tile "A" is not present in the player's hand using the self.assertNotIn assertion.

## [1.1.1] - 2023-08-29

### Added

    -The draw_tiles method takes two arguments: bag (an instance of the BagTiles class) and num_tiles (the number of tiles 
     the player wants  to draw from the bag).
    -The method checks if the requested number of tiles (num_tiles) is less than or equal to the number of tiles in the bag (bag.tiles).
    -If the condition is met, the method adds the specified tiles (num_tiles) to the player's hand (self.tiles) 
     using extend and then     removes those tiles from the bag using del bag.tiles[:num_tiles]
     -Modifications were made to the 'draw_tiles' test.
     
    -Added the exchange_tiles method to the Player class to facilitate tile exchange between a player and a bag of tiles.
    -The method takes two arguments: bag (an instance of the BagTiles class) and tiles_to_exchange (a list of tiles to exchange).
    -It checks if all the specified tiles in tiles_to_exchange are present in the player's hand (self.tiles).
    -If all the specified tiles are found, the method extends the bag with the exchanged tiles (tiles_to_exchange) 
     and removes these tiles from the player's hand.
    -The method returns True if the exchange is successful, indicating that the tiles were successfully exchanged.
    -If the condition is not met, it returns False, indicating that the exchange was not possible due to missing tiles in the player's hand.
    
### Added
    
    -Implemented the check_tile_in_hand method in the Player class.
    -This method allows players to check if a specific tile is present in their hand.
    -A test for this method was created.
    -Implemented the get_hand_size method in the Player class.
    -This method allows players to retrieve the current size of their hand, i.e., how many tiles they have in their hand at a given moment.
    -A test for this method was created.
    
## [1.1.1] - 2023-09-06

### Added
  
    
    -Implemented the next_turn method in the ClassName class to switch to the next player in the game's turn.
    -If the current player is None, it is set as the first player in the list of players.
    -If there is already a current player, it switches to the next player in the list of players.
    -A test for this method was created.
    -There are tests left to correct.
    
## [1.1.1] - 2023-09-07

### Added
   
    -Implemented the place_tiles method in the Board class to allow the placement of tiles on the Scrabble board.
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
