import requests
from datetime import datetime
import smtplib
import time
from config import *


def main():
    while True:
        time.sleep(60)

        # Get ISS position
        response = requests.get(url=ISS_API_URL)
        response.raise_for_status()
        data = response.json()

        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])

        # Your position is within +5 or -5 degrees of the ISS position.
        my_lat_range = [MY_LAT - 5, MY_LAT + 5]
        my_lng_range = [MY_LONG - 5, MY_LONG + 5]

        # Get sunrise and sunset times
        parameters = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
        }
        response = requests.get(SUNRISE_SUNSET_API_URL, params=parameters)
        response.raise_for_status()
        data = response.json()

        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

        time_now = datetime.now()

        # If the ISS is close to your current position and it is currently dark
        is_iss_close = (my_lat_range[0] <= iss_latitude <= my_lat_range[1]) & (
                my_lng_range[0] <= iss_longitude <= my_lng_range[1])
        is_day_here = sunrise < time_now.hour < sunset

        if is_iss_close and not is_day_here:
            with smtplib.SMTP(SMTP_CONNECTION, 587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)

                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg="Subject:Look UP!\n\nISS is overhead now!"
                )


if __name__ == "__main__":
    main()
