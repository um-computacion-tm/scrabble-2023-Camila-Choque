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



