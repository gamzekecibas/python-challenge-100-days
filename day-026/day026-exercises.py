## Squaring Numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

squared_numbers = [number ** 2 for number in numbers]

#Write your code 👆 above:

print(squared_numbers)

## Filtering Even Numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:

result = [number for number in numbers if number % 2 == 0]

#Write your code 👆 above:

print(result)

## Data Overlap

with open('file1.txt', 'r') as file:
    # Use list comprehension to read lines into a list
    info1 = [int(line.strip()) for line in file]

with open('file2.txt', 'r') as file:
    # Use list comprehension to read lines into a list
    info2 = [int(line.strip()) for line in file]

result = [value for value in info1 if value in info2]
# Write your code above 👆

print(result)

## Dict Comprehension - I
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

result = {word: len(word) for word in sentence.split()}

print(result)

## Dict Comprehension - II
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

weather_f = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)

import pandas as pd
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    if key == 'Angela':
        print(value)

student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    if row.student == 'Angela':
    #Access row.student or row.score
        print(row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}