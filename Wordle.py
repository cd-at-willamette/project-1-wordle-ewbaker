########################################
# Name: Evyn Baker
# Collaborators (if any): My Girlfriend and Calvin's slides
# GenAI Transcript (if any): used to troubleshoot syntax error, ChatGBT
# Estimated time spent (hr): 4 1/2
# Description of any added extensions: 
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR
from english import *  # ENGLISH_WORDS, is_english_word
import random

# ===================== Milestone 0: Display a Word ===================== #
# Puts a word on the given row in the game
def word_to_row(word: str, row: int):
    for col in range(len(word)):
        gw.set_square_letter(row, col, word[col].upper())  # Displays each letter in its spot

# ===================== Milestone 1: Get Guess and Validate ===================== #
# Grabs the word from the given row as a string
def row_to_word(row: int) -> str:
    return "".join(gw.get_square_letter(row, col).lower() for col in range(N_COLS))  # Turns the row of letters into a word

# Checks if the guessed word is in the word list
def check_guess(guess: str):
    return is_english_word(guess)  # Make sure it's a real word from the list

# ===================== Milestone 2: Color Letters in the Row ===================== #
# Colors the row based on how the guess matches the answer
def color_row(row: int, answer: str):
    guess = row_to_word(row)
    answer_letters = list(answer)

    # First, mark correct letters (green)
    for col in range(N_COLS):
        if guess[col] == answer[col]:
            gw.set_square_color(row, col, CORRECT_COLOR)
            answer_letters[col] = None  # Remove letter from further checking

    # Then, mark present (yellow) and missing (gray) letters
    for col in range(N_COLS):
        if guess[col] != answer[col]:
            if guess[col] in answer_letters:
                gw.set_square_color(row, col, PRESENT_COLOR)
                answer_letters[answer_letters.index(guess[col])] = None  # Mark this letter as used
            else:
                gw.set_square_color(row, col, MISSING_COLOR)

# ===================== Milestone 3: Random Word Selection ===================== #
# Picks a random 5-letter word with no repeated letters
def random_five_letter_word():
    words = [word for word in ENGLISH_WORDS if len(word) == 5 and len(set(word)) == len(word)]
    return random.choice(words)

# ===================== Milestone 5: Color Keyboard Keys ===================== #
# Colors the keyboard based on the guessed letters
def color_keys(guess: str, answer: str):
    for letter in guess:
        if letter in answer:
            gw.set_key_color(letter, PRESENT_COLOR if guess.count(letter) <= answer.count(letter) else MISSING_COLOR)
        if guess[guess.index(letter)] == answer[guess.index(letter)]:
            gw.set_key_color(letter, CORRECT_COLOR)

# ===================== Milestone 4: Handle Guess and Row Progression ===================== #
# Handles what happens when the player presses ENTER
def enter_action():
    current_row = gw.get_current_row()
    guess = row_to_word(current_row)

    if not check_guess(guess):
        gw.show_message("Not in word list")
        return

    # Update the grid with colors
    color_row(current_row, answer)
    color_keys(guess, answer)

    # Check if the word was guessed right or move to the next row
    if guess == answer:
        gw.show_message("You guessed the word!")
        gw.set_current_row(N_ROWS)  # End the game
    elif current_row < N_ROWS - 1:
        gw.set_current_row(current_row + 1)  # Move to the next row
    else:
        gw.show_message(f"The correct word was {answer}.")

# ===================== Main Function: Initialize the Game ===================== #
def wordle():
    global gw, answer
    answer = random_five_letter_word()  # Grab a random word
    print(f"The chosen word is: {answer}")  # For debugging, print the word

    # Start the Wordle game window
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# ===================== Startup Code ===================== #
# Start the game when the script runs
if __name__ == "__main__":
    wordle()
