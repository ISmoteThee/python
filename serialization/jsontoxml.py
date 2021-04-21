import json
import xmltodict
with open('server.json', 'r') as file:
    server = json.load(file)
print(server)

with open('server.xml', 'w') as file:
    file.writelines(xmltodict.unparse(server, pretty=True))
    



