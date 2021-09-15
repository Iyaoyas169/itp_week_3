
import requests
import json
import openpyxl #Use this to start accessing the wb variable step below

# using the requests package, we can make API calls to retrieve JSON
# and storing it into a variable her called "response"
response = requests.get("https://rickandmortyapi.com/api/character")

#verify the response status as 200 which is a code for data retrieved successfully
#print(response)

#verify the raw string data of the response
#print(response.text)
clean_data = json.loads(response.text)

#print(clean_data)

result = clean_data["results"]

first_item = result[0] #points to the first set of "results"
print(type(first_item)) #dictionary
#print(first_item)
print(first_item["name"])

# print key values pairs
# find a way to load it into xcel sheet
wb = openpyxl.load_workbook("\itp_week_4\day_1\output.xlsx")
sheet = wb["Sheet1"]

# sheet["A1"] = first_item["name"]
# sheet["B1"] = first_item["species"]
# sheet["C1"] = first_item["gender"]
# sheet["D1"] = first_item["location]["name"]

# second_item = result[1]

# sheet["A2"] = second_item["name"]
##### End Iteration

##### New Iteration

row = 1

for character in result:
    sheet["A" + str(row)] = character["name"]
    sheet["B" + str(row)] = character["species"]
    sheet["C" + str(row)] = character["gender"]
    sheet["D" + str(row)] = character["location"]["name"]
    row += 1


#loop through
#name/gender/location/species name
#output them in to an excel sheet