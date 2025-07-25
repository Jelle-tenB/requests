import requests
from datetime import datetime

USERNAME = "jellepelle213"
TOKEN = "kladglkaghlkag"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.now()

graph_input = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10",
}

response = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs/graph1", json=graph_input, headers=headers, timeout=10)
print(response.text)
