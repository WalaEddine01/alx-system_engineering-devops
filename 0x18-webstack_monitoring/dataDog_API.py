#!/usr/bin/python3

import requests

# Datadog API credentials
api_key = '48f0fee9cea33b962645784c745e4cc4'
app_key = '16b461bf3929913dadf02cd653e5cc1ce7dbf939'

# Endpoint URL for retrieving dashboards
url = 'https://api.datadoghq.com/api/v1/dashboard'

# Headers for API request
headers = {
    'Content-Type': 'application/json',
    'DD-API-KEY': api_key,
    'DD-APPLICATION-KEY': app_key
}

# Make GET request to retrieve dashboards
response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code == 200:
    # Parse JSON response
    for i in response.json().get('dashboards'):
        if i.get('id'):
            print(i.get('id'))
    
    # Print dashboard names and IDs
    
else:
    print(f"Error: {response.status_code}, {response.text}")
