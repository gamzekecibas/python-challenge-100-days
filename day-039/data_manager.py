import os
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    # get Sheety keys from .env file
    
    SHEETY_GET_ENDPOINT = os.getenv("SHEETY_GET_ENDPOINT")
    SHEETY_POST_ENDPOINT = os.getenv("SHEETY_POST_ENDPOINT")
    SHEETY_PUT_ENDPOINT = os.getenv("SHEETY_PUT_ENDPOINT")
    SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
    SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")
    
    def get_destination_data(self):
        response = requests.get(url=self.SHEETY_GET_ENDPOINT, auth=(self.SHEETY_USERNAME, self.SHEETY_PASSWORD))
        data = response.json()
        
        return data["sayfa1"]
    
    def update_destination_codes(self):
        for city in self.destination_data:
            # Replace [Object ID] in the URL with the actual row ID
            put_endpoint = self.SHEETY_PUT_ENDPOINT.replace("[Object ID]", str(city["id"]))
            
            new_data = {
                "sayfa1": {
                    "iataCode": city["iataCode"]
                }
            }
            
            requests.put(
                url=put_endpoint,
                auth=(self.SHEETY_USERNAME, self.SHEETY_PASSWORD),
                json=new_data
            )
            
        print("The update is successful!")