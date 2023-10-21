# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.0.1] - 2023-08-27

### Added
      
    -Implemented the Tile class to represent a Scrabble tile with letters and values.
    -Implemented the BagTiles class to represent the Scrabble tile bag.
    -The tile bag is initialized with all Scrabble tiles and shuffled randomly.
    -Provided a take(count) method to take a specified number of tiles from the bag.
    -Provided a put(tiles) method to return tiles to the bag.
    
## [0.0.2] - 2023-08-27

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
    

## [0.0.3] - 2023-08-28

### Added

    -Implemented the Cell class to represent a cell on a word game board (e.g., Scrabble).
    -Each cell holds information about the multiplier and multiplier type (multiplier and multiplier_type) applied to tiles placed on it.
    -Cells can hold a letter (letter) if a tile is placed on them.
    -Provided an add_letter(letter: Tile) method to add a letter to the cell.
    -Provided a calculate_value() method to calculate the value of the cell, considering the multiplier type and the letter contained in it.

## [0.0.4] - 2023-08-28

### Added

   -Added the draw_tile method to the Player class to allow players to draw tiles and add them to their hand.
   -Added the test_draw_tile test case to the TestPlayer test suite.
   -Created an instance of the Player class for testing.
   -Added a tile "B" to the player's hand using the draw_tile method.
   -Verified that the tile "A" is not present in the player's hand using the self.assertNotIn assertion.

## [0.0.5] - 2023-08-29

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
   
## [0.0.6] - 2023-08-29

### Added
    
    -Implemented the check_tile_in_hand method in the Player class.
    -This method allows players to check if a specific tile is present in their hand.
    -A test for this method was created.
    -Implemented the get_hand_size method in the Player class.
    -This method allows players to retrieve the current size of their hand, i.e., how many tiles they have in their hand at a given moment.
    -A test for this method was created.
    
## [0.0.7] - 2023-09-06

### Added
  
    
    -Implemented the next_turn method in the ClassName class to switch to the next player in the game's turn.
    -If the current player is None, it is set as the first player in the list of players.
    -If there is already a current player, it switches to the next player in the list of players.
    -A test for this method was created.
    -There are tests left to correct.
    
## [0.0.8] - 2023-09-07

### Added
   
    -Implemented the place_tiles method in the Board class to allow the placement of tiles on the Scrabble board.
 
    
## [0.0.9] - 2023-09-08

### Added
   
   -Created the TestPlaceTiles class for performing unit tests of the place_tiles function in the 
   Board class (Modifications must be   made.).
   
## [0.0.10] - 2023-09-10

### Added
    
    -Implemented the initial_tiles function to define initial tiles and their quantities in the Spanish Scrabble game.
    
## [0.0.11] - 2023-09-11

### Added

    -Created the initial_tiles test to verify that the initial tile counts match expectations in the Spanish Scrabble game.
    -Defined the expected_tiles_count dictionary containing the expected quantities of initial tiles 
    for each letter and combination in the game.
    -The test verifies if the initial_tiles function provides results that match the expected counts in expected_tiles_count.
    -The parts marked with the symbol '#' are being corrected.

## [0.0.12] - 2023-09-12

### Added
    
    -Implemented the code to perform tile counting within a letter bag.
    -Created an empty list called 'total' to store the additional tiles needed.
    -Established a dictionary named 'current_tiles_count' to keep track of how many tiles of each letter are currently present in the bag.
    
## [0.0.13] - 2023-09-13 

### Added  
    
    -Added the `validate_word_inside_board` function to validate if a word can be placed on the board.
    -The function handles validation of the word's location and orientation.
    -It checks if the orientation is "H" (horizontal) and if the word fits within the board in that direction.
    -Returns `True` if the word fits within the board in the horizontal orientation.
    -Added a provisional condition for vertical orientation that is still in development.
    -A test for this method was created.
    
### Changes

    -Modifications were made to the `__init__` function within the `board.py` file.
    
## [0.0.14] - 2023-09-18

### Added  
   
     -Added the joker method to the class.
     -The joker method allows changing the current letter of an object of the class if it is an asterisk ("*").
     -Implemented a Joker exception that is raised if an attempt is made to change the letter when it is not an asterisk.
     -If the Joker exception occurs, an error is raised that can be caught and handled in client code.
     
## [0.0.15] - 2023-09-19

### Added  
       
     -An "init" function was created for the "joker" class
     -Created a test class named TestJoker using the unittest module to test the functionality of the joker class.
     -Created a test case named test_joker_with_wildcard that verifies if the joker method of the joker class works correctly 
     when using a wildcard character ('*') to change the letter.
     -Created a test case named test_joker_without_wildcard that verifies if the joker method of the joker 
     class raises a JokerA exception when attempting to change the letter without using a wildcard character.
     

## [0.0.16] - 2023-09-20


### Added  
     
     -Created the calculate_total_value(cells) function to calculate the total value of a list of cells.
     -The function iterates through all cells, checks if they have a letter, and adds the value of the letter 
     (considering the multiplier if applicable) to the total value.

## [0.0.17] - 2023-09-25


