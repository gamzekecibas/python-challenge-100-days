import requests
from twilio.rest import Client
## proxy client may be required in python anywhere
#import os
#from twilio.http.http_client import TwilioHttpClient

OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
MY_LAT = 40.89
MY_LON = 29.31
EXCLUDED_DATA = "current,minutely,daily"

with open('my_api_info.txt', 'r') as file:
    MY_API_KEY = file.readline().strip()  # if it is environment variable, it is embedded in
                                          # terminal with export MY_API_KEY=my_key
                                         # this export line(s) should be in tasks!!
                                         # call the key as  os.environ.get("MY_API_KEY")
    MY_SID = file.readline().strip()
    MY_TOKEN = file.readline().strip()
    FROM_NUM = file.readline().strip()
    TO_NUM = file.readline().strip()

PARAMS = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "exclude": EXCLUDED_DATA,
    "appid": MY_API_KEY
}

try:
    response = requests.get(OWM_ENDPOINT, params=PARAMS)
    response.raise_for_status()
    weather_data = response.json()

    will_rain = False

    weather_slice = weather_data["hourly"][:12]
    for hour_data in weather_slice:
        condition_code = hour_data["weather"][0]["id"]
        if int(condition_code) < 700:
            will_rain = True

    if will_rain:
        #print("Bring an umbrella!")
    #else:
        #print("No rain expected.")
        client = Client(MY_SID, MY_TOKEN)
        message = client.messages.create(
            body="It's going to rain today. Remember to bring an ☔️",
            from_=FROM_NUM,
            to=TO_NUM
        )
        print(message.status)
except requests.exceptions.HTTPError as e:
    print(f"Error: {e}")

## Now use pythonanywhere to run the script in 7 am each morning