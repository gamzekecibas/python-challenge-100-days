## Day 5 - Python Loops
## 02.06.2023
## Exercises

## Average Height Practice
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_height = 0
for height in student_heights:
    total_height += height

print(round(total_height / len(student_heights)))

## High Score Exercise
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score

print(f'The highest score in the class is: {max_score}')

## Adding even numbers
#Write your code below this row 👇

all_numbers = range(101)
even_numbers = list(filter(lambda x: x % 2 == 0, all_numbers))

even_sum = sum(even_numbers)
print('Total sum of even numbers from 0 to 100: ', even_sum)


##FizzBuzz Exercise
# Write your code below this row 👇

numbers_1_100 = range(1, 101)

for num in numbers_1_100:
    if (num % 3 == 0) and (num % 5 == 0):
        print('FizzBuzz')
    elif (num % 3 == 0 and num % 5 != 0):
        print('Fizz')
    elif (num % 3 != 0 and num % 5 == 0):
        print('Buzz')
    else:
        print(num)
