# Save the workout data to the Google Sheet using Sheety API & Nutritionix API
# Import the required libraries
import os
from dotenv import load_dotenv

import requests
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Get Nutritionix API credentials from environment variables
ID = os.environ.get("NUTRITIONIX_APP_ID")
PASSWORD = os.environ.get("NUTRITIONIX_API_KEY")

# Get Sheety API credentials from environment variables
sheety_info = {
    "connection": {
        "GET": os.environ.get("SHEETY_GET_ENDPOINT"),
        "POST": os.environ.get("SHEETY_POST_ENDPOINT")
    },
    "auth": {
        "Authorization": os.environ.get("SHEETY_AUTH_TOKEN"),
        "username": os.environ.get("SHEETY_USERNAME"), 
        "password": os.environ.get("SHEETY_PASSWORD")
    }
}

# check the connection to the Nutritionix API
exercise_endpoint = os.environ.get("NUTRITIONIX_ENDPOINT", "https://trackapi.nutritionix.com/v2/natural/exercise")

headers = {
    "x-app-id": ID,
    "x-app-key": PASSWORD,
    "Content-Type": "application/json"
}
        
# get the endpoint for the Sheety API
sheety_endpoint = sheety_info["connection"]["POST"]

# Use HTTP Basic Auth with username and password
auth = (sheety_info["auth"]["username"], sheety_info["auth"]["password"])

# Get the exercise query from the user
query = input("What exercise did you do?:\n")

parameters = {
    "query": query
}

# Send the query to the Nutritionix API
response = requests.post(exercise_endpoint, json=parameters, headers=headers)

# Check if response is successful before proceeding
if response.status_code != 200:
    print(f"Error with Nutritionix API: {response.status_code}")
    print(response.json())
    exit()

try:
    exercise_data_list = response.json()["exercises"]
except KeyError:
    print("No exercise data found in response. Check your Nutritionix API credentials.")
    exit()

# Add Authorization header for Sheety API
sheety_headers = {
    "Authorization": sheety_info["auth"]["Authorization"]
}

for exercise_data in exercise_data_list:
    workout_data = {
        "sayfa1": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise_data["name"].title(),
            "duration": exercise_data["duration_min"], 
            "calories": exercise_data["nf_calories"],
            "id": exercise_data["tag_id"] if "tag_id" in exercise_data else None,
            "met": exercise_data["met"] if "met" in exercise_data else None,
            "user_input": query
        }
    }
    
    # Post each exercise using both Basic Auth and Bearer token
    response = requests.post(
        sheety_endpoint, 
        json=workout_data, 
        auth=auth,
        headers=sheety_headers
    )
    
    if response.status_code != 200:
        print(f"Error with Sheety API: {response.status_code}")
    print(response.text)
    
print("Workout data successfully posted to your Google Sheet!")