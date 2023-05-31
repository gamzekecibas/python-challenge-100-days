## Day 3 - Conditional Operators
## 31.05.2023
## Exercises

## Conditional Operators
## ---

## Odd or Even Exercise
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

## BMI 2.0 Exercise :)
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / (height ** 2))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif (bmi > 18.5) and (bmi < 25):
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif (bmi > 25) and (bmi < 30):
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif (bmi > 30) and (bmi < 35):
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically.")

## Determine Leap Year Exercise
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

mode_4 = year % 4
mode_100 = year % 100
mode_400 = year % 400

if (mode_4 == 0 and mode_100 != 0 or mode_400 == 0):
    print("Leap year.")
else:
    print("Not leap year.")

## Pizza Delivery Challenge
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
pizza_cost = 0

pepperoni_decision = 1 if add_pepperoni == 'Y' else 0
cheese_decision = 1 if extra_cheese == 'Y' else 0

if size == 'S':
    pizza_cost = 15
    pizza_cost += pepperoni_decision * 2 + cheese_decision
elif size == 'M':
    pizza_cost = 20
    pizza_cost += pepperoni_decision * 3 + cheese_decision
elif size == 'L':
    pizza_cost = 25
    pizza_cost += pepperoni_decision * 3 + cheese_decision

print(f"Your final bill is: ${pizza_cost}.")

##Love Calculator Exercise
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
true_score = 0
love_score = 0

for letter in name1.lower():
    if letter in 'true':
        true_score += 1

for letter in name2.lower():
    if letter in 'true':
        true_score += 1

for letter in name1.lower():
    if letter in 'love':
        love_score += 1

for letter in name2.lower():
    if letter in 'love':
        love_score += 1

total_score = int(f"{true_score}{love_score}")

if (total_score < 10 or total_score > 90):
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif (total_score > 40 and total_score < 50):
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")

