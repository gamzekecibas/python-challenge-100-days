## Day 10 - Debugging
## 10.06.2023
## Exercises

############DEBUGGING#####################

# # Describe Problem
def my_function():
    for i in range(1, 21):       ## range is updated as (1,21) instead of (1,20)
        if i == 20:
            print("You got it")
my_function()

# # Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)        ### change randint borders as 0 to 5 instead of 1 to 6
#print(dice_num)                ## the line is added to monitor bug
print(dice_imgs[dice_num])

# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:              ## add = sign to cover 1994
    print("You are a Gen Z.")

# # Fix the Errors
age = int(input("How old are you?"))  ## add int() to input to be available to compare
if age > 18:
    print(f"You can drive at age {age}.")  ## it returns f-string

#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))  ## delete one of the equal sign
total_words = pages * word_per_page
print(total_words)

# #Use a Debugger
# https://pythontutor.com/visualize.html#mode=edit
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)  ## an indentation is added to update list for each item
    print(b_list)

mutate([1,2,3,5,8,13])

## Debugging for Even or Odd Number
number = int(input("Which number do you want to check?"))

if number % 2 == 0:                ## Add double equal sign to check same or not instead of assign a value
  print("This is an even number.")
else:
  print("This is an odd number.")

## Debugging Leap Year Detection
year = int(input("Which year do you want to check?"))  ## add int() to convert type string to integet to check the year

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")


## Debugging for FizzBuzz
for number in range(1, 101):
  if (number % 3 == 0 and number % 5 == 0):  ## or is changed with and to provide 15x
    print("FizzBuzz")
  elif number % 3 == 0:                      ## Line 79 and 81 are changed with elif instead of if
    print("Fizz")                            ## When they are if statements, exact number is always printed!
  elif number % 5 == 0:
    print("Buzz")
  else:
    print([number])