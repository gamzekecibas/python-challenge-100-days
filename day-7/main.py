## Day 7 - Beginner | Hangman
## 04.06.2023
## Exercises

## Step 0 : Drawing Flow Chart for Hangman

import random
from hangman_words import course_word_list
from hangman_art import logo, stages
print(logo)

end_of_game = False
lives = len(stages)

selected_word = []
rand_word = random.choice(course_word_list).lower()

rand_word_len = len(rand_word)    ### For Step 2
selected_word += '_'*rand_word_len
print(selected_word)

while end_of_game != True:
    guess_letter = input('\nGuess a letter: ').lower()

    for letter_idx in range(rand_word_len):                            ## For Step 1
        if rand_word[letter_idx] == guess_letter:
            selected_word[letter_idx] = guess_letter
    print(selected_word)

    if guess_letter not in rand_word:
        print(f'You lose a life! You have extra {lives-1}')
        print(stages[lives - 1])
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lose!')
            print(f'Target word is {rand_word}')
            print(selected_word)

    if '_' not in selected_word:
        end_of_game = True
        print('You win')
