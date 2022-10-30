import requests
from datetime import datetime
# this section is to create a user in pixela

today = datetime.now()
today = today.strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"

TOKEN = "tbontbtitq123"
USERNAME = "josefsho"

GRAPH_ID = "graph1"

HEADERS = {
    "X-USER-TOKEN": TOKEN
}

date = today

# change the quantity as you see fit
quantity = input("how many hours did you code today: ")

user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

"""
response = requests.post(url=pixela_endpoint, json=user_param)
print(response.text)"""

# this section is to create a new graph in pixela

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_param = {
    "id": GRAPH_ID,
    "name": "coding_graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}

"""response = requests.post(url=graph_endpoint, json=graph_param, headers=HEADERS)
print(response.text)"""

# this is to add a pixel to the graph


post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

post_pixel_param = {
    "date": date,
    "quantity": quantity
}

response = requests.post(url=post_pixel_endpoint, headers=HEADERS, json=post_pixel_param)
print(response.text)

