import yaml
import json
import xmltodict
import os

with open('user.yaml', 'r') as file:
    data = yaml.safe_load(file)

user = data['user']
print(user['name'])
for role in user['roles']:
    print(' -', role)
user['location']['city'] = 'Corpus Christie'

os.makedirs('autoGen')

with open('autoGen/user-edit.yaml', 'w') as file:
    yaml.safe_dump(data, file, default_flow_style=False)
with open('autoGen/user.json', 'w') as file:
    json.dump(data, file, indent=4)
with open('autoGen/user.xml', 'w') as file:
    file.writelines(xmltodict.unparse(data, pretty=True))
    



