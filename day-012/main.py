## Day 12 - Beginner | Scope & Number Guessing Game
## 09.06.2023

from art import logo
import random

def guess_game(ref_number, guess_number):
    if ref_number < guess_number:
        print("It's too high.\nGuess again.")
        new_guess_number = int(input("Make a guess: "))
    elif ref_number > guess_number:
        print("It's too low.\nGuess again.")
        new_guess_number = int(input("Make a guess: "))
    return new_guess_number

# Include an ASCII art logo.
print(logo)
# Allow the player to submit a guess for a number between 1 and 100.
print("I'm thinking of a number between 1 and 100.")
diff_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
ref_number = random.choice(range(1, 101))

if diff_level == 'hard':
    rights = 5
    print(f"You have {rights} attempts remaining to guess the number.")
    guess_number = int(input('Make a guess: '))
    if guess_number != ref_number:
        rights -= 1
        print(f"You have {rights} attempts remaining to guess the number.")
        while (rights != 0):
            guess_number = guess_game(ref_number, guess_number)
            if ref_number != guess_number:
                rights -= 1
                print(f"You have {rights} attempts remaining to guess the number.")
                if rights == 0:
                    print(f"The number is {ref_number}. You lose :(")
            else:
                print(f"You got it! The answer is {guess_number}.")
                break
else:
    rights = 10
    print(f"You have {rights} attempts remaining to guess the number.")
    guess_number = int(input('Make a guess: '))
    if guess_number != ref_number:
        rights -= 1
        print(f"You have {rights} attempts remaining to guess the number.")
        while (rights != 0 or ref_number == guess_number):
            guess_number = guess_game(ref_number, guess_number)
            if ref_number != guess_number:
                rights -= 1
                print(f"You have {rights} attempts remaining to guess the number.")
                if rights == 0:
                    print(f"The number is {ref_number}. You lose :(")
            else:
                print(f"You got it! The answer is {guess_number}.")
                break

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

