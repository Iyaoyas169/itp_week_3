import requests
import json

# using the requests package, we can make API calls to retrieve JSON
# and storing it into a variable her called "response"
response = requests.get("https://rickandmortyapi.com/api/character")

#verify the response status as 200
# print(response)

#verify the raw string data of the response
#print(response.text)
clean_data = json.loads(response.text)

#print(clean_data)

print(clean_data["name"])
# print key values pairs
# find a way to load it into xcel sheet

#loop through
#name/gender/location/species name