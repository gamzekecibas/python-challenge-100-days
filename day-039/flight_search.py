import os

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")
        self.AMADEUS_SECRET_PWD = os.getenv("AMADEUS_SECRET_PWD")
        
    