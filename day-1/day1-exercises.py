## Day 1 - String Manipulation
## 29.05.2023
## Exercises

## print() method
print("Day - 1 Python Print Function")
print("The function is declared like this")
print("print('what to print')")

print("\n\nDay - 1 Python Print Function\nThe function is declared like this\nprint('what to print')")

print("\n\nHello " + "World")
print("Hello" + " World")
print("Hello " + "" +"World")

## Take inputs from users
print("\n\nHello " + input("\nWhat is your name?\n"))
print("\n\n")
print(len(input("What is your name? ")))

## Assign variables
user_name = input('What is your name?')  ## changable
print(user_name)

user_name_length = len(user_name)
print(user_name_length)

## Replace variables
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

memory_value = a
a = b
b = memory_value

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

