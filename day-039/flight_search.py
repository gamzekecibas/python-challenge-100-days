import os
import time
from amadeus import Client, ResponseError

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")
        self.AMADEUS_SECRET_PWD = os.getenv("AMADEUS_SECRET_PWD")
        
    def get_iata_code(self, city_name):
        amadeus = Client(
            client_id=self.AMADEUS_API_KEY,
            client_secret=self.AMADEUS_SECRET_PWD
        )
        
        max_retries = 5  # Increased from 3 to 5 retries
        retry_delay = 10  # Increased initial delay to 10 seconds
        
        for attempt in range(max_retries):
            try:
                # Add a small delay even before first attempt to respect rate limits
                if attempt > 0:
                    print(f"Attempt {attempt + 1} of {max_retries}")
                    time.sleep(retry_delay)
                
                response = amadeus.reference_data.locations.get(
                    keyword=city_name,
                    subType=["AIRPORT", "CITY"]
                )
                
                if len(response.data) > 0:
                    # Look for airports first
                    for location in response.data:
                        if location["subType"] == "AIRPORT":
                            return location["iataCode"]
                    
                    # If no airports found, look for city code
                    for location in response.data:
                        if location["subType"] == "CITY":
                            return location["iataCode"]
                    
                    return response.data[0]["iataCode"]
                else:
                    print(f"No IATA code found for city: {city_name}")
                    return None
            
            except ResponseError as error:
                if error.code == 429:  # Too Many Requests
                    if attempt < max_retries - 1:
                        print(f"Rate limit exceeded for {city_name}. Attempt {attempt + 1}/{max_retries}")
                        print(f"Waiting {retry_delay} seconds before retrying...")
                        time.sleep(retry_delay)
                        retry_delay *= 2  # Double the delay for next attempt
                        continue
                    else:
                        print(f"Failed to get IATA code for {city_name} after {max_retries} attempts")
                print(f"Error getting IATA code for {city_name}: {error}")
                return None