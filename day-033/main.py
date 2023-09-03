import requests
from datetime import datetime as dt
"""
Meanins of Response Codes:

- 1XX: Hold On ..
- 2XX: Success :) 
- 3XX: ~No permission :(:(
- 4XX: Client Screwed Up or It does not exist :( 
- 5XX: Server Screwed Up such as server is down :(

docs: https://www.webfx.com/web-development/glossary/http-status-codes/
"""

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # There too many status code to define Exception separately
# # if response.status_code == 404:
# #     raise Exception("That resource does not exist!")
# # elif response.status_code == 401:
# #     raise Exception("You are not authorised to access this data.")
#
# response.raise_for_status()
#
# all_data = response.json()["iss_position"]
#
# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]
# iss_position = (float(longitude), float(latitude))
# ## To find the position on the map: https://www.latlong.net/Show-Latitude-Longitude.html
# ## when I run the script, ISS is on Ankalalobe /Madagascar :)
# print(iss_position)

# sunrise sunset API: https://sunrise-sunset.org/api
MY_LAT, MY_LNG = 41.074025, 29.053162
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]  ## to transform format 24-hours & seperate the hour
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = dt.now()
now_hour = time_now.hour