### Added  

      - Added the `remove_letter` method to the `Cell` class to enable the removal of a letter tile from the cell.
      - The `remove_letter` method stores the letter tile to be removed in a `letter` variable.
      - After removal, the `letter` property of the cell is set to `None`.
      - The `remove_letter` method returns the removed letter for further processing.
      -A test for this method was created.
      

### Removed
     
     -The 'calculate_total_value' function was removed because there was a similar function
   
    
## [0.0.18] - 2023-09-26 


### Added    
    
      -A 'calculate_word_value' function was created, but it is unfinished.
      

## [0.0.19] - 2023-10-03


### Added    
      
      -Initial implementation of the `Dictionary` module.
      -remove_accents` and `verify_word` methods for word processing and verification against the word list.
      -Improved error handling in the `verify_word` method.
      -Performance optimization in word lookup.
      
      
## [0.0.20] - 2023-10-04


### Added    
       
      -Imported the unittest module to perform unit testing.
      -Imported the Dictionary class from the game.dictionary module to conduct tests on the dictionary.
      -Implemented four test methods in the TestDictionary class:

         1-test_simple_verify(): Checks if a simple word ("Casa") is present in the dictionary. Expected to pass.
         2-test_verify_false_word(): Verifies if a word not in the dictionary ("Kadabra") is correctly detected. Expected to pass.
         3-test_verify_word_with_accents(): Checks if a word with accents ("Cafè") is present in the dictionary. Expected to pass.
         4-test_verify_word_with_dieresis(): Checks if a word with dieresis ("Cigüeña") is present in the dictionary. Expected to pass.

## [0.0.21] - 2023-10-05


### Added    

      -The folder "dictionary_words.txt" was created.
      -All the words corresponding to the dictionary were added.


## [0.0.22] - 2023-10-09


### Added  
       
       -A folder named main.py was created, containing the game's initial code.
       -An initialization method was implemented to welcome the players.
       -The player_count method was added, allowing users to input the number of players (maximum 4) and validating the user's input.


## [0.0.23] - 2023-10-10


### Added  
      
      -Implemented the unit test test_place_tiles in the TestBoard class to evaluate the place_tiles function.
      -The test verifies the ability of the place_tiles function to place tiles at specified coordinates on the board.
      -Assertions are made to confirm that the function returns True when a tile is placed successfully and False when the 
       position is already occupied.
    
    
## [0.0.24] - 2023-10-11 


### Changed
      
     -Method modification: The place_tiles method was modified to enable tile placement on the board.
     -Added validations: The method checks whether the location_x and location_y coordinates are within the board boundaries 
      (between 0 and 14) before proceeding with the placement.
     -Cell validation implemented: It verifies if the cell at the specified location already contains a letter (cell.letter is None) 
      before adding a new letter to the board.
     -Boolean return value: If all conditions are met, the tile letter is added to the cell, and True is returned to 
      indicate successful placement. If any of the conditions are not met, False is returned to indicate unsuccessful placement. 
  
## [0.0.25] - 2023-10-18
    
### Added  
      
      -Added multiplier function to represent multipliers on the Scrabble game board.
      -Implemented a two-dimensional array to represent the distribution of multipliers on the game board.
      -Introduced the following types of multipliers:
         "3W": Triple word multiplier.
         "2W": Double word multiplier.
         "3L": Triple letter multiplier.
         "2L": Double letter multiplier.   
         
      
      -Introduced active_multipliers function to convert multiplier types into usable Cell objects in the game.
      -Now accepts a multiplier argument representing the multipliers on the game board.
      -Handles two types of multipliers: "W" for word and "L" for letter.
      -If the multiplier is None, it returns a null Cell object.
      
      -Implemented the __repr__ method in the Cell class to represent the state of the Cell object as a string.
    
## [0.0.26] - 2023-10-19
    
### Added 
      
      -Implemented the validate_word function.
      -Added support for validating words in both horizontal and vertical orientations on a 15x15 grid.
      -The function takes input parameters: starting coordinates (start_location_x, start_location_y), the word to validate 
       (word),and the orientation (orientation).
      -If the word can be placed on the grid without issues, the function returns True; otherwise, it returns False.
      -Implemented the test_validate_word function to perform word validation tests on the game board.
      -Implemented the test_place_word_horizontal function to conduct tests for placing words horizontally on the game board.
      -Created a game board instance.
      -Defined the word to be placed as "Calcular."
      -Specified the starting position as (7, 4) and the orientation as horizontal.
      -Checked the validity of the word and its placement on the board using the validate_word_inside_board function.
      
## [0.0.27] - 2023-10-20


### Added 
      
      -Implemented the validate_word_horizontal method in the existing class.
      -The method checks if a word can be placed horizontally at a specific location on the board.
      -The validate_word_inside_board method is invoked to ensure the word can be placed at the specified location horizontally on 
       the board.
      -The method returns True if a valid letter is found and the word can be placed at the specified location horizontally;
       otherwise, it returns False.
      -Implemented the validate_word_vertical method in the existing class.
      -The method checks if a word can be placed vertically at a specific location on the board.
      -Added the test_word_inside_board_vertical test case to validate word placement inside the board vertically.
      -Created a new instance of the Board class for testing purposes.
    
    
    
    
    
    
    
    
