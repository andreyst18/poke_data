import requests
import json

# response = requests.get("https://pokeapi.co/api/v2/pokemon/1")
# print(response.status_code)
# data = response.json()
# # print(list(data.keys()))
# print(type(data))

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=20&offset=0")
page = response.json()
print(page['count'])
print(page['next'])