import requests

TRIVIA_API = "https://opentdb.com/api.php"
parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(url=TRIVIA_API, params=parameters)
response.raise_for_status()
question_data = response.json()['results']