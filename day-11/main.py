## Day 11 - Beginner | Capstone Project: Blackjack
## 08.06.2023

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random

import random
from art import logo

# Global variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
game_over = False


def deal_card():
    """Returns a random card from the deck."""
    return random.choice(cards)


def calculate_score(hand):
    """Calculates and returns the score of a given hand."""
    # Check for blackjack (ace + 10)
    if sum(hand) == 21 and len(hand) == 2:
        return 0

    # Convert ace (11) to 1 if the score is over 21
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return sum(hand)


def compare(user_score, computer_score):
    """Compares the scores between the user and the computer to determine the winner."""
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Computer wins with a blackjack!"
    elif user_score == 0:
        return "You win with a blackjack!"
    elif user_score > 21:
        return "You went over 21. You lose!"
    elif computer_score > 21:
        return "Computer went over 21. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"


def play_game():
    """Plays a game of Blackjack."""
    global game_over  # Add this line to define game_over as a global variable

    # Clear the cards at the start of the game
    user_cards.clear()
    computer_cards.clear()

    # Deal the initial cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        # Check if the game should end
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            # Ask the user if they want to draw another card
            user_choice = input("Type 'y' to get another card, or 'n' to pass: ")
            if user_choice == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    # Let the computer play
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

print(logo)
while True:
    should_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if should_play == 'y':
        game_over = False
        play_game()
    else:
        break