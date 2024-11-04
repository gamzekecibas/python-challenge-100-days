import os
import time
from amadeus import Client, ResponseError

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")
        self.AMADEUS_SECRET_PWD = os.getenv("AMADEUS_SECRET_PWD")
        
    def get_iata_code(self, city_name):
        if not self.AMADEUS_API_KEY or not self.AMADEUS_SECRET_PWD:
            print("Error: Amadeus API credentials not found in environment variables")
            return None
            
        try:
            amadeus = Client(
                client_id=self.AMADEUS_API_KEY,
                client_secret=self.AMADEUS_SECRET_PWD
            )
        except Exception as e:
            print(f"Error initializing Amadeus client: {e}")
            return None
        
        max_retries = 5
        retry_delay = 10
        
        for attempt in range(max_retries):
            try:
                if attempt > 0:
                    print(f"Attempt {attempt + 1} of {max_retries}")
                    time.sleep(retry_delay)
                
                try:
                    response = amadeus.reference_data.locations.get(
                        keyword=city_name,
                        subType=["AIRPORT", "CITY"]
                    )
                except ResponseError as error:
                    if error.code == 429:  # Too Many Requests
                        if attempt < max_retries - 1:
                            print(f"Rate limit exceeded for {city_name}. Attempt {attempt + 1}/{max_retries}")
                            print(f"Waiting {retry_delay} seconds before retrying...")
                            time.sleep(retry_delay)
                            retry_delay *= 2
                            continue
                        print(f"Failed to get IATA code for {city_name} after {max_retries} attempts")
                    elif error.code == 401:
                        print(f"Authentication error: Please check your API credentials")
                    else:
                        print(f"API error ({error.code}) for {city_name}: {error}")
                    return None
                except Exception as e:
                    print(f"Unexpected error querying API for {city_name}: {e}")
                    return None

                if not response.data:
                    print(f"No location data found for city: {city_name}")
                    return None
                    
                # Look for airports first
                for location in response.data:
                    if location.get("subType") == "AIRPORT":
                        return location.get("iataCode")
                
                # If no airports found, look for city code
                for location in response.data:
                    if location.get("subType") == "CITY":
                        return location.get("iataCode")
                
                # If neither airport nor city specifically found, return first code
                if response.data[0].get("iataCode"):
                    return response.data[0]["iataCode"]
                
                print(f"No valid IATA code found in response for: {city_name}")
                return None
                
            except Exception as e:
                print(f"Unexpected error processing response for {city_name}: {e}")
                if attempt == max_retries - 1:
                    return None
                continue