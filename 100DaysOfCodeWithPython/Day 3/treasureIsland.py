"""
treasureIsland.py

Simple word-based adventure game in Python
"""
print('''
 *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Left or Right
choice = input("""You're at a cross road. 
Where do you want to go?\n\t Type \"left\" or \"right\"
""")
if choice == "left":
    # Wait or Swim
    choice = input("""You've come to a lake. There is an island in the middle of the lake.
    \n\t Type \"wait\" to wait for a boat. Type \"swim\" to swim to the island
    """)
    if choice == "wait":
        # Red, Yellow or Blue Doors
        choice = input("""You arrive at the island unharmed. There is a house with 3 doors.
        \n\tOne red, one yellow and one blue. Which color do you choose ?
        """)
        if choice == "yellow":
            print("You found Treasure ! You Win !!!")
        elif choice == "red":
            print("You got burned to death ! Game Over !!!")
        elif choice == "blue":
            print("Oops! You got eaten by a tiger 🐯. Game Over !!!")
        else:
            print("Game Over !!!")
    elif choice == "swim":
        print("Oops! You swam into a pack of trouts and they ate out your liver.\n\tGame Over !!!")
    else:
        print("Game Over !!!")
elif choice == "right":
    print("You fell into a hole.\n\tGame Over !!!")
else:
    print("Game Over !!!")