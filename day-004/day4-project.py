## Day 4 - Randomisation and Python Lists
## 01.06.2023
## ----
## DAY 4 PROJECT Rock Paper Scissors
## ----

## Reference for ASCII figures: https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe

import random

print('Welcome to Rock, Paper, Scissors Game!')
options = ['rock', 'paper', 'scissors']

player_move = input("What's your move?: ")

if player_move.lower() == options[0]:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif player_move.lower() == options[1]:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif player_move.lower() == options[2]:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
else:
    print("Not defined move! It can be rock, paper & scissors!")

computer_move = random.choice(options)
print('Computer move is: ')
if computer_move.lower() == options[0]:
    print(""" Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif computer_move.lower() == options[1]:
    print(""" Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
else:
    print(""" Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

if player_move.lower() == computer_move:
    print('Deal!')
elif ((player_move.lower() == options[0] and computer_move == options[2]) or
      (player_move.lower() == options[1] and computer_move == options[0]) or
       (player_move.lower() == options[2] and computer_move == options[1])) :
    print('You win!!')
else:
    print('You lose!')