import json

with open('user.json','r') as file:
    data = json.load(file)
user = data['user']
print(user['name'])
for role in user['roles']:
    print(' -', role)

user['location']['city'] = 'Plano'
with open('user-edit.json','w') as file:
    json.dump(data, file, indent=4)

