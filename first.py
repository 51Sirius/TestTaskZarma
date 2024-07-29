import requests
import json

data = requests.get('https://jsonplaceholder.typicode.com/posts').json()
with open('data.json', 'w') as f:
    json.dump(data, f)