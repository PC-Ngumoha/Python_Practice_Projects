"""
main.py: Mail merge main codebase
"""
# TODO: Create a letter using starting_letter.txt
# For each name in invited_names.txt
with open('Input/Names/invited_names.txt', mode='r') as file:
    invited_names = file.read().split('\n')

# Replace the [name] placeholder with the actual name.
with open('Input/Letters/starting_letter.txt', mode='r') as file:
    starting_letter = file.read()

# Save the letters in the folder "ReadyToSend".
for name in invited_names:
    message = starting_letter.replace('[name]', name)
    with open(f'Output/ReadyToSend/Letter_To_{name}.txt', mode='w') as letter:
        letter.write(message)
