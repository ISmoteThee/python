import requests
import json
from pprint import pprint

url = 'https://jsonplaceholder.typicode.com/users/2'

response = requests.get(url=url, params=None)
status_code = response.status_code
content = json.loads(response.content)

print(f'Status code: {status_code}')
for item in content:
    if type(content[item]) == dict:
        print(f'--------------{item}--------------')
        for subitem in content[item]:
            print(f'{subitem:>14}:  {content[item][subitem]}')
        print('-----------------------------------')
    else:
        print(f'{item:>10}:  {content[item]}')
