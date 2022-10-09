import requests
from datetime import datetime

USER_NAME = 'kimeuihyun'
TOKEN = "dswjflwlfsawe"
GRAPH_ID = "graph1"


pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    "token": "dswjflwlfsawe",
    "username": "kimeuihyun",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config,headers=headers)
# print(response.text)

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "8.99",

}
pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
# response = requests.post(url=pixel_endpoint,json=pixel_config,headers=headers)
# print(response.text)

# pixel_update_config = {
#     "quantity": "7.24"
# }
# pixel_update_endpoint = f"{pixel_endpoint}/{pixel_config['date']}"
# response = requests.put(url=pixel_update_endpoint,json=pixel_update_config,headers=headers)
# print(response.text)

pixel_delete_endpoint = f"{pixel_endpoint}/{pixel_config['date']}"
response = requests.delete(url=pixel_delete_endpoint,headers=headers)
print(response.text)