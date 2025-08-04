"""
Rock, Paper, Scissors
"""
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
hand_moves = [rock, paper, scissors]

# print(random.choice(hand_moves))
# choice = random.choice(hand_moves)

index = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

player_choice = hand_moves[index]
print(player_choice)

computer_choice = random.choice(hand_moves)
print("Computer chose:")
print(computer_choice)

# Game logic - Defined in terms of possible player lose moves
if player_choice == computer_choice:
    print("It's a draw!")
elif player_choice == rock and computer_choice == paper \
        or player_choice == scissors and computer_choice == rock \
        or player_choice == paper and computer_choice == scissors:
    print("You lose!")
else:
    print("You win!")