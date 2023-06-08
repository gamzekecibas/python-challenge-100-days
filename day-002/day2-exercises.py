## Day 2 - Understanding Data Types
## 30.05.2023
## Exercises

## Data Types
## ---
## String --> sequence of character(s), "Hello", "123" etc.
    ## Subscripting: "Hello"[0] = 'H'
## Integer
    ## 123, 345, print(123 + 345) = 468
    ## 123_456_789 == 123456789 --> '_' equals ',' in larger integers.
## Float
    ## 3.14159, 3141.59 etc.
## Boolean
    ### True or False

## Check data type
num_char = len(input("What is your name?\n"))
new_num_char = str(num_char)

print("Type of num_char is ", type(num_char))
print("Type of new_num_char is ", type(new_num_char))
print("Your name has " + new_num_char + " characters.\n\n")

a = 123
print("First type of a is ", type(a))
a = str(123)
print("Second type of a is ", type(a))
a = float(123)
print("Third type of a is ", type(a), '\n\n')

print(type(70 + float("100.5")))
print(type(str(70) + str(1000)), '\n\n')

## Interactive Exercise - 1
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

print(int(two_digit_number[0]) + int(two_digit_number[1]))


## Mathematical Operations, PEMDAS[(), **, * /, + -][Left to Right]  works here!
print(3 + 5)
print(7 - 3)
print(3 * 2)
print(type(6 / 3))  ## division always return float, 2.0
print(2 ** 3)

print(3 * 3 + 3 / 3 - 3)

## Interactive Exercise - 2 | BMI Calculator
# HINTS
#Check the data type of the inputs.
#Try to use the exponent operator in your code.
#Remember PEMDAS.
#Remember to convert your result to a whole number (int).

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

print(int(float(weight) / (float(height) ** 2)))

## Round numbers
print(int(8 / 3)) ## 2
print(8 // 3) ## 2
print(round(8 / 3)) ## 3
print(round(8 / 3, 2)) ## 2.67

#f-String
score = 0
score += 10
height = 1.8
isWinning = True

print(f"Your score is {score}, your heigth is {height}, you are winning is {isWinning}")

## Interactive Exercise - 3 | Left Time to 90 :)
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
left_year = 90 - int(age)

current_days = 365 * left_year
current_months = 12 * left_year
current_weeks = 52 * left_year

print(f"You have {int(current_days)} days, {int(current_weeks)} weeks, and {int(current_months)} months left.")
