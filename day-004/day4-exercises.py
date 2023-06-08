## Day 4 - Randomisation and Python Lists
## 01.06.2023
## Exercises

## Random library
## ---

## Heads or Tails exercise
# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲

# Write the rest of your code below this line 👇
import random

gen_num = random.randint(0, 1)

if gen_num == 1:
    print('Tails')
else:
    print('Heads')

## Banker Roulette for Meal :)
# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

num_people = len(names) - 1
select_idx = random.randint(0, num_people)

print(f'{names[select_idx]} is going to buy the meal today!')

## Treasure Map Exercise
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

select_row = map[int(str(position)[1]) - 1]
select_row[int(str(position)[0]) - 1] = 'X'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")



