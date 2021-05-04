import requests
URL="http://127.0.0.1:8000/api/BTS/2"
print(requests.get(url=URL).json())
