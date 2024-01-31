#!/usr/bin/python3
"""
This module for get data from users API
and export it to the 'ID.csv' file
"""
if __name__ == "__main__":
    import csv
    import json
    from sys import argv
    from urllib import request
    ID_ = argv[1]
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

                csv_file_path = f'{argv[1]}.csv'
                data = []
                with open(csv_file_path, 'w', newline='') as csvfile:
                    for i in range(len(res2)):
                        if res2[i].get("userId") is int(ID_):
                            status = res2[i].get('completed')
                            csv_list = [str(argv[1]),
                                        username,
                                        status,
                                        res2[i].get('title')]
                            data.append(csv_list)
                    csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
                    csv_writer.writerows(data)
    except Exception as e:
        print(f"Error code: {e}")
