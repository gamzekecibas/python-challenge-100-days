import requests
from datetime import datetime, timedelta
from twilio.rest import Client
import configparser
import os

# Read the configuration file
config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), '.project_config')
config.read(config_path)

# Get the API keys and other configurations
try:
    API_KEY = config['API_KEYS']['ALPHA_VANTAGE_API_KEY'].strip('"')
    NEWS_API_KEY = config['API_KEYS']['NEWS_API_KEY'].strip('"')
    TWILIO_ACCOUNT_SID = config['TWILIO']['ACCOUNT_SID']
    TWILIO_AUTH_TOKEN = config['TWILIO']['AUTH_TOKEN']
    TWILIO_PHONE_NUMBER = config['TWILIO']['TWILIO_PHONE_NUMBER']
    YOUR_PHONE_NUMBER = config['TWILIO']['YOUR_PHONE_NUMBER']
except KeyError as e:
    print(f"Error: {e} not found in the config file.")
    exit(1)

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Get yesterday's and day before yesterday's dates
yesterday = datetime.now() - timedelta(1)
day_before_yesterday = datetime.now() - timedelta(2)
yesterday_str = yesterday.strftime('%Y-%m-%d')
day_before_yesterday_str = day_before_yesterday.strftime('%Y-%m-%d')

# Make a request to the Alpha Vantage API
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=params)
data = response.json()

# Get closing prices
yesterday_close = float(data["Time Series (Daily)"][yesterday_str]["4. close"])
day_before_yesterday_close = float(data["Time Series (Daily)"][day_before_yesterday_str]["4. close"])

# Calculate price difference and percentage
price_difference = abs(yesterday_close - day_before_yesterday_close)
percentage_difference = (price_difference / day_before_yesterday_close) * 100

# If percentage difference is greater than 5%, get news and send messages
if percentage_difference > 5:
    # Get news articles
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "pageSize": 3
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"][:3]

    # Create Twilio client
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    # Send messages
    for article in articles:
        symbol = "🔺" if percentage_difference > 0 else "🔻"
        formatted_message = f"""
        {STOCK_NAME}: {symbol}{round(percentage_difference, 2)}%
        Headline: {article['title']}
        Brief: {article['description']}
        """
        message = client.messages.create(
            body=formatted_message,
            from_=TWILIO_PHONE_NUMBER,
            to=YOUR_PHONE_NUMBER
        )
        print(f"Sent formatted message: {message.sid}")

