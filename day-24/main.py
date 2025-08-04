"""
main.py
"""
# Opening a file
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()  # Necessary because it frees up computer resources.

# 2nd approach:
with open('my_file.txt', mode='a') as file:
    file.write("New text,")


