import requests

OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
MY_LAT = 40.893660
MY_LON = 29.312556
EXCLUDED_DATA = "current,minute,daily"
with open('my_openweather_api_key', 'r') as file:
    for line in file:
        MY_API_KEY = line

PARAMS = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": MY_API_KEY,
    "exclude": EXCLUDED_DATA
}

response = requests.get(OWM_ENDPOINT, params=PARAMS)
# To view json format: https://jsonviewer.stack.hu/
response.raise_for_status()
weather_data = response.json()

will_rain = False

## To print weather id referred in tables: https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
# print(weather_data["hourly"][0]["weather"][0]["id"])
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella!")
