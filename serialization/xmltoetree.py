import xml.etree.ElementTree as ET

with open('user.xml', 'r') as file:
    mytree = ET.parse(file)
user = mytree.getroot()
#user = myroot.find('user')
print(user.find('name').text)
for role in user.findall('roles'):
    print(role.text)

user.find('location').find('city').text = 'Corpus Cristi'
with open('user-edit.xml', 'w') as file:
    mytree.write(file, encoding='unicode')