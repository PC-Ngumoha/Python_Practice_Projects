import random

from hangman_words import word_list
from hangman_art import logo as game_logo, stages, you_win, you_lose, letter_already_typed, letter_not_in_word

# GAME VARIABLES
game_over = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

print(game_logo)

display = []
for _ in chosen_word:
    display.append('_')

print("".join(display))

# GAME LOOP
while not game_over:
    guess = input("Guess a letter: ").lower()

    # Already guessed that letter ?
    if guess in display:
        print(letter_already_typed(guess))

    # Fill in correct guesses
    for i in range(word_length):
        if chosen_word[i] == guess:
            display[i] = chosen_word[i]

    # Handle wrong guesses and give user feedback
    if guess not in chosen_word:
        print(letter_not_in_word(guess))
        lives -= 1

        # Game Over, You Lose
        if lives == 0:
            game_over = True
            print(you_lose)
            print(f"The correct word is: \033[91m{chosen_word}\033[0m") # chosen_word in red

    print("".join(display))

    # Congrats, You Win
    if '_' not in display:
        game_over = True
        print(you_win)

    print(stages[lives])