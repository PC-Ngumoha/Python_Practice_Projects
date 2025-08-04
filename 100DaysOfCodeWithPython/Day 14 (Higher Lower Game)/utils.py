import os

def clear_terminal():
    """Clears terminal display on Windows, MacOS and Linux."""
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For MacOS and Linux
    else:
        os.system('clear')

def format_data(option):
    """Takes option data and returns a readable format."""
    option_name = option['name']
    option_desc = option['description']
    option_country = option['country']

    return f"{option_name}, a {option_desc}, from {option_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Determines if the user made the right guess."""
    if a_followers > b_followers:
        return user_guess == 'A'
    else:
        return user_guess == 'B'
