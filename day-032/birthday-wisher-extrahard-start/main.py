##################### Extra Hard Starting Project ######################
import pandas as pd
import smtplib
from datetime import datetime as dt
from random import choice
import os
import glob

MY_EMAIL = "gkecibas@gmail.com"
SMTP_CONNECTION = "smtp.gmail.com"
with open("app_password.txt") as file:
    MY_PASSWORD = file.readlines()[0]

# 1. Update the birthdays.csv - Done
birthdays = pd.read_csv("birthdays.csv", sep=',')

# Use glob to find all .txt files in the directory
letter_templates = glob.glob(os.path.join("letter_templates/", '*.txt'))
# If you want just the file names without the directory path, you can use a list comprehension
template_names = [os.path.basename(file) for file in letter_templates]

# print(birthdays)
# 2. Check if today matches a birthday in the birthdays.csv

today_dt = dt.now()
today_day = today_dt.day
today_month = today_dt.month

print(f"Today is {today_day}/{today_month}.")
birthday_people = []

for idx in range(len(birthdays)):
    if (birthdays.iloc[idx, 4] == today_day) & (birthdays.iloc[idx, 3] == today_month):
        birthday_people.append(birthdays.iloc[idx, 0])
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        random_template = choice(template_names)
        message_path = "letter_templates/" + random_template

        with open(message_path) as file:
            birthday_message = file.read()

        updated_birthday_message = birthday_message.replace("[NAME]", birthdays.iloc[idx, 0])

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP(SMTP_CONNECTION, 587) as connection: 
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)

            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthdays.iloc[idx, 1],
                msg=f"Subject:HAPPY BIRTHDAY!\n\n{updated_birthday_message}"
            )

if len(birthday_people) != 0:
    print(f"Today is birthday of {birthday_people}")
else:
    print("There is no birthday for today.")