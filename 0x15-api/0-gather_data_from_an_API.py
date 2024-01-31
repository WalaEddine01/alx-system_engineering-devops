#!/usr/bin/python3
"""
This module for get data from users API
"""
if __name__ == "__main__":
    import json
    from sys import argv
    from urllib import request
    ID_ = argv[1]
    list_ = []
    b = 0
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        with request.urlopen(url) as request_:
            res = json.load(request_)
            for i in res:
                if i.get('id') == int(ID_):
                    name = i.get('name')
                    break
            url2 = "https://jsonplaceholder.typicode.com/todos"
            with request.urlopen(url2) as req:
                res2 = json.load(req)
                a = 0
                for i in res2:
                    if i.get("userId") is int(ID_)\
                            and i.get("completed") is True:
                        a = a + 1
                        list_.append(i.get("title"))
                    if i.get("userId") == int(ID_):
                        b = b + 1
                print(f"Employee {name} is done with tasks({a}/{b}):")
                for i in list_:
                    print("\t ", end="")
                    print(i)
    except Exception as e:
        print(f"Error code: {e}")
