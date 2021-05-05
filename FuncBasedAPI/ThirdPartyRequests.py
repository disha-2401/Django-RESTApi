#this program is only for when w e doct have postman

import requests
import json

URL = "http://127.0.0.1:8000/FuncBasedAPI/hello"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)

# get_data()


def post_data():
    data = {
        'name': 'vihaan',
        'roll': 30,
        'city': 'surat'
    }
    headers={'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL, headers=headers ,data=json_data)
    data = r.json()
    print(data)

post_data()


def update_data():
    data = {
        'id': 23,
        'name': 'chomu',
        'roll': 31,
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)

# update_data()


def delete_data():
    data = {'id': 3}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)


#delete_data()
