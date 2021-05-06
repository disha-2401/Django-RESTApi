# this program is only for when w e doct have postman

import requests
import json

URL = "http://127.0.0.1:8000/FuncBasedAPI/StudentInfo/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r = requests.get(url=URL, headers=headers,data=json_data)
    data = r.json()
    print(data)


#get_data(2)


def post_data():
    data = {
        "name": "disha",
        "roll": 31,
        "city": "surat"
    }
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


# post_data()


def put_data():
    data = {
        'name': 'Disha',
        'roll': 25,
        'city':'surat'
    }
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url=URL+'2', headers=headers, data=json_data)
    data = r.json()
    print(data)


# put_data()

def patch_data():
    data = {
        'name': 'Disha',
        'roll': 10,
    }
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.patch(url=URL+'2', headers=headers, data=json_data)
    data = r.json()
    print(data)

# patch_data()

def delete_data():
    headers = {'content-Type': 'application/json'}
    r = requests.delete(url=URL+"2", headers=headers)
    data = r.json()
    print(data)

# delete_data()
