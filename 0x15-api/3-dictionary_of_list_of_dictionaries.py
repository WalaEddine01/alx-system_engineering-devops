#!/usr/bin/python3
"""
This module for get data from users API
and export data in the JSON format.
"""
if __name__ == "__main__":
    import json
    from urllib import request
    dict_ = {}
    json_data_list = {

    }
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        with request.urlopen(url) as request_:
            res = json.load(request_)
            for i in res:
                ID_ = i.get('id')
                username = i.get('username')
                url2 = "https://jsonplaceholder.typicode.com/todos"
                with request.urlopen(url2) as req:
                    res2 = json.load(req)
                    json_data_list[str(ID_)] = []
                    for j in range(len(res2)):
                        dict_ = {}
                        if res2[j].get("userId") is int(ID_):
                            completed = res2[j].get('completed')
                            title = res2[j].get("title")
                            dict_['task'] = title
                            dict_['completed'] = completed
                            dict_['username'] = username
                            json_data_list[str(ID_)].append(dict_)
            json_file_path = "todo_all_employees.json"
            jsonfile = open(json_file_path, 'w', newline='')
            json.dump(json_data_list, jsonfile)
            jsonfile.close()
    except Exception as e:
        print(f"Error code: {e}")
