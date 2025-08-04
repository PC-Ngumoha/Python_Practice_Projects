"""
Higher-Lower Game
"""
import random
from game_data import data
from art import vs, logo
from utils import clear_terminal, format_data, check_answer

options = {'A': random.choice(data), 'B': random.choice(data)}

if options['A'] == options['B']:
    options['B'] = random.choice(data)

score = 0
game_over = False
selected_options = []

clear_terminal()
print(logo)
# TODO-1: Loop the program
while not game_over:
    print(f'Compare A: {format_data(options['A'])}')
    print(vs)
    print(f'Against B: {format_data(options['B'])}')
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    is_correct = check_answer(
        guess,
        options['A']['follower_count'],
        options['B']['follower_count']
    )
    # TODO-2: If user selects correct option, increase score, then set optionA to optionB
    if is_correct:
        score += 1
        options['A'] = options['B']

        # Continue searching until a new option is found
        while True:
            option_id = random.randint(0, int(len(data) - 1))
            if option_id not in selected_options:
                selected_options.append(option_id)
                break

        options['B'] = data[option_id]
        clear_terminal()
        print(logo) # Print Logo
        print(f"You're right! Current score: {score}.")
    else:
        # TODO-3: End game when user gets it wrong.
        clear_terminal()
        print(logo) # Print Logo
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True