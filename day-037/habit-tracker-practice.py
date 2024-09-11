import requests
from datetime import datetime

USERNAME = "YOUR_USERNAME"
TOKEN = "YOUR_TOKEN"

"""
Step 1: Create a user account
$ curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes", "notMinor":"yes"}'
{"message":"Success.","isSuccess":true}
"""
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,             ## password
    "username": USERNAME,       ## username
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response =requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

"""
Step 2: Create a graph definition
$ curl -X POST https://pixe.la/v1/users/kvgamze/graphs -d '{"id":"test-graph", "name":"Test Graph", "unit":"commit", "type":"int", "color":"shibafu"}'
"""


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "coding-tracker",
    "name": "Coding Graph",
    "unit": "minute",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

"""
Step 3: Get the graph information
$ https://pixe.la/v1/users/YOUR_USERNAME/graphs/YOUR_GRAPH_ID.html
"""
"""_summ
Step 4: Post a pixel to the graph
$ curl -X POST https://pixe.la/v1/users/YOUR_USERNAME/graphs/YOUR_GRAPH_ID -d '{"date":"20240229", "quantity":"30"}'
"""

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

today_date = datetime.now().strftime("%Y%m%d")

pixel_config = {
    "date": today_date,
    "quantity": "70.5"
}

## If we want to change a data on graphs
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{today_date}"

update_config = {
    "quantity": "100.5"
}

#response = requests.put(url=update_endpoint, json=update_config, headers=headers)
#print(response.text)

## If we want to delete a data on graphs
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{today_date}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
