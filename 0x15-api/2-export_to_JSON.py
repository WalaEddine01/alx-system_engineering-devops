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
    list_ = []
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
                for i in res2:
                    if i.get("userId") is int(ID_):
                        list_.append(i.get("title"))
                    if i.get("userId") == int(ID_):
                        b = b + 1
                print(f"Employee {name} is done with tasks({a}/{b}):")
                for i in list_:
                    print("\t ", end="")
                    print(i)
    except Exception as e:
        print(f"Error code: {e}")
