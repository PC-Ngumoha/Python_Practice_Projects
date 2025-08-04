"""
Caesar Cipher

Project to create a simple caesar cipher.
"""
import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, encode_or_decode):
    output = ''

    if encode_or_decode == 'decode':
        shift *= -1

    for char in text:
        if char not in alphabet:
            output += char
        else:
            shift_pos = (alphabet.index(char) + shift) % len(alphabet)
            output += alphabet[shift_pos]

    print(f'Here is the {encode_or_decode}d result: {output}')

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to continue. Otherwise, type 'no'\n").lower()
    should_continue = restart == 'yes'