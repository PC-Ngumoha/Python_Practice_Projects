"""
day 26: List & Dictionary comprehensions
"""

"""
Iterating through a pandas data frame

for (index, row) in data_frame.iterrows():
    print(f'{index}: {row}')
"""

# NATO Alphabet Program

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet = {letter:code for (_, (letter, code)) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter text: ").upper()
result = [nato_alphabet[letter] for letter in user_input if letter != ' ']
print(result)
