# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

In this assignment, you will build a Hangman game in Python using strings, loops, and conditionals. You will practice handling user input and game state while creating a fun, interactive program.

## 📝 Tasks

### 🛠️	Build the Core Hangman Loop

#### Description
Create the main game loop for Hangman. The program should choose a random word, ask the player for letter guesses, and update the displayed progress after each guess.

#### Requirements
Completed program should:

- Randomly select one word from a predefined list.
- Accept one letter guess at a time from the user.
- Display the word progress using underscores for unknown letters (for example, `_ _ _ _`).
- Reveal correctly guessed letters in their correct positions.


### 🛠️	Handle Attempts and Game End Conditions

#### Description
Add rules for incorrect guesses and implement clear game ending messages. The game should stop when the player wins or uses all attempts.

#### Requirements
Completed program should:

- Track remaining attempts and reduce them only for incorrect guesses.
- End the game when all letters are guessed or attempts reach zero.
- Display a clear win message when the player guesses the word.
- Display a clear lose message with the correct word when attempts run out.
