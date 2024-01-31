#!/usr/bin/python3
import json

# Your list of JSON objects
json_data_list = {
    "user" : [
    {
        "userId": 1,
        "id": 11,
        "title": "Complete Task 1",
        "completed": True
    },
    {
        "userId": 2,
        "id": 21,
        "title": "Incomplete Task 2",
        "completed": False
    },
    {
        "userId": 3,
        "id": 31,
        "title": "Complete Task 3",
        "completed": True
    }
    ]
}

# Specify the JSON file path
json_file_path = 'output_data.json'

# Write JSON data to the file
with open(json_file_path, 'w') as json_file:
    json.dump(json_data_list, json_file, indent=2)