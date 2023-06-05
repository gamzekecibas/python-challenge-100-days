## Day 8 - Beginner | Function Parameters & Caesar Cipher
## 05.06.2023
## Exercises

## Exercise - 1: Paint Area Calculator
#Write your code below this line 👇
from math import ceil

def paint_calc(height, width, cover):
    num_cans =  (height * width) / cover
    print(f"You'll need {ceil(num_cans)} cans of paint.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

##Exercise - 2: Prime Number Checker
# Write your code below this line 👇

def prime_checker(number):
    res = []
    for div in range(2, 10):
        if number / div >= 1:
            res.append(number % div == 0)
    if number >= 10:
        if True in res:
            print("It's not a prime number.")
        else:
            print("It's a prime number.")
    else:
        if res.count(True) >= 2:
            print("It's not a prime number.")
        else:
            print("It's a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


