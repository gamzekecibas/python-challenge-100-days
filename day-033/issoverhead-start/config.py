## Configuration for issoverhead/main.py
# Your latitude and longitude
MY_LAT = 41.074025
MY_LONG = 29.053162

# Your email and SMTP server connection
MY_EMAIL = "gkecibas@gmail.com"
SMTP_CONNECTION = "smtp.gmail.com"

# Read the email app password from a file
with open("app_password.txt") as file:
    MY_PASSWORD = file.readlines()[0]

# ISS API URL
ISS_API_URL = "http://api.open-notify.org/iss-now.json"

# Sunrise-sunset API URL
SUNRISE_SUNSET_API_URL = "https://api.sunrise-sunset.org/json"