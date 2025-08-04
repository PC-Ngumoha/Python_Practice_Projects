"""calculator.py

Simple calculator program
"""
import art

# TODO: Write out the four basic operations: add, subtract, multiply and divide.
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these four operations as the values in a dictionary where the keys are: "+", "-", "*" and "/"
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# TODO: Use the dictionary operations to multiply 4 by 8
# print(f"4 * 8 = {operations["*"](4, 8)}")

print(art.logo)

def calculator():
    continue_calc = True
    num1 = float(input("What's the first number? "))
    while continue_calc:
        print("Available operations:")
        for symbol in operations:
            print(symbol)
        op_pick = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))

        if op_pick in operations:
            answer = operations[op_pick](num1, num2)
        else:
            op_pick = 'undefined'
            answer = 0.0

        print(f"{num1} {op_pick} {num2} = {answer} ")

        choice = input(f"Type 'y' to continue calculating with {answer}, or 'n' for a new calculation: ")
        if choice == 'y':
            num1 = answer
        else:
            continue_calc = False
            print('\n' * 100)
            # HER Approach: Used recursive function to implement looping functionality.
            calculator()


calculator()

# MY Approach: Used a second infinite loop to rerun program continuously
# while True: # infinite loop
#     calculator()
