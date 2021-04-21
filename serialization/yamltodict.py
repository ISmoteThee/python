import yaml
import json
import xmltodict
with open('user.yaml', 'r') as file:
    data = yaml.safe_load(file)
user = data['user']
print(user['name'])
for role in user['roles']:
    print(' -', role)
user['location']['city'] = 'Corpus Christie'
with open('user-edit.yaml', 'w') as file:
    yaml.safe_dump(data, file, default_flow_style=False)
with open('user.json', 'w') as file:
    json.dump(data, file, indent=4)
with open('user.xml', 'w') as file:
    file.writelines(xmltodict.unparse(data, pretty=True))
    



