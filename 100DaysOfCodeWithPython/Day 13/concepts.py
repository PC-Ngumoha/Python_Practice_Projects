"""
Day 13: Debugging Techniques

Step 1: Describe the problem clearly. Testing your assumptions to see which is False.

Step 2: Reproduce the bug that you encountered. To discover when it and why it occurs.

Step 3: Play computer and evaluate the lines of code manually.

Step 4: Fixing errors and watching for red underlines. Understanding errors and then solving them.
    Using the exception handling mechanisms of the programming language

Step 5: Squash bugs with the print() function.

Step 6: Using a debugger

Final Tips:
- Take regular breaks
- Ask a real human for feedback. Any set of fresh eyes that could see through your errors
- Run your code often. Don't wait until you've writen all the code you had in mind.
- Use Stackoverflow or ChatGPT.
"""
## DESCRIBE THE PROBLEM
# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("Something")
#
# my_function()
# """
# The problem is that 'i' never gets to be equals to 20. The range function only iterates
# i from 1 to 19 and then terminates the loop. As a result, the if block is never called.
# """

# # REPRODUCE THE BUG
# from random import randint
# dice_images = ["1️⃣", "2️⃣", "3️⃣", "️4️⃣", "5️⃣", "6️⃣"]
# dice_num = randint(0, 5)
# print(dice_images[dice_num])

# # PLAY COMPUTER
# year = int(input("What's your year of birth? "))
#
# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year >= 1994:
#     print("You are a Gen Z.")
#
# """The problem is that both ends of the year range are not inclusive.
# """

# # FIXING ERRORS AND WATCHING FOR RED UNDERLINES.
# try:
#     age = int(input("How old are you? "))
# except ValueError:
#     print("You entered an invalid value. Please try again.")
#     age = int(input("How old are you? "))
#
# if age >= 18:
#     print(f"You can drive at age {age}.")

# # SQUASH BUGS USING THE PRINT() FUNCTION
#
# pages = int(input("Number of pages: "))
# # print(pages)
# word_per_page = int(input("Number of words per page: "))
# # print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)

# # USING A DEBUGGER
# import random
# import maths
#
#
# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1, 3)
#         new_item = maths.add(new_item, item)
#         b_list.append(new_item)
#     print(b_list)
#
# mutate([1, 2, 3, 5, 8, 13])

# CHALLENGE 3
# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

fizz_buzz(10)
