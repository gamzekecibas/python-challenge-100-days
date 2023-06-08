## Day 2 - Understanding Data Types
## 30.05.2023
## ----
## DAY 2 PROJECT Tip Calculator
## ----

#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to tip calculator!\n")

total_cost = input('What is the total of bill ($)?: ')
num_people = input('What is number of people?: ')
tip_percent = input('How much tip would you like to give? %10, 12 or 15: ')
cost_by_person = (float(total_cost) / float(num_people)) * (1 + int(tip_percent) / 100)

print(f'\nBill of each person with {tip_percent}% tip equals to ${round(cost_by_person, 2)}')