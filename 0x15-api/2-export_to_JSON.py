#!/usr/bin/python3
"""
This module for get data from users API
and export data in the JSON format.
"""
if __name__ == "__main__":
    import json
    from sys import argv
    from urllib import request
    ID_ = argv[1]
    dict_ = {}
    json_data_list = {
        str(ID_): []
    }
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        with request.urlopen(url) as request_:
            res = json.load(request_)
            for i in res:
                if i.get('id') == int(ID_):
                    username = i.get('username')
                    break
            url2 = "https://jsonplaceholder.typicode.com/todos"
            with request.urlopen(url2) as req:
                res2 = json.load(req)
                json_file_path = f'{argv[1]}.json'
                with open(json_file_path, 'w', newline='') as jsonfile:
                    for i in range(len(res2)):
                        dict_ = {}
                        if res2[i].get("userId") is int(ID_):
                            completed = res2[i].get('completed')
                            title = res2[i].get("title")
                            dict_['task'] = title
                            dict_['completed'] = completed
                            dict_['username'] = username
                            json_data_list[str(ID_)].append(dict_)
                    json.dump(json_data_list, jsonfile)
    except Exception as e:
        print(f"Error code: {e}")
