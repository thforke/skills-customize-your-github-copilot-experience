
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

In this assignment, you will build a text-based Hangman game in Python. You will practice working with strings, loops, conditionals, and user input while creating a complete playable game.

## 📝 Tasks

### 🛠️	Create the Game Setup

#### Description
Set up the basic game data and starting state for Hangman. Define a list of possible words, randomly choose one secret word, and prepare the variables needed to track guessed letters and remaining attempts.

#### Requirements
Completed program should:

- Include a predefined list of words to choose from
- Randomly select one secret word at the start of the game
- Initialize remaining attempts with a fixed number
- Initialize tracking for guessed letters and current word progress


### 🛠️	Implement the Game Loop

#### Description
Build the main loop that asks the player for letter guesses and updates the game state. The game should reveal correct letters, decrease attempts for incorrect guesses, and stop when the player wins or loses.

#### Requirements
Completed program should:

- Prompt the user to guess one letter at a time
- Display current progress in the hidden word (for example: `_ _ n g m a n`)
- Reduce remaining attempts for incorrect guesses
- End with a clear win message when the word is fully guessed
- End with a clear lose message when attempts reach zero
