"""
Day 8:
- Functions with inputs
"""
# Normal function
def greet():
    print("Hello Abuja")
    print("Hello Nigeria")
    print("Hello World")

# greet()

# Function that accepts inputs
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"{name}, wetin be your favorite food ?")
    print("You dey into coding ?")


# greet_with_name("Lukman")

"""
Parameters: The name of the data that's being passed in

Argument: The actual piece of data being passed in.
"""

# Functions with more than one input.
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is like in {location} ?")

greet_with("Chukwuemeka", "Abuja, Nigeria")