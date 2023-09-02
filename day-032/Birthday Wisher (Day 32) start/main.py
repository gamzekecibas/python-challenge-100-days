import smtplib
import datetime as dt

## SMTP PRACTICES
my_email = "gkecibas@gmail.com"
with open('app_password.txt') as file:
     my_password = file.readlines()[0]
#
# # connection = smtplib.SMTP("smtp.gmail.com", 587)
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:   # with block helps to reduce # lines with eliminating close method
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="gamzetest@ku.edu.tr",
#         msg="Subject:Hello!\n\nThis is body of the message!"
#     )
#
# # connection.close()


## DATETIME PRACTICES

# now = dt.datetime.now()
# year = now.year
# print(type(now))
#
# date_of_birth = dt.datetime(year=1998, month=4, day=30)
# print("My birthday:", date_of_birth)

# MONDAY MOTIVATION :)
import pandas as pd

today_date = dt.datetime.now()
today_day = today_date.weekday()

# Initialize an empty list to store data
data = []

# Open the text file
with open('quotes.txt', 'r') as file:
    # Read lines one by one
    for line in file:
        # Split each line by '-'
        parts = line.strip().split('-')
        if len(parts) == 2:  # Ensure there are two parts
            quote, owner = parts
            # Create a dictionary for each line
            data.append({'quote': quote.strip(), 'owner': owner.strip()})

# Create a pandas DataFrame from the list of dictionaries
df = pd.DataFrame(data)

if today_day == 1:
    random_quote = df.sample()
    today_quote = random_quote.iloc[0, 0]
    today_owner = random_quote.iloc[0, 1]

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:   # with block helps to reduce # lines with eliminating close method
         connection.starttls()
         connection.login(user=my_email, password=my_password)

         connection.sendmail(
             from_addr=my_email,
             to_addrs="gamzetest@gmail.com",
             msg=f"Subject:Today Motivation<3\n\n{today_quote}\n\n{today_owner}"
         )
else:
    print("Today is not Monday!")