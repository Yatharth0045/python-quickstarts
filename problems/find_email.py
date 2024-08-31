## Write a Python script that retrieves users data from the given API endpoint - , filters users based on their geographical location (latitude and longitude within +0.0 to +30.0), and extracts their email addresses.

import requests
import json

url = 'https://jsonplaceholder.typicode.com/users'

response = requests.get(url)

print(response.text)
print()
user_data = json.loads(response.text)

# print(user_data)

def find_emails(data):
    emails = []
    for user in data:
        lat = float(user['address']['geo']['lat'])
        lng = float(user['address']['geo']['lng'])
        # print(float(lat),float(lng))
        if(lat >= +0.00 and lat <= +30.0):
            if(lng >= +0.00 and lng <= +30.0):
                print(user['email'])
        
find_emails(user_data)
