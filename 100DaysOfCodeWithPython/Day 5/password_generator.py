"""
Password Generator
"""
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password_set = []

for _ in range(nr_letters):
    password_set.append(random.choice(letters))

for _ in range(nr_symbols):
    password_set.append(random.choice(symbols))

for _ in range(nr_numbers):
    password_set.append(random.choice(numbers))

print(password_set)
# print("".join(password_set))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# # My Approach
# randomized_set = []
# char_length = len(password_set)
# for _ in range(char_length):
#     char = random.choice(password_set)
#     randomized_set.append(char)
#     password_set.remove(char)
# print(randomized_set)
# print("".join(randomized_set))

# Course Approach
random.shuffle(password_set)
print(password_set)
print(f"My password is: {"".join(password_set)}")
