## Day 5 - Python Loops
## 02.06.2023
## ----
## DAY 5 PROJECT Password Generator
## ----

import string
import random

print('Welcome to the PyPassword Generator!')
num_letters = int(input('How many letters would you like in your password?: '))
num_symbols = int(input('How many symbols would you like?: '))
num_numbers = int(input('How many numbers would you like?: '))

uppercase_letters = list(string.ascii_uppercase)
lowercase_letters = list(string.ascii_lowercase)

all_letters = uppercase_letters + lowercase_letters
random.shuffle(all_letters)
all_symbols = [char for char in string.punctuation]
random.shuffle(all_symbols)
all_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
random.shuffle(all_numbers)

password_list = []

for letter_idx in range(num_letters):
    password_list.append(random.choice(all_letters))
random.shuffle(password_list)
for symbol_idx in range(num_symbols):
    password_list.append(random.choice(all_symbols))
random.shuffle(password_list)
for num_idx in range(num_numbers):
    password_list.append(random.choice(all_numbers))
random.shuffle(password_list)

print('The generated password is: ', ''.join(password_list))