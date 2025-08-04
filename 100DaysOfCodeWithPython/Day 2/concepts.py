"""
Day 2:
- Data types in Python
- Type error, type checking and type conversion
- Math operations in Python
- Number manipulation and f-strings in Python
"""
# print(len(1234556))

# Subscripting
print("Hello"[-1])

# String Concatenation
print("123" + "456")

# Integer
print(123 + 456)
print(1_000_000) # Make larger numbers more readable

# Float
print(3.14159)

# Boolean
print(True)
print(False)

# Type checking
print(type("1123"))
print(type(1123))
print(type(1123.96))
print(type(True))

# Type conversion
print(int("234") + int("567"))

# print("Number of letters in your name: " + str(len(input("Enter your name: "))))

# Number manipulation
bmi = 84 / 1.68 ** 2

print(bmi)

print(int(bmi))

print(round(bmi))
print(round(bmi, 2))

# F-strings
score = 0
height = 1.72
is_winning = False

print(f'Your score is {score}, your height is {height} and you are{' ' if is_winning else ' not '}winning ')
