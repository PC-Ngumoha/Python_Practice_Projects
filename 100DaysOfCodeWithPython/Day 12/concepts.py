"""
Day 12:
- Scope: Local & Global Variables
"""
# Global Scope
enemies = 1

def increase_enemies():
    # Local Scope
    global enemies # enables us modify global variable values from within local scope
    # The above is not advised
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

"""
There is no such thing as a Block scope in Python.
Any variables declared in blocks is considered as belonging
to the same scope as the enclosing scope (function or otherwise)
"""

# Global constants
PI = 3.142