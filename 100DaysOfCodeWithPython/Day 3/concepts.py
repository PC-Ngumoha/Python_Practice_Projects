"""
Day 3:

- Control flow:
    - if / else statement
    - nested if statements and elif
    - Logical operators

"""
"""
if / else statements syntax:

if condition:
    do this
else:
    do this
"""
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm ? "))
#
# if height >= 120:
#     print("You can go ahead to the rollercoaster")
# else:
#     print("Sorry, you need to grow a bit taller for this ride 🤭")
#

""" Modulo Operator
"""
# print("Welcome to Even Odds")
# number = int(input("Enter any number: "))
#
# if number % 2 == 0:
#     print(f'{number} is an even number.')
# else:
#     print(f'{number} is an odd number.')


"""
Nested if / else statement:

if condition:
    if another_condition:
        do this
else:
    do this
"""
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm ? "))
#
# if height >= 120:
#     print("You can go ahead to the rollercoaster")
#     age = int(input("What is your age ?"))
#     if age <= 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12")
# else:
#     print("Sorry, you need to grow a bit taller for this ride 🤭")

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
#
# bill = 0
# if size == "S":
#     bill = 15
# elif size == "M":
#     bill = 20
# elif size == "L":
#     bill = 25
# else:
#     print("You selected the wrong inputs.")
#
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is: ₦{bill}.")

""" Logical Operators

- and : both conditions are True, so everything evaluates to True i.e True and True = True
- or : one of the conditions is True, so everything evaluates to True i.e True or False = True
- not: reverses / flips the result of a conditional i.e True = False

"""
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm ? "))

if height >= 120:
    print("You can go ahead to the rollercoaster")
    age = int(input("What is your age ? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    elif 45 <= age <= 55:
        print("You can ride for free ($0)")
    else:
        print("Please pay $12")
else:
    print("Sorry, you need to grow a bit taller for this ride 🤭